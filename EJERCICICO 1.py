import time

def fibonacci(n, recursive=True):
    if recursive:
        return n if n <= 1 else fibonacci(n - 1, True) + fibonacci(n - 2, True)
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

def compare_execution_times():
    ns = [1, 10, 20, 30, 40]
    for n in ns:
        start_time = time.time()
        fib_rec = fibonacci(n, recursive=True)
        rec_time = time.time() - start_time

        start_time = time.time()
        fib_iter = fibonacci(n, recursive=False)
        iter_time = time.time() - start_time

        print(f"n = {n}: Fibonacci = {fib_rec}, Recursivo = {rec_time:.6f}s, Iterativo = {iter_time:.6f}s")

if __name__ == "__main__":
    compare_execution_times()
