import math

r = 10   #radius of the circle
offset = 48



for t in range(0,361):
    theta=math.radians(t)
    time = t/10   #in seconds
    xe =round(r*math.cos(theta),4)
    ye= round(r*math.sin(theta),4) + offset
    #parameters.append((x,y,t,time))  
    l1 = 20
    l2 = 40
    f = 10

    d1 = math.sqrt((xe + f )**2 + (ye)**2)   
    d2 = math.sqrt((xe - f )**2 + (ye)**2) 
    d = math.sqrt((xe)**2 + (ye)**2)         

    tx = math.acos(((l1*l1) - (l2*l2) + (d1**2))/(2*l1*d1))
    temp = ((l1**2) - (l2**2) + (d2**2))/(2*l1*d1)
    print(temp)
    ty = math.acos(temp)

    te1 = math.acos(((d1**2) + (f**2) - (d**2))/ (2*f*d1))
    te2 = math.acos(((d2**2) + (f**2) - (d**2))/ (2*f*d2))

    tl = math.radians(90) - (te1 + tx)
    tr = te2 + ty - math.radians(90)


    print(math.degrees(tl),math.degrees(tr)) 
    

#print(parameters)

