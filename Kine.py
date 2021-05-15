import math
from math import pi,cos,sin,radians
import numpy as np

F=10
L1=20
L2=40

def Fkine(Ltheta,Rtheta):
  Pl = (-F-L1*cos(pi+radians(Ltheta)),L1*sin(radians(Ltheta)))
  Pr = (F+L1*cos(pi+radians(Rtheta)),L1*sin(radians(Rtheta)))
  Pl=np.array(Pl)
  Pr=np.array(Pr)
  print("\tP(L) = {}\n\tP(R) = {}".format(Pl,Pr))
  diff = Pl-Pr
  d = math.sqrt(np.sum(diff**2))
  theta  = math.atan(diff[1]/diff[0])
  phi = math.acos(d/(2*L2))
  print("\td = {}\n\tTheta = {}\n\tPhi = {}".format(d,theta,phi))

  Pd = [L2*cos(phi-theta),L2*sin(phi-theta)]
  Pd = np.array(Pd)
  Pe = Pl+Pd

  print("\t(X,Y) = {}".format(np.round(Pe,2)))
  return(Pe)

def Ikine(Pe):
  Ol = np.array([-F,0])
  Or = np.array([F,0])
  dl = math.sqrt(np.sum((Pe-Ol)**2))
  dr = math.sqrt(np.sum((Pe-Or)**2))
  print("\tD(L) = {}\n\tD(R) = {}".format(dl,dr))
  thetaL = math.acos((F+Pe[0])/dl)
  thetaR = math.acos((F-Pe[0])/dr)
  phiL = math.acos((L1**2+dl**2-L2**2)/(2*dl*L1))
  phiR = math.acos((L1**2+dr**2-L2**2)/(2*dr*L1))
  Ltheta = math.degrees(thetaL+phiL)
  Rtheta = math.degrees(thetaR+phiR)
  print("\tTh(L,R) = {}\n\tPhi(L,R) = {}\n\tTheta(L,R) = {}".format((thetaL,thetaR),(phiL,phiR),(Ltheta,Rtheta)))

if __name__=='__main__':
  (L,R) = input("Ltheta,Rtheta(deg):")
  Pe = Fkine(L,R)
  Ikine(Pe)
