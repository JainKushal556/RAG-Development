# Here We Can Provide Any Api Then Provide Any Id To Get The Exact Data

import httpx
import asyncio


# Fake Api : https://jsonplaceholder.typicode.com/todos


async def fetch_data(client,url,id):
    print("Fetch Started.....")
    result = await client.get(f"{url}/{id}")
    print("Fetch Completed.....")
    return result.json()
    
async def main(url,id):
    async with httpx.AsyncClient() as client:
        print("Waiting For Response...")
        result = await fetch_data(client,url,id)
        print("Response Recived...")
        return result


url = input("Enter API (url): ")
id = int(input("Which Records U Want: "))

fetched_data = asyncio.run(main(url,id))
keys = fetched_data.keys()

print(".........Data..........")
for key in keys:
    print(key,": ",fetched_data[key])
#   print(key,fetched_data[key])




