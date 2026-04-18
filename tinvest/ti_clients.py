import sys
import importlib
from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator
import asyncio

import grpc
import httpx
from google.protobuf.json_format import MessageToJson

from .ti_task import Task
from .errors import get_error_by_code




class Client(ABC):
    def __init__(self, token, url):
        self.url = url
        self.token = token


    @abstractmethod
    async def get_response(self, task: Task | None):
        pass



class RESTClient(Client):
    def __init__(self, token, url):
        super().__init__(token, url)

        self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {self.token}'
            }

        self.client = httpx.AsyncClient(headers=self.headers, 
                                        verify=False,
                                        timeout=10.0)


    async def get_response(self, task: Task | None):
        if task:
            try:
                response = await self.client.post(
                    f'{self.url}.{task.service}/{task.method}', 
                    json=task.data)
                return response.content.decode()
            except Exception as e:
                return(get_error_by_code(701, self, e))
        return(get_error_by_code(702, self))

    async def close(self):
        await self.client.aclose()



class GRPCClient(Client):
    def __init__(self, token, url):
        super().__init__(token, url)

        self.headers = [
                ('authorization', f'Bearer {self.token}')
        ]

        self.options = [
            ('grpc.keepalive_time_ms', 30000),
            ('grpc.keepalive_timeout_ms', 20000),
            ('grpc.keepalive_permit_without_calls', 1),
            ('grpc.initial_reconnect_backoff_ms', 1000),
            ('grpc.max_reconnect_backoff_ms', 30000),
            ('grpc.http2.max_pings_without_data', 0)
        ]
        
        self.root_certificates = None
        with open('tinvest/certs/russian_trusted_root_ca.cer', 'rb') as f:
            self.root_certificates = f.read()

        self.channel = grpc.aio.secure_channel(
            self.url,
            credentials=grpc.ssl_channel_credentials(root_certificates=self.root_certificates),
            options=self.options
        )


    async def get_response(self, task: Task | None):
        if task:
            try:
                pb2 = importlib.import_module(f'tinvest.protos.{task.service}_pb2')
                sys.modules[f'{task.service}_pb2'] = pb2
                pb2_grpc = importlib.import_module(f'tinvest.protos.{task.service}_pb2_grpc')
                sys.modules[f'{task.service}_pb2_grpc'] = pb2_grpc

                request_class = getattr(pb2, f'{task.body_name_request}')

                stub_class = getattr(pb2_grpc, f'{task.service}Stub')
                stub = stub_class(self.channel)

                method = getattr(stub, task.method)

                req = request_class(**task.data)

                response = await method(req, metadata=self.headers)
                return MessageToJson(response, preserving_proto_field_name=False)

            except (ModuleNotFoundError, AttributeError) as e:
                return(get_error_by_code(706, self, e))
            
            except Exception as e:
                return(get_error_by_code(701, self, e))
        return(get_error_by_code(702, self))
    


class GRPCStreamClient(GRPCClient):

    async def get_response(self, task: Task | None) -> AsyncGenerator[str, None]:
        if not task:
            yield get_error_by_code(702, self)
            return

        try:
            pb2 = importlib.import_module(f'tinvest.protos.{task.service}_pb2')
            sys.modules[f'{task.service}_pb2'] = pb2
            pb2_grpc = importlib.import_module(f'tinvest.protos.{task.service}_pb2_grpc')
            sys.modules[f'{task.service}_pb2_grpc'] = pb2_grpc

            request_class = getattr(pb2, f'{task.body_name_request}')

            stub_class = getattr(pb2_grpc, f'{task.service}Stub')
            stub = stub_class(self.channel)

            method = getattr(stub, task.method)

            req = request_class(**task.data)
            meth = method(req, metadata=self.headers)

            async for response in meth:
                res = MessageToJson(response, preserving_proto_field_name=False)
                if not res:
                    continue
                yield res
                #await asyncio.sleep(3)


        except asyncio.CancelledError as e:
            yield get_error_by_code(705, self, e)
            return

        except (ModuleNotFoundError, AttributeError) as e:
            yield get_error_by_code(706, self, e)
            return

        except Exception as e:
            yield get_error_by_code(701, self, e)
            return

