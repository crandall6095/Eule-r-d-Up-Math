import cmath as mh

x0 = float(input("Initial x0: "))
y0 = float(input("Initial y0: "))
h = float(input("Step size: "))
n = int(input("Number of steps: "))

x = x0
y = y0


for i in range(n):
    dxdy = (((mh.cos(mh.exp(y)))**2 - mh.log(x**2 + mh.sqrt(mh.pi)))/((mh.exp(y**2 - x**(1/3))) + 5**(x-y))) ##enter differential equation, use x & y: eg. 2*x+y
    y1 = y+h*dxdy
    x1 = x+h
    x = x1
    y = y1

print(f"Step {i+1}: x = {x1}, y = {y1}")