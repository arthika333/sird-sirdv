#include the required libraries 
import numpy as np 
import matplotlib.pyplot as plt 

#set the values for constants 
#sirdv 
N=1000 
b=0.5  
g=1/7   
m=0.01  
a=0.00121  
e=0.49  

#total population 
#transmission rate 
#days flu lasts = 7 days so the recovery rate is the inverse 
#death rate 0.1 % 
#0.121 % of susceptible population get vaccinated everyday 
#vaccine efficacy = 49%  

steps=np.arange(0,366,dtype=int) 
time=1*steps 

#define the sird function to calculate the equations 
def SIRDV(s,i,r,d,v,b,g,m,e,a): 
    sdash= -s*i*(b/(s+i+r+d+v))-(a*s) 
    rdash=g*i 
    idash=((s*i*b)/(s+i+r+d+v))-(g*i)-(m*i) 
    ddash=m*i 
    vdash=(a*s)-((e*b*i*v)/(s+i+r+d+v)) 
    return sdash, idash, rdash, ddash, vdash 

#create lists to store values 
tlen=len(time) 
s=np.empty([tlen]) 
i=np.empty([tlen]) 
r=np.empty([tlen]) 
d=np.empty([tlen]) 
v=np.empty([tlen]) 

#initialize variables 
i[0]=1 
r[0]=0 
d[0]=0 
v[0]=0 
s[0]=N-i[0]-r[0]-d[0]-v[0] 
dt=0.1 

#create loop to update variables 
for t in steps: 
    if t<len(steps)-1: 
        sdash, idash, rdash, ddash, vdash= SIRDV(s[t],i[t],r[t],d[t],v[t],b,g,m,e,a) 
        s[t+1]=s[t]+dt*sdash 
        i[t+1]=i[t]+dt*idash 
        r[t+1]=r[t]+dt*rdash 
        d[t+1]=d[t]+dt*ddash 
        v[t+1]=v[t]+dt*vdash 

#plot the graph 
plt.plot(time,s,label='susceptible') 
plt.plot(time,i,label='infected') 
plt.plot(time,r,label='recovered') 
plt.plot(time,d,label='deceased') 
plt.plot(time,v,label='vaccinated') 
plt.xlabel('time in days') 
plt.ylabel('no of people') 
plt.legend() 
plt.show() 
