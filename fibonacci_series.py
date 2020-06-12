# fibonacci_series
n1=0
n2=1
fibonacci=[n1,n2]
#enter the number of terms you want
n=int(input())
for i in range(n):
    fibonacci.append(n1+n2)
    n3=n1+n2
    n1=n2
    n2=n3
    
print(fibonacci)
