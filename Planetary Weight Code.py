#Title: Inter Planetary Weights Project
#Author: Zaily Alvarado
#Date: 9/29/2019

#1. Input user's name with a string function
sName=str(input("What is your name: "))

#2. Input user's weight with a float function in case there are decimal values
nWeight=float(input("What is your weight: "))

#3. Calculations
# Store the weight * each individual planetary constant value into an appropiate variable
nMercury_Weight = nWeight * 0.38
nVenus_Weight = nWeight * 0.91
nMoon_Weight = nWeight * 0.165
nMars_Weight = nWeight * 0.38
nJupiter_Weight = nWeight * 2.34
nSaturn_Weight = nWeight * 0.93
nUranus_Weight = nWeight * 0.92
nNeptune_Weight = nWeight * 1.12
nPluto_Weight = nWeight * 0.066

#4. Output
# (Name) here are your weights on our Solar System's planets:
#Weight on (x planet): format(planet weight variable, '10.2f'))

print(sName + " here are your weights on our Solar System's planets:")
print("Weight on Mercury:" + format(nMercury_Weight,'10.2f'))
print("Weight on Venus:" + format(nVenus_Weight,'10.2f'))
print("Weight on our moon:" + format(nMoon_Weight,'10.2f'))
print("Weight on Mars:" + format(nMars_Weight,'10.2f'))
print("Weight on Jupiter:" + format(nJupiter_Weight,'10.2f'))
print("Weight on Saturn:" + format(nSaturn_Weight,'10.2f'))
print("Weight on Uranus:" + format(nUranus_Weight,'10.2f'))
print("Weight on Neptune:" + format(nNeptune_Weight,'10.2f'))
print("Weight on Pluto:" + format(nPluto_Weight,'10.2f'))
