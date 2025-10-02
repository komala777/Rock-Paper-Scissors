from tkinter import *
from random import randint
from tkinter import ttk

#main window
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry('500x450')
root.iconbitmap("C:\\Users\\komal\\Downloads\\game_icon.ico")
root.resizable(False, False)

#bgimage
bgimage = PhotoImage(file = "C:\\Users\\komal\\Downloads\\bg.png")
photolabel = Label(root, image= bgimage)
photolabel.place(relx= 0, rely = 0, relheight= 1, relwidth= 1)

#images for Rock, Paper, Scissors
Rock = PhotoImage(file = "C:\\Users\\komal\\Downloads\\rock.png")
Paper = PhotoImage(file = "C:\\Users\\komal\\Downloads\\paper.png")
Scissors = PhotoImage(file = "C:\\Users\\komal\\Downloads\\scissors.png")
photo_list = [Rock, Paper, Scissors]
pick_no = randint(0, 2)
label = Label(root, image= photo_list[pick_no], bd = 0)
label.pack(pady = 5)

#Main Function
def spin():
    pick_no = randint(0, 2)
    label.config(image = photo_list[pick_no])

    if user_choice.get() == 'Rock':
        user_choice_value = 0
    elif user_choice.get() == 'Paper':
        user_choice_value = 1
    else:
        user_choice_value = 2
    
    #WIN OR LOSE

    #Rock
    if user_choice_value == 0:
        if pick_no == 0:
            win_lose_label.config(text = 'It is a Tie! Spin again...')
        elif pick_no == 1:
            win_lose_label.config(text = 'Paper Cover Rock.. YOU LOSE!')
        else:
            win_lose_label.config(text = 'Rock smashes Scissors!.. YOU WIN!!!')

    #Paper
    if user_choice_value == 1:
        if pick_no == 0:
            win_lose_label.config(text = 'Paper cover Rock .. YOU WIN!!!')
        elif pick_no == 1:
            win_lose_label.config(text = 'It is a Tie! Spin again...')
        else:
            win_lose_label.config(text = 'Scissors cuts Paper .. YOU LOSE!')

    #Scissors
    if user_choice_value == 2:
        if pick_no == 0:
            win_lose_label.config(text = 'Rock smashes Scissors.. YOU LOSE!')
        elif pick_no == 1:
            win_lose_label.config(text = 'Scissors cuts Paper .. YOU WIN!!!')
        else:
            win_lose_label.config(text = 'It is a Tie! Spin again...')


#COMBOBOX
            
user_choice = ttk.Combobox(root,value = ('Rock','Paper','Scissors'))
user_choice.current(0)
user_choice.pack(pady = 5)

#SPINBUTTON
    
spin_button = Button(root,text = 'Spin!',bg = '#80aaff',fg = '#001133',padx = 10,command = spin) 
spin_button.pack()

#WIN/LOSE

win_lose_label = Label(root,text = '',font =('Helvetica',18))
win_lose_label.pack(pady = 50)

root.mainloop()
