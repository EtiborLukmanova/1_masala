import time
import asyncio
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
    return wrapper

@timer
def find_primes_synchronous(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

@timer
async def find_primes_asynchronous(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
            await asyncio.sleep(1)
    return primes

print("Sync function:")
find_primes_synchronous(10000)

print("\nAsync function:")
asyncio.run(find_primes_asynchronous(10000))
