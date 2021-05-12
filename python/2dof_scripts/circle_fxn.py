import math

radius = 10   #radius of the circle

parameters = []


for t in range(0,361):
    theta=math.radians(t)
    time = t/100   #in seconds
    x =round(radius*math.cos(theta),4)
    y= round(radius*math.sin(theta),4) 
    parameters.append((x,y,t,time))   
    

print(parameters)

