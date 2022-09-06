import fibo

def main():
    fibo.fib(1000)
    print(fibo.sum(10))
    print(fibo.__name__)
    print(__name__)
    
if __name__ == "__main__":
    main()