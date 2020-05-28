# Tail recursion i stedet for den almenlige fib(n): return fib(n-1) + fib(n-2)
def fib(n):
    return go(n, 0, 1)
    
def go(n, a, b):
    #print(str(n))
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        #print("a: " + str(a) + " b: " + str(b) + " n: " + str(n))
        return go(n-1, b, b+a)

val =input("Enter a number: ")
print fib(val)
