import httpx
import json
import asyncio
from .utils import async_timed


class Worker:

    def __init__(self, token, url):
        self.url = url
        self.token = token
        self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {self.token}'
            }


    @async_timed()
    async def getResponse(self, *tasks) -> list:
        _tasks = tasks if tasks else tuple()
        async with httpx.AsyncClient(verify=False) as client:
            queries = [client.post(f'{self.url}.{task.service}/{task.method}', 
                                headers=self.headers, 
                                json=task.data) for task in _tasks]
            responses = await asyncio.gather(*queries)
            return [json.loads(response.content.decode()) for response in responses]

    # @timed
    # def _getResponse(self, tasks=None):
    #     tasks = tasks if tasks else []
    #     responses = []
    #     for task in tasks:
    #         with httpx.Client(verify=False) as client:
    #             res = client.post(f'{self.url}.{task.service}/{task.method}', headers=self.headers, json=task.data)
    #         responses.append(json.loads(res.content.decode()))
    #     return responses


