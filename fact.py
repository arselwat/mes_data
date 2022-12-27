# def factoriel (n) :
#     if n==0:
#         return 1
#     else:
#         return n*factoriel(n-1)
# print(factoriel(1000))
import time
def factoriel(n):
    if n==0:
        return 1
    else:
        f=1
        for k in range(2,n+1):
            f=f*k
        return f

for i in range(10):
    d=time.perf_counter()*1000
    print(factoriel(600),"\n")
    f=time.perf_counter()*1000
    print((f-d),"\n")
    
