import sys

input = sys.stdin.readline

n = int(input())
a = int(n//3)
b = int(n//5)
check = b+1

for i in reversed(range(b+1)):
    m = n-5*i
    if(m==0):
        print(i)
        break
    elif (m%3==0):
        print(int(i+m/3))
        break
    else:
        check -= 1
        continue 

if(check ==0):
    print(-1)        

    
        
      
