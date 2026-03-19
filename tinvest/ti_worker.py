import httpx


class Worker:
    def __init__(self, token, url):
        self.url = url
        self.token = token
        self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {self.token}'
            }

        self.client = httpx.AsyncClient(verify=False)


    async def getResponse(self, task):
        response = None
        try:
            response = await self.client.post(f'{self.url}.{task.service}/{task.method}',
                                    headers=self.headers, json=task.data)
        except Exception as e:
            print(f"Error: {e}, Response: {response}")
        return response
        



