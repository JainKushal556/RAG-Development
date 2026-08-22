import time
import asyncio
start = time.time()

# print("Normal Syncrronus Function")
def fun1():
    print("start fun1")
    time.sleep(5)
    print("end fun1")

def fun2():
    print("start fun2")
    time.sleep(2)
    print("end fun2")

async def fun3():
    print("start fun3")
    await asyncio.sleep(5)
    print("end fun3")

async def fun4():
    print("start fun4")
    await asyncio.sleep(2)
    print("end fun4")

async def main():
    result = await asyncio.gather(fun3(),fun4())
    print(result)
# asyncio.run(main())
asyncio.run(fun3())


# fun1()
# fun2()
end = time.time()
print(end-start)