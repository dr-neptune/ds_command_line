def factorial(x):
    if x == 1: 
        return 1
    else: 
        return x * factorial(x-1)

if __name__ == "__main__": 
    import sys
    x = int(sys.argv[1])
    print("The factorial of ", x, " is ", factorial(x))
