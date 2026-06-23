print("Welcome to quiz app")
score = 0


q1=input("Capital of India?:\n")
if q1.lower()=="delhi":
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")


q2=input("2""+""2?:\n")
if q2=='4':
    print("Correct answer")
    score+=1
else:
    print("wrong answer")

q3=input("National Animal of India?:\n")
if q3.lower()=="tiger":
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")


q4=input("Python is a ______?:\n")
if q4=="language":
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")


q5=input("Sun rises in the ______?:\n")
if q5=="east":
    score=score+1
    print("Correct answer")
else:
     print("Wrong answer")


print("Quiz Completed")
print("your score:",score,"/5")

if score==5:
  print("Excellent")
elif score==4:
 print("Very good")
elif score==3:
 print("Good")
else:
 print("Needs improvement")




         


 






