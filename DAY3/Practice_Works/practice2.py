import asyncio
async def get_weather():
    print("Getting Data..")

    await asyncio.sleep(4)

    print("Fetched Weather Data..")
async def send_to_server():
    print("Sending To Server")

    await asyncio.sleep(3)

    print("Data Sent Sucessfully..")

async def main():
    await get_weather()
    await send_to_server()

asyncio.run(main())
print("ksdshksfghfsgsh")