#Mao
https://replit.com/join/htvpdvnoye-elianguerrero1
#Objective. Algorithm for obtaining zoo statistics.
#Create an algorithm to obtain statistics in a zoo where a count and percentage of “n” animals within a certain age range is required:
#Less than 2 years
#Between 2 and less than 5 years
#Between 5 and less than 10 years
#Greater than or equal to 10 years

#The diagram should ask as input: if there is another animal to be recorded (yes/no response), the age (years) of each one. Tip: use the lower function to validate yes and no
#The output must specify the number and percentage of animals in each age range.

print("Hi, today we are going to be doing statistics from animals, lets start.")
lessyears_2 = 0
B2or5 = 0
B5or10 = 0
G10 = 0
animals= 0
print("Is there an animal to be recorder? (yes or no)")
animal = input()

while animal == "yes":
  animals+=1
  age = int(input("How old are they?"))
  if age < 2:
    lessyears_2+= 1
  elif age >= 2 and age <= 5:
    B2or5 += 1
  elif age >= 5 and age <= 10:
    B5or10 += 1
  elif age > 10:
    G10+= 1
  print("Is there another animal to be recorded?")
  animal = input()
less= (lessyears_2*100)/animals
betweenless= (B2or5*100)/animals
betweenbig= (B5or10*100)/animals
greater10= (G10*100)/animals
print("Have less than 2 years:", lessyears_2, "and they are", less, "% of the animals")
print("Have between 2 and 5 years:", B2or5, "and they are", betweenless, "% of the animals")
print("Have between 5 and 10 years:", B5or10, "and they are", betweenbig, "% of the animals")
print("They are greater than 10 years:", G10, "and they are", greater10, "% of the animals")
