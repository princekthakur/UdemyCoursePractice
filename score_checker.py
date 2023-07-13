#score_tracker a udemy project 
#grade
# A-->8.5
# B-->7.5
# C-->6.5
# D-->5.5
# E-->4.5
# F-->3.3 
def score_tracker(score):
    score=float(score)
    
    if score>10.0:
        return("Invalid Score !!")
    if(score<=8.5 and score>=7.5):
        return("Grade A")
    if(score<=7.5 and score>=6.5):
        return("Grade B")
    if(score<=6.5 and score>=5.5):
        return("Grade C")
    if(score<=5.5 and score>=4.5):
        return("Grade D")
    if(score<=4.5 and score>=3.3):
        return("Grade E")
    if(score<3.3):
        return("Do Some more workhard!!")
    else:
        return("Bad Entry !!")



Name=input("Plese Enter Your Name: ")
score=input("Please Enter your Score: ")
result=score_tracker(score)

print("Here is Your Grade Or Remarks:" + result)
 

    