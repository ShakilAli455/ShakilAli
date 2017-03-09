import random
import string


print("Welcome to the Speed Camera program")

#These are the variables
Distance = 500
SpeedLimit = 75

#This is Task 2 
letter1 = (random.choice(string.ascii_uppercase))#Generates five random letters from A to Z
letter2 = (random.choice(string.ascii_uppercase))
letter3 = (random.choice(string.ascii_uppercase))
letter4 = (random.choice(string.ascii_uppercase))        
letter5 = (random.choice(string.ascii_uppercase))
num1 = random.randint(0,9) #Generates two random numbers from 0 to 9
num2 = random.randint(0,9)

#Organizes the letters and numbers generated into a format of a number plate
NumberPlate = str(letter1) + str(letter2) + str(num1) + str(num2) + " " + str(letter3) + str(letter4) + str(letter5) 



#This is Task 1
FirstName = input("Enter your first name: ")
SecondName = input("Enter your second name: ")

#writing to a file.

#fw = open('list', 'a')#list is the file name and the w means you're writing to file
#fw.write("Name:" FirstName )

TimeOfEntry = float(input("Enter your Entry Time: "))
TimeOfExit = float(input("Enter your Leaving Time: "))
TotalTime = (TimeOfExit - TimeOfEntry)
AvgSpeed = (Distance/TotalTime)


if AvgSpeed <= SpeedLimit:
    print("You have exceeded the speed limit.")
    text_file = open("Information.txt", "a")
    text_file.write("First Name: " + (FirstName) + "\n")
    text_file.write("Second Name: " + (SecondName) + "\n")
    text_file.write("Entry Time: " + str (TimeOfEntry) + "\n")
    text_file.write("Leaving Time: " + str (TimeOfExit)+ "\n")
    text_file.write("Speed : " + str (AvgSpeed) + "mph" + "\n")
    text_file.write("License Plate: " + str(NumberPlate) + "\n")
    text_file.write("-----------------------------------------" )
    text_file.write("" )
    text_file.close()
elif AvgSpeed >= SpeedLimit:
    print("Adequate speed")



"""text_file = open("Information.txt", "w")
text_file.write("First Name: " + (FirstName) + "\n")
text_file.write("Second Name: " + (SecondName) + "\n")
text_file.write("Entry Time: " + str (TimeOfEntry) + "\n")
text_file.write("Leaving Time: " + str (TimeOfExit)+ "\n")
text_file.write("Speed : " + str (AvgSpeed) + "mph" + "\n")
text_file.write("License Plate" + str (NumberPlate) + "\n")

text_file.close()"""

text_file = open("Information.txt", "r")

text_file.close()

