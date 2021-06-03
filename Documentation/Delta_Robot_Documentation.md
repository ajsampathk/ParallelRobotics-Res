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

****Case 1: If both ϴ1 and ϴ2 are equal. i.e C(x,y) = (0,y)****

![image1](https://user-images.githubusercontent.com/61882073/119257251-08d34a80-bbe2-11eb-862f-9eff98175196.png)

 From Δ ABC,

   ![image](https://user-images.githubusercontent.com/61882073/120584208-26f44280-c44d-11eb-800f-44d6819a4aac.png)                                         -----------(eqn-1)
   
   From ΔBCE,	 	 	 	
   
   ![image](https://user-images.githubusercontent.com/61882073/120584645-fbbe2300-c44d-11eb-8ea3-f0a52d7de9c3.png)					   -----------(eqn-2)


   From eqn-1 and eqn-2,
   
  ![image](https://user-images.githubusercontent.com/61882073/120585043-afbfae00-c44e-11eb-84e2-28a866ce7ebe.png)
   
   
   Hence,the position of end-effector C(x,y) = C(0,AC)
  
  
  
 
 
****Case 2: If both ϴ1 and ϴ2 are not equal. i.e C(x,y) = (x,y)****

![image](https://user-images.githubusercontent.com/61882073/120587592-41311f00-c453-11eb-9936-fe5ee75194eb.png)

When the two input angles are not equal the point C of the end effector traverses along the plane in x-direction and the imbalance is noted as ϴeffective. ϴeffective is calculated and the resulting end-effector position is known as follows,

Similar to Case 1,

![image](https://user-images.githubusercontent.com/61882073/120588499-ed273a00-c454-11eb-9c7a-cd2ed2f26c7d.png)
![image](https://user-images.githubusercontent.com/61882073/120588568-08924500-c455-11eb-9606-2c9d96f48837.png)

Hence the Coordinates of the End-effector C(x,y)=C(Xe,Ye)


###### Inverse Kinematics:
