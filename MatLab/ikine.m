function [Ltheta,Rtheta] = ikine(F,L1,L2,P)
%Inverse Kinematic Function for 2-Axis delta robot
%ikine(Frame,Link1,Link2,[X,Y])
    Lf = [F,0];
    Rf = [-F,0];
    XL = norm(P-Lf);
    XR = norm(P-Rf);
    
    ThetaXL = CosineLaw(F,XL,XR);
    ThetaXR = CosineLaw(F,XR,XL);
    ThetaL = CosineLaw(L1,XL,L2);
    ThetaR = CosineLaw(L1,XR,L2);
    
    Ltheta = (pi/2) - (ThetaXL+ThetaL);
    Rtheta = (ThetaXR+ThetaR) - (pi/2);
    
    
end