import random
import tkinter as tk

root = tk.Tk()
root.title('Rock / paper / scissors game')
root.geometry('500x400+100+100')

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ''
COMP_CHOICE = ''

def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissors': 2}
    return rps[choice]


game_choice = ['rock', 'paper', 'scissors']
def random_computer_choice():
    return random.choice(game_choice)
    
def result(user_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(user_choice)
    comp = choice_to_number(comp_choice)
    if (user == comp):
        print('Tie')
    elif ((user - comp)%3 == 1):
        print('You win')
        USER_SCORE += 1
    else: 
        print('Computer win')
        COMP_SCORE += 1
    text_area = tk.Text(root, height = 10, width = 30, background = '#BFF3A5')
    text_area.grid(column = 0, row = 4)
    answer = "Your choice: {uc} \nComputer's Choice: {cc} \nYour Score: {u} \nComputer's Score: {c}".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)   
    text_area.insert(tk.END, answer)
    
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
    
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
    
def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissors'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

bt1 = tk.Button(text = '     ROCK     ', background = '#FF007F', command = rock)
bt1.grid(column=0, row=1)

bt2 = tk.Button(text = '     PAPER    ', background = '#FF00FF', command = paper)
bt2.grid(column=0, row=2)

bt3 = tk.Button(text = '   SCISSORS   ', background = '#7F00FF', command = scissors)
bt3.grid(column=0, row=3)    
    

root.mainloop()
