print("Welcome to my computer quizz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()
else:
  print ("Okay! Lets play: ")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("correct")
  score += 1
else:
  print("WRONG")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("correct")
  score += 1
else:
  print("WRONG")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("correct")
  score += 1
else:
  print("WRONG")
  
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3) * 100) + "%.")
