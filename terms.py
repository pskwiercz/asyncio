import asyncio
import time

def sync_function(param: str) -> str:
    print("This is synchronous function")
    time.sleep(0.1)
    return f"Sync result: {param}"

# ALSO KNOWN AS A COROUTINE FUNCTION
async def async_function(param: str) -> str:
    print("This is anysynchronous function (coroutine function)")
    await asyncio.sleep(1)
    return f"Async result: {param}"

async def main():
    sync_result = sync_function("Test")
    print(sync_result)

    # --------------- FUTURE ---------------
    # loop = asyncio.get_running_loop()
    # future = loop.create_future() # promise that results will be available later
    # print(f"Empty future: {future}")
    #
    # future.set_result("Future result: Test")
    # future_result = await future
    # print(future_result)

    # --------------- COROUTINE ---------------
    coroutine_obj = async_function("Test")
    print(coroutine_obj)

    coroutine_result = await coroutine_obj
    print(coroutine_result)

    # --------------- TASK ---------------
    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)

if __name__ == "__main__":
    asyncio.run(main())