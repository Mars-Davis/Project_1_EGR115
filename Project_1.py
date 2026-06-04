# Project 1
print("this program is used to help analyze series and parallel resistor circuits by calculating equivalent resistance, current, and power consumption.")
voltage=float(input("enter voltage (V): "))
choice=int(input("For series enter 1, for parrallel enter 2: "))
resistors=int(input("enter number of resistors in circuit: "))
resistance_list=[]
sum=0
recipricol_sum=0
for n in range(resistors):
    if choice==1:
        resistance=float(input("enter resistance"))
        sum+=resistance
        resistance_list.append(resistance)
    else:
        resistance=float(input("enter resistance"))
        recipricol_sum+=1/resistance
        sum=1/recipricol_sum
        resistance_list.append(resistance)
print(f"equivalent resistance:{sum}")
current=voltage/sum
wires=(18,16,14,12,10,8,6,4,3,2,1,-1,-2,-3)
wire_ampacity = {
    18: 7,
    16: 10,
    14: 15,
    12: 20,
    10: 30,
    8: 40,
    6: 55,
    4: 70,
    3: 85,
    2: 95,
    1: 110,
    0: 125,
    -1: 145,   # 00 AWG
    -2: 165,   # 000 AWG
    -3: 195    # 0000 AWG
}
print("below are all suported Wire Gauges")
print(wires)
rating=int(input("select wire rating"))
max_amps=wire_ampacity[rating]
print("Voltage ", voltage)
print("Resistors:", resistance_list)
print("Equivalent resistance", sum, "Current ", current)
print
if current>max_amps:
    print("Unsafe, current is greater than what wire is rated for")
else:
    print("Safe")
