Parallel Robotics- Documentation
=============================

- [Parallel Robots](#parallel-robots)
- [Delta Robots](#delta-robots)
- [Kinematic Analysis](#kinematic-analysis)
	 - [Kinematics of 2-DOF Delta robot](#1-kinematics-of-2-dof-delta-robot)
        - [Considering Frame and Base to be a point](#considering-frame-and-base-to-be-a-point)
       - [Considering Frame to be of some unit (2f) and Base to be a point](#considering-frame-to-be-of-some-unit-and-base-to-be-a-point)
      

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

Let C(x,y) be the given parameters, then the end-effector values can be represented in cartesian form as

![image](https://user-images.githubusercontent.com/61882073/120752446-5c6d5e80-c527-11eb-9dc9-57f358618987.png)                 (Converting the distance and angle obtained from polar form to cartesian form)

![image](https://user-images.githubusercontent.com/61882073/120752687-ba01ab00-c527-11eb-89e3-a988a842084f.png)

Using Cosine Rule,

![image](https://user-images.githubusercontent.com/61882073/120752745-c8e85d80-c527-11eb-88eb-5eb4da4b8122.png)

![image](https://user-images.githubusercontent.com/61882073/120752786-da316a00-c527-11eb-882f-3a49d3351076.png)

![image](https://user-images.githubusercontent.com/61882073/120752818-e87f8600-c527-11eb-8884-ec06f391cfbd.png)

![image](https://user-images.githubusercontent.com/61882073/120752853-f33a1b00-c527-11eb-9695-28e9c643076a.png)

![image](https://user-images.githubusercontent.com/61882073/120755680-ea4b4880-c52b-11eb-817b-a663c9337fc2.png)

Hence we obtain the resulting joint angles ϴ1,ϴ2.


##### Considering Frame to be of some unit (2f) and Base to be a point
Consider the frame length to be 2f and base length to be Zero.. Let AB and ED be the upper links, say L1, BC and DC be the lower links, say L2. According to the standard design of a delta robot we assume the length of links L1 and L2 to be in the ratio of 1:2,hence L2 = 2(L1). We calculate the distance between the frame and base points using the basic trigonometric equations and the concept of pythagoras theorem.

###### Forward Kinematics:

****Case 1: If both ϴ1 and ϴ2 are equal. i.e C(x,y) = (0,y)****

![image](https://user-images.githubusercontent.com/61882073/120756723-3ba80780-c52d-11eb-83c0-06365ec4e8ac.png)

From ΔABP,

![image](https://user-images.githubusercontent.com/61882073/120756774-51b5c800-c52d-11eb-8598-c577e0a642f6.png)						 -----------(eqn-1)

From ΔBCE,	

![image](https://user-images.githubusercontent.com/61882073/120756912-7d38b280-c52d-11eb-8db2-3d51ec5001e4.png)

![image](https://user-images.githubusercontent.com/61882073/120756942-8aee3800-c52d-11eb-9166-e4b1e5b89131.png)

![image](https://user-images.githubusercontent.com/61882073/120757146-c983f280-c52d-11eb-9a21-0383f6f434aa.png)						-----------(eqn-2)


From eqn-1 and eqn-2,
AC = y + z

![image](https://user-images.githubusercontent.com/61882073/120757242-ea4c4800-c52d-11eb-97e4-844935446721.png)
Hence,the end-effector position C(x,y) = C(0,AC)

****Case 2: If both ϴ1 and ϴ2 are not equal. i.e C(x,y) = (x,y)****
When the two input angles are not equal the point C of the end effector traverses along the plane in x-direction and the imbalance is noted as ϴeffective. The below diagram represents the situation where in ϴeffective is calculated and the resulting end-effector position is known as follows,

![image](https://user-images.githubusercontent.com/61882073/120758794-e6b9c080-c52f-11eb-9fc3-364120f99135.png)

![image](https://user-images.githubusercontent.com/61882073/120758833-f33e1900-c52f-11eb-88b0-fb6026665bf8.png)

![image](https://user-images.githubusercontent.com/61882073/120758854-f9cc9080-c52f-11eb-87b0-d617dd96dc29.png)

Using Distance Formula

![image](https://user-images.githubusercontent.com/61882073/120758894-05b85280-c530-11eb-9cc9-70eb636d30ce.png)

Consider ΔBDC,
Using Cosine Rule,

![image](https://user-images.githubusercontent.com/61882073/120760188-790e9400-c531-11eb-96d3-b8ac1d1317c5.png)

![image](https://user-images.githubusercontent.com/61882073/120761250-9f80ff00-c532-11eb-8246-41c6f14c4026.png)

![image](https://user-images.githubusercontent.com/61882073/120761285-a740a380-c532-11eb-9004-0070104cca83.png)

![image](https://user-images.githubusercontent.com/61882073/120761336-b6275600-c532-11eb-995d-7bf08f827fca.png)

Hence we obtain the value of end effector position C(X,Y)=(x,y) and ϴ effective.

###### Inverse Kinematics:

![image](https://user-images.githubusercontent.com/61882073/120761427-cc351680-c532-11eb-8cc7-e8024d63c091.png)

![image](https://user-images.githubusercontent.com/61882073/120761512-e5d65e00-c532-11eb-8f60-ee988a321bcb.png)

![image](https://user-images.githubusercontent.com/61882073/120761553-f38be380-c532-11eb-835c-9ab0a35515fe.png)

![image](https://user-images.githubusercontent.com/61882073/120761590-fbe41e80-c532-11eb-8071-8968038819b5.png)

From ΔABC, ∠BAC=ϴ1
Using Cosine Rule

![image](https://user-images.githubusercontent.com/61882073/120761635-09010d80-c533-11eb-8a90-5f1080454a8f.png)

![image](https://user-images.githubusercontent.com/61882073/120761717-1d450a80-c533-11eb-9e8a-9129b15661f8.png)

From ΔAFC,  ∠CAF=ϴe1
Using Cosine Rule,

![image](https://user-images.githubusercontent.com/61882073/120762236-aa885f00-c533-11eb-96e2-57e20c6ce4a6.png)

![image](https://user-images.githubusercontent.com/61882073/120762270-b411c700-c533-11eb-80c9-d193e200d3ad.png)

From ΔDEC, ∠DEC=ϴ2
Using Cosine Rule,

![image](https://user-images.githubusercontent.com/61882073/120763037-77929b00-c534-11eb-8322-f9da3bd164a5.png)

![image](https://user-images.githubusercontent.com/61882073/120763070-7eb9a900-c534-11eb-8f7b-b4c45fb39c2d.png)

From ΔCEF, ∠CEF=ϴe2
Using Cosine Rule,

![image](https://user-images.githubusercontent.com/61882073/120763160-95600000-c534-11eb-8ef9-e5a2af2fa0d7.png)

![image](https://user-images.githubusercontent.com/61882073/120763190-9d1fa480-c534-11eb-8890-0cba28b78236.png)

![image](https://user-images.githubusercontent.com/61882073/120763226-a446b280-c534-11eb-8fa1-03769e8671fb.png)

Hence we obtain the values of joint Angles ϴL and ϴR





