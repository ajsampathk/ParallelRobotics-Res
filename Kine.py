import math

F=200
L1=800
L2=1600

def fkine(Ltheta,Rtheta):
  
  Pl = (L1*math.sin(math.radians(Ltheta))-F,L1*math.cos(math.radians(Ltheta)))
  Pr = (L1*math.sin(math.radians(Rtheta))+F,L1*math.cos(math.radians(Rtheta)))
  #print("PL:{},PR:{}".format(Pl,Pr))
  lr = (L1*(math.sin(math.radians(Rtheta))-math.sin(math.radians(Ltheta)))+2*F)**2 + (L1*(math.cos(math.radians(Rtheta))-math.cos(math.radians(Ltheta))))**2
  lf = (L1*math.sin(math.radians(Ltheta)) - F)**2 + (L1*math.cos(math.radians(Ltheta)))**2
  rf = (L1*math.sin(math.radians(Rtheta)) + F)**2 + (L1*math.cos(math.radians(Rtheta)))**2
  Dlr = math.sqrt(lr)
  Dlf = math.sqrt(lf)
  Drf = math.sqrt(rf)
  
  thetaA = math.acos((Dlr**2)/(2*Dlr*L2))
  thetaB = math.acos((Dlf**2 + Dlr**2 - Drf**2)/(2*Dlf*Dlr))
  
  Dfe = math.sqrt(Dlf**2 + L2**2 - 2*Dlf*L2*math.cos(thetaA+thetaB))
  print("Dist_FE: {}".format(Dfe))
  thetaC = math.acos((Dfe**2+Dlf**2-L2**2)/(2*Dfe*Dlf))
  thetaD = math.acos((Dlf**2+F**2-L1**2)/(2*F*Dlf))
  
  thetaEff = (thetaC+thetaD-(math.pi/2))/2
  print("Ang_FE: {}".format(math.degrees(thetaEff)))
  X = Dfe*math.sin(thetaEff)
  Y = Dfe*math.cos(thetaEff)
  print("FK-(x,y):{}".format((X,Y)))
  return (X,Y)

def ikine(x,y):
  Xl = (x + F)**2 +(y**2)
  Xl = math.sqrt(Xl)
  Xr = (x - F)**2 +(y**2)
  Xr = math.sqrt(Xr)
  print("Xl:{},Xr:{}".format(Xl,Xr))
  R=[]
  R.append((F**2+Xl**2 - Xr**2)/(2*Xl*F))
  R.append((F**2+Xr**2 - Xl**2)/(2*Xr*F))
  R.append((L1**2+Xl**2 - L2**2)/(2*L1*Xl))
  R.append((L1**2+Xr**2 - L2**2)/(2*Xr*L1))
  
  theta = [math.acos(r) for r in R]
#  print("Theta:{}".format(theta))
  Ltheta = theta[0]+theta[2]
  Rtheta = theta[1]+theta[3]
  print("L-Theta:{},R-Theta:{}".format(90-math.degrees(Ltheta),math.degrees(Rtheta)-90))
  return (90-math.degrees(Ltheta),math.degrees(Rtheta)-90)

if __name__=='__main__':
  (x,y) = input("x,y: ")
  (L,R) = ikine(x,y)
  print("-----\nIK-{}\n-----".format((L,R)))
  cart=fkine(L,R)
  print("-----\nFK-{}\n-----".format(cart))
