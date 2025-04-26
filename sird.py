#include the required libraries 
import numpy as np 
import matplotlib.pyplot as plt 

#set the values for constants 
#sird 
N=1000 
b=0.5  
g=1/7   
m=0.01  

#total population 
#transmission rate 
#days flu lasts = 7 days so the recovery rate is the inverse 
#death rate 0.1 % 

steps=np.arange(0,366,dtype=int) 
time=1*steps 

#define the sird function to calculate the equations 
def SIRD(s,i,r,d,b,g,m): 
        sdash= -s*i*(b/(s+i+r+d)) 
        rdash=g*i 
        idash=((s*i*b)/(s+i+r+d))-(g*i)-(m*i) 
        ddash=m*i 
        return sdash, idash, rdash, ddash 

#create lists to store values 
tlen=len(time) 
s=np.empty([tlen]) 
i=np.empty([tlen]) 
r=np.empty([tlen]) 
d=np.empty([tlen]) 

#initialize variables 
i[0]=1 
r[0]=0 
d[0]=0  
s[0]=N-i[0]-r[0]-d[0] 
dt=0.1 

#create loop to update variables 
for t in steps: 
        if t<len(steps)-1: 
                sdash, idash, rdash, ddash= SIRD(s[t],i[t],r[t],d[t],b,g,m) 
                s[t+1]=s[t]+dt*sdash 
                i[t+1]=i[t]+dt*idash 
                r[t+1]=r[t]+dt*rdash 
                d[t+1]=d[t]+dt*ddash
                
#plot the graph 
plt.plot(time,s,label='susceptible') 
plt.plot(time,i,label='infected') 
plt.plot(time,r,label='recovered') 
plt.plot(time,d,label='deceased') 
plt.xlabel('time in days') 
plt.ylabel('no of people') 
plt.legend() 
plt.show()
