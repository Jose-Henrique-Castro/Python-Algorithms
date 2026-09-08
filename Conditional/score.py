print("what is the score of the test ?\n") 
score = float(input(""))

if(score >= 90.0):{print("A\n")}
elif(score < 90.0 and score >= 80): print("B\n")
elif(score < 80.0 and score >= 70): print("C\n")
elif(score < 70.0 and score >= 60): print("D\n")
else : print("F")