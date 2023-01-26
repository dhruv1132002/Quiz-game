print("welcome to the Quiz!")

ask = input("Do you wanna play the game? ")
if ask.lower() != "yes":
    quit() 
else:
    print("let's start the game!" )
correct=0
# Question 1
question = input("what is full form of CPU? ")
if question.lower() == "central processing unit":
    print("correct!")
    correct = correct + 1
else:
    print("Incorrect answer!")

# Question 2
question = input("what is full form of ROM? ")
if question.lower() == "read only memory":
    print("correct!")
    correct = correct + 1
else:
    print("Incorrect answer!")
# Question 3
question = input("what is full form of HTTP? ")
if question.lower() == "hypertext transmission protocol":
    print("correct!")
    correct = correct + 1
else:
    print("Incorrect answer!")
 # Question 4   
question = input("what is full form of RAM? ")
if question.lower() == "random access memory":
    print("correct!")
    correct = correct + 1
else:
    print("Incorrect answer!")

# Question 5
question = input("what is full form of HTMl? ")
if question.lower() == "hypertext markup language":
    print("correct!")
    correct = correct + 1
else:
    print("Incorrect answer!")

# result
print("your have scored " + str(correct) + " correct answers." )
print("your have scored " + str((correct / 5) * 100) + " correct answers." )
