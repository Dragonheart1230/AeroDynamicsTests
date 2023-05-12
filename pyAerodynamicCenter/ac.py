# https://en.wikipedia.org/wiki/Pitching_moment#:~:text=In%20aerodynamics%2C%20the%20pitching%20moment,aerodynamic%20center%20of%20the%20airfoil
import csv
dataAirSpeed =[]
dataAoA = []
header =["AoA", "AirSpeed", "Moment", "Cm"]

def cm(aoa):
 return -0.0002* pow(aoa,3) -0.1

def q(u): #u = airspeed q= dynamic pressure
    airDensity = 1.293
    return 0.5 * airDensity * pow(u,2)
chord = 1
airSpeed = 0 #m/s
surfaceArea = 16
aoa = 0
moment = 0

while(airSpeed < 27.7778): #Airspeed less than 100km/h
    airSpeed+=0.1
    moment = cm(aoa)*q(airSpeed)*surfaceArea*chord
    dataAirSpeed.append([aoa, airSpeed, moment, cm(aoa)])

aoa = -15
airSpeed=27.7778
while(aoa<15):
    aoa +=0.1
    moment = cm(aoa)*q(airSpeed)*surfaceArea*chord
    dataAoA.append([aoa, airSpeed, moment, cm(aoa)])

with open('AirSpeedOut.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(dataAirSpeed)
with open('AoAOut.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(dataAoA)
print("Completed")