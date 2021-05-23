Parallel Robotics- Documentation
=============================

- [Parallel Robots](#parallel-robots)
- [Delta Robots](#delta-robots)
- [Kinematic Analysis](#kinematic-analysis)
	 - [Kinematics of 2-DOF Delta robot](#1-kinematics-of-2-dof-delta-robot)
       - [Considering Frame and Base to be a point](#considering-frame-and-base-to-be-a-point)

## Parallel Robots
A Parallel Robot refers to a kinematic chain in which a fixed platform and moving platform are connected to each other by several serial Kinematic chains.

## Delta Robots
Delta Robot is a type of Parallel Robot consisting of 3 identical Kinematics chains connected to a Base, The key design feature of Delta Robots are the use of Parallelograms in the arms
which restrict the movement of the base/end plate to pure translation( i.e. Only movement in X,Y or Z direction) 
Delta Robots are known for it's high speed and high acceleration, Also having all the kinematic chains connected together to end-effector increases stiffness of the robot.

In this project we have Design a 3-DOF Delta Robot

## kinematic Analysis

+  Forward Kinematics: 
Forward kinematics refers to the use of the kinematic equations of a robot to compute the position of the end-effector from specified values for the joint parameters.

+  Inverse kinematics: 
Inverse kinematics is the mathematical process of calculating the variable joint parameters needed to place the end of a kinematic chain, when the end-effector position is given.

For the ease of understanding initially we develop a 2 DOF Delta parallel robot

### 1 Kinematics of 2-DOF Delta robot

##### Considering Frame and Base to be a point
Initially considering the 2-axis delta robot with frame and base length to be zero,let AB and AD be the upper links say L1, BC and DC 
be the lower links say L2. According to the standard design of a delta robot we assume the length of links L1 and L2 to be in the ratio 
of 1:2,hence L2 = 2(L1). We calculate the distance between the frame and base points using the basic trigonometric equations and 
the concept of pythagoras theorem.

###### Forward Kinematics:

Case 1: If both ϴ1 and ϴ2 are equal. i.e C(x,y) = (0,y)

![image1](https://user-images.githubusercontent.com/61882073/119257251-08d34a80-bbe2-11eb-862f-9eff98175196.png)

 From Δ ABC,

   <img src="https://bit.ly/2RDfPkT" align="center" border="0" alt="x= Sin( \theta 1) * L1" width="139" height="18" />
     
   <img src="https://bit.ly/2Q38CtM" align="center" border="0" alt="y = Cos( \theta 1)*L1" width="144" height="19" />                                         -----------(eqn-1)
   
   From ΔBCE,	 	 	 	
   
   <img src="https://bit.ly/3uyQ4Rd" align="center" border="0" alt="L_{2} ^{2} = z^{2}  +  x^{2}" width="100" height="25" />	 	 	
   
   <img src="https://bit.ly/33uEQBf" align="center" border="0" alt="z^{2} = L_{2} ^{2} -  x^{2} " width="100" height="25" />
   
   <img src="https://bit.ly/3o3pywH" align="center" border="0" alt="z=  \sqrt[]{(L_{2}^{2} - ( Sin^{2}( \theta_{1}))*L1^{2})} " width="233" height="31" />-------------(eqn-2)
  
   From eqn-1 and eqn-2,
   
  <img src="http://www.sciweavers.org/tex2img.php?eq=AC%20%3D%20y%2Bz&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="AC = y+z" width="89" height="19" />
   
   <img src="https://bit.ly/2RAxr0C" align="center" border="0" alt="AC = \sqrt[] {Cos( \theta_{1})*L_{1} + √(L_{2}^{2}-(Sin^{2}( \theta _{1}))*L_{1}^{2}) }" width="361" height="31" />
   
   
   Hence,the end-effector C(x,y) = C(0,AC)
