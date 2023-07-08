hours=input("Enter Hours: ")
rate=input("Enter Per Hours rate: ")
hours=float(hours)
rate=float(rate)
pay= int(rate) * int(hours)
if(hours>=40):
    rate=rate*1.2
print(f"Total Pay: {round(hours*rate,3)}")