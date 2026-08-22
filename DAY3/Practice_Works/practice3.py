# fetching data from a fake api
import httpx
import asyncio


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        result = await client.get(url)
        return result.json()


result = asyncio.run(fetch_data("https://fakestoreapi.com/products/1"))
print(result)