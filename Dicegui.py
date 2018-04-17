from Dice import die, dieName, isIntList
from guizero import App, Text, PushButton
from time import localtime, strftime

#roll the dice in the hand.
def roll(hand,dice,results):
    #if there is a non zero amount of a die in hand, loop and roll them,
    #appending result to coresponding array in the total var
    total = []
    for x in range(len(dice)):
        total.append([])
        for y in range(hand[x]):
            total[-1].append(die(dice[x]))
    
    #dual purpose loop logs the rolled dice to the console, as well as totaling
    #them for display
    result = 0
    print(strftime('%Y-%m-%d %H:%M:%S',localtime()))
    for x in range(len(dice)):
        print(str(dieName(dice[x])).ljust(4) + ' | '  + str(total[x]))
        if not isIntList(total[x]):
            result = 'cannot sum named die and int die'
            break
        for y in range(len(total[x])):
                result += total[x][y]
    print()
    
    #write the final result to the gui
    results.value = result
    return


#Reset dice to roll to none
def emptyHand(dice,hand,inHand,results):
    for x in range(len(hand)):hand[x]=0 #must loop through and clear array as hand is an alias here
    inHand.value = ''                   #and attempts to replace with new array will simply remove link
    results.value = ''
    
#create and display a string detailing dice to be rolled
def diceToRoll(dice,hand,inHand):
    s=''
    for x in range(len(hand)):
        if (hand[x] != 0):
            s = s + str(hand[x]) + dieName(dice[x]) + ' + '
    s = s[:-3]
    inHand.value = s
    return s

#when button is pressed, increment dice in hand
def rollDie(dice,hand,d,inHand):
    hand[dice.index(d)] = hand[dice.index(d)] + 1
    diceToRoll(dice,hand,inHand)

#dice to use
dice=[4,6,8,('D01',[1,2,3,4,5,6,7,8,9,0]),('D10',[10,20,30,40,50,60,70,80,90,0]),12,20,1]

#Create a window
app = App(title='Dice Roller', layout='grid')

#define array to track count of dice in hand
hand=[0]*len(dice)

#displays for dice in hand and final roll
inHand = Text(app, grid=[3,0,5,2])
results= Text(app, grid=[3,2,5,2],size=20)

#create a button for each die
buttons=[]
buttonWidth = 10

for x in range(len(dice)):
    buttons.append(  PushButton(  app,
                                  text=dieName(dice[x]),
                                  grid=[0,x,3,1],
                                  command=rollDie,
                                  args=[dice,hand,dice[x],inHand]) )
    buttons[x].width=buttonWidth

#create special buttons (eg roll and reset)
buttons.append(PushButton(app,
                          text='ROLL',
                          grid=[0,len(dice)+1,3,1],
                          command=roll,
                          args=[hand,dice,results]))
buttons[-1].width = buttonWidth
buttons.append(PushButton(app,
                          text='reset',
                          grid=[0,len(dice)+2,3,1],
                          command=emptyHand,
                          args=[dice,hand,inHand,results]))
buttons[-1].width = buttonWidth
    
#Resize window to fit
app.height = (len(buttons)) * 40
app.width  = 600


#display window
app.display()



