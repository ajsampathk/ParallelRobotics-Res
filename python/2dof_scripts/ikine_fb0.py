import math

l1=20
l2=40

#assigningt he co-ordinates of the end effector
x,y = 0,25

d = math.sqrt(x**2 + y**2)

t = math.atan(x/y)  #slope

#using cosine rule
t_eff = math.acos((l1**2 + d**2 - l2**2)/(2*l1*d))

t1,t2 = abs(t-t_eff),abs(t+t_eff) #compensating shift from reference

print(math.degrees(t1),math.degrees(t2))