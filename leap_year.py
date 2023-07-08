#leap Year Code 
#leap years 2000,2048,1996,1992

def leap_year(year):
    year=int(year)
    if ((year%400==0) or (year%100!=0) and (year%4==0)):
        print("Leap Year")
    else:
        print("its not leap year")


year1=input("Enter a year to check if its a leap year:")
leap_year(year1)