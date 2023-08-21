#if you decided to edit the code(for scalability or any other reason, remember DO NOT REMOVE the commets. It would be a real pain)


from random import randint
def Game():
    OperstionsList = ["+","-","*","+"] #the -1 element is placed + for easy playtime (if you want headaches you can switch to /)
    ProblemOperations = ['FirstOperator', 'SecondOperator', 'ThirdOperator', 'FourthOperator',] #functionality (record keeping)
    NumberList = ['fistNumber', 'SecondNumber', 'ThirdNumber', 'FourthNumber', 'FifthNumber'] #functionality (record keeping)
    global MathsProblem 
    MathsProblem =""
    result = 0
    #print("Calculation Order (Division > Multlipication > Addition > Subtraction)")
    for i in range(len(NumberList)):
        RandomNumber0_101 = randint(0, 101)
        MathsProblem = MathsProblem + str(RandomNumber0_101)
        NumberList[i] = RandomNumber0_101
        for j in range(1):
            Random_i = randint(0,3)
            RandomOperations = OperstionsList[Random_i]
            MathsProblem = MathsProblem + RandomOperations
            ProblemOperations[j] = RandomOperations
    MathsList = list(MathsProblem)
    #print(MathsList) #this list is ending with a random operator
    List2String = ''
    MathsList = List2String.join(MathsList)
    MathsList = MathsList[:-1] #list = list[:-1] it removes the last element from the list
    MathsProblem = MathsList
    print("\t",MathsProblem)
    print("--------------------------------")
    result = eval(MathsProblem)
    result = int(result)
    #print(result)
    def EnterInput():
        try:
            userInput = int(input("Enter the Final Result: "))
            
            if userInput == result:
                print("Yes, you are absolutely right! The result is {}\n".format(result))
                RestartGame()  # Call the restart function
            else:
                print("Oops! That's not correct. The correct answer is {}\n".format(result))
                RestartGame()  # Call the restart function
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            EnterInput()

    def RestartGame():
        restartCondition = input("Do you want to restart the game? (y/n): ")
        
        if restartCondition.lower() == 'y':
            Game()
        elif restartCondition == '':
            Game()
        else:
            print("Thanks for playing! <3")
    EnterInput() #its the first calling of the original Enterinput()
Game()
