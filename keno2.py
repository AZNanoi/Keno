from random import randint
import random
#menyn har problem att lämna loopen.
#från att jag la till meny så ligger inte allt i den exakt rätta loopen
#vilket gör en del kod inte körs
def print_menu():
    print ("*******************************")
    print ("Välkommen till Bingo!")
    print ("*******************************")
    print ("Välj ett utav alternativen")
    print ("1. Spela bingo!")
    print ("2. Statistik")
    print ("3. Avsluta")

#skriva ut statistik
def print_statistik():
    print ("*************************")
    print ("statistik!")
    print ("*************************")
    for position, point in enumerate(statistik):
        print("Spel", position+1, ":", point, "poäng")

#skapa dragnings nummer och sparar dem i listan "drawingNumbers"
def generate_drawingNumbers():
    print ("Dragning")
    print ("****************************************")
    del drawingNumbers[:]
    while(len(drawingNumbers) < 10):
        iNewNumber = randint(1,25)
        if(iNewNumber not in drawingNumbers):
            drawingNumbers.append(iNewNumber)

#Skriva ut spelplan
def printOut_playBoard():
    count = 0
    output = ""
    for num in range(1,26):
        count += 1
        if num in drawingNumbers:
            output = output + "    " + "[" + str(num)+ "]"
        else:
            output = output + "    " + str(num)

        if(count == 5): #Skriva ut varje femte tal, och återställer count och output for en ny rad
            print(output)
            print("---------------------------------------------")
            count = 0
            output = ""

#Beräkna vinnar poäng
def calculate_point(IMyNumbers):
    pointCounter = 0
    for num in IMyNumbers:
        if num in drawingNumbers:
            pointCounter += 1
    return pointCounter

#Starta spelet
def initiateGame():
    inputNotSuccess = True
    print ("****************************************")
    inputMessage = "Ange fem siffror [1-25] (avgränsa med ','): "
    while(inputNotSuccess):
        try:
            inputs = input(inputMessage)
            IMyNumbers = [int(x) for x in inputs.split(",")] #splittra inmatningen i en lista och konvertera varje tal till int typ.
            if(len(IMyNumbers) == 5):
                correctNumbers = True
                seen = set()
                for n in IMyNumbers:
                    if( n > 25 or n <= 0 ):
                        correctNumbers = False
                        inputMessage = "Incorrect numbers in input! Please try again! Enter five number [1-50] (separated with ','):"
                        break
                    elif n in seen: #kolla om det aktuella numret finns i listan
                        correctNumbers = False
                        inputMessage = "Duplicate numbers in input! Please try again! Enter five number [1-50] (separated with ','):"
                        break
                    seen.add(n) #lägga in aktuell nummer i listan
            
                if(correctNumbers):
                    inputNotSuccess = False; #avbryta while loop
            else:
                inputMessage = "Invalid input! Please try again! Enter five number [1-50] (separated with ','):"
        except ValueError:
            print ("Oops! There were no valid number in input.  Try again...")

    generate_drawingNumbers()
    printOut_playBoard()
    point = calculate_point(IMyNumbers)
    print ("du fick " +str(point) + " poäng")
    statistik.append(point)

statistik=[]
drawingNumbers = []
iNewNumber = 0
#loopar meny tills den blir False
loop=True
while loop:
    #visar menyn
    print_menu()
    
    #programmet skriver ut för användaren.
    #la till det som en extra funtion då det ser snyggare ut!
    print ("*******************")
    try:
        choice = int(input("Välj mellan [1-3]: "))
    
        #Användarens val visas på skärmen
        print (u'Ditt val: %s'  %(choice))
           
        if(choice>=1 and choice<=3):
            if choice==1:
                initiateGame()
            elif choice==2:
                print_statistik()
            elif choice==3:
                print ("Hejdå!")
                exit()
        else:
            input("Fel val. Tryck på enter för att försöka igen!")
    except ValueError:
        print ("Oops! That was no valid number.  Try again...")
