#In this program will learn about the exception handling in case of incorrect type or incorrect input


def gross_pay(hours,rate):
    if((hours== int) or (rate==int)):
        hours=float(hours)
        rate=float(rate)
        # pay= int(rate) * int(hours)
        print(f"Total Pay: {round(hours*rate,3)}")
    else:    
        print("Exception Caused")
    
  

try:
    hours=input("Enter Hours: ")
except ValueError:
    print("Exception Occured")

try:
    rate=input("Enter Per Hours rate: ")
except ValueError:
    print("Exception Occured")

print(gross_pay(hours,rate))