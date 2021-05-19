import math, cmath

#--------------------------------------------
#Input data
#--------------------------------------------

Z = 60
K_db = 10
K_val = math.pow(10, K_db/20)

#--------------------------------------------
#Calc Pi-pad attenuator
#--------------------------------------------
R1_R3 = Z*((K_val+1)/(K_val-1))
R2 = Z*((K_val**2-1)/(2*K_val))
print(f"Pi-pad R1,R3 = {round(R1_R3,2)}")
print(f"Pi-pad    R2 = {round(R2,2)}")


#--------------------------------------------
#Calc O-pad attenuator
#--------------------------------------------
R1_R3 = Z*((K_val+1)/(K_val-1))
R2 = Z*((K_val**2-1)/(2*K_val))*0.5

print(f"O-pad R1,R3 = {round(R1_R3,2)}")
print(f"O-pad    R2 = {round(R2,2)}")

