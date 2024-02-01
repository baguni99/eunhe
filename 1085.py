import math
x,y,w,h=map(int,input().split())
print(math.sqrt((x-w)**2+(y-h)**2))


x,y,w,h=map(int,input().split())
print(min(x,y,w-x,h-y))