function [x,y] = fcn(t,r)
theta=deg2rad(t);
x = r*cos(theta);
y = r*sin(theta)+48;
end