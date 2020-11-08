gryffindor, hufflepuff, ravenclaw, slytherin, answer1, answer2, answer3, answer4 = 0, 0, 0, 0, 0, 0, 0, 0

print ("=====================")
print ("The Sorting Hat Quiz!")
print ("=====================")

# ~~~~~~~~~~ Question 1 ~~~~~~~~~~

print ("Q1) When I'm dead, I want people to remember me as:")
print ("  1) The Good")
print ("  2) The Great")
print ("  3) The Wise")
print ("  4) The Bold")
answer1 = int(input("Enter your answer (1-4): "))

if answer1 == 1:
    hufflepuff += 1
elif answer1 == 2:
    slytherin += 1
elif answer1 == 3:
    ravenclaw += 1
elif answer1 == 4:
    gryffindor += 1
else:
	print ("Invalid input")

# ~~~~~~~~~~ Question 2 ~~~~~~~~~~

print ("Q2) Dawn or Dusk?")
print ("  1) Dawn")
print ("  2) Dusk")
answer2 = int(input("Enter your answer (1-2): "))

if answer2 == 1:
	gryffindor += 1
	ravenclaw += 1
elif answer2 == 2:
	hufflepuff += 1
	slytherin += 1
else:
	print ("Invalid input")

# ~~~~~~~~~~ Question 3 ~~~~~~~~~~

print ("Q3) Which kind of instrument most pleases your ear?")
print ("  1) The violin")
print ("  2) The trumpet")
print ("  3) The piano")
print ("  4) The drum")
answer3 = int(input("Enter your answer (1-4): "))

if answer3 == 1:
	slytherin += 1
elif answer3 == 2:
	hufflepuff += 1
elif answer3 == 3:
	ravenclaw += 1
elif answer3 == 4:
	gryffindor += 1
else:
	print ("Invalid input")

# ~~~~~~~~~~ Question 4 ~~~~~~~~~~

print ("Q4) Which road tempts you the most?")
print ("  1) The wide, sunny grassy lane")
print ("  2) The narrow, dark, lantern-lit alley")
print ("  3) The twisting, leaf-strewn path through woods")
print ("  4) The cobbled street lined (ancient buildings)")
answer4 = int(input("Enter your answer (1-4): "))

if answer4 == 1:
	hufflepuff += 1
elif answer4 == 2:
	slytherin += 1
elif answer4 == 3:
	gryffindor += 1
elif answer4 == 4:
    ravenclaw += 1
else:
	print ("Invalid input")

# ========== Sorting ==========

print ("Congrats on being sorted into... ")

max = 0
house = ""

if gryffindor > max:
	max = gryffindor
	house = "Gryffindor"
if hufflepuff > max:
	max = hufflepuff
	house = "Hufflepuff"
if ravenclaw > max:
	max = ravenclaw
	house = "Ravenclaw"
if slytherin > max:
	max = slytherin
	house = "Slytherin"

print(house + "!")

