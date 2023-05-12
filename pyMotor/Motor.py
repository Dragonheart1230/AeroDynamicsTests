"""EMRAX 228 : 4000rpm → 52kW cont → 96kW peak      (Not geared)
 
Below few datas about the propellers: This is for a pair of engines and contarotative propellers.
Speed is the air speed inside the upper propeller (data for a perpendicular air speed) . Datas are in Newton
 
 
SPEED 0
SPEED 90KM/H
RPM
NEWTON
NEWTON
3000
1229,869
665,3334
3125
1347,7037
884,4805
3250
1540,4862
1071,4806
3375
1899,3068
1409,294
3500
2032,6349
1516,1309
3625
2268,1848
1666,4109
3750
2425,9232
1824,8313
3875
2693,5474
2218,9722
4000
2869,465
2416,9524
 
4000 is the max rpm of the propellers"""

"""https://emrax.com/wp-content/uploads/2022/11/EMRAX_228_datasheet_A00.pdf"""
import csv
f = open("output.csv","w")
Voltage = 0
Kv = 10.12
Kt = 0.94
Resistance = 15.48
Current =0
Rpm= 0
Torque =0
data =[]

header =["Voltage", "Current", "RPM", "Torque"]

while(Rpm < 4000):
    Voltage += 1
    Rpm = Kv* Voltage
    Current = Voltage/Resistance
    Torque = Kt * Current
    data.append([Voltage, Current, Rpm,Torque])


with open('motorOut.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
print("Complete")
