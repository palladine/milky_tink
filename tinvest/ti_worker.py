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

        self.client = httpx.AsyncClient(headers=self.headers, verify=False)


    async def close(self):
        await self.client.aclose()


    async def getResponse(self, task):
        response = None
        try:
            response = await self.client.post(f'{self.url}.{task.service}/{task.method}', 
                                            json=task.data, timeout=1)
        except Exception as e:
            ...
        return (response, task.extras)  # кортеж (ответ, доп. инфа задачи)
    




