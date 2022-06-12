import tkinter as tk
from tkinter import ttk 



class TVController():
    def __init__(self, channel):
        self.chan = channel
        self.N = 0 # позиция соответствует позиции во внутреннем списке
        
    
    def first_channel(self):
        self.N = 0
        self.print_message()       #show up on the screen 
        return self.chan[self.N]

    def chan_number(self, n):
        if n != 0 and n <= len(self.chan):
            self.N = n - 1
            self.print_message()
        else: 
            print(f'the channel: {n}. No signal')

    def last_channel(self):
        self.N = len(self.chan) - 1
        self.print_message()
        return self.chan[self.N]
        
    def turn_channel(self):
        new_channel = int(input('Enter channel number: '))
        if 0 < new_channel <= len(self.chan)+1:
            self.N = new_channel - 1
            self.print_message()
        else: 
            print(f'The channel: {new_channel - 1}. No signal')
        return self.chan[self.N]

    def next_channel(self):
        if self.N == len(self.chan) - 1:
            self.N = 0
        else:
            self.N += 1
        self.print_message()
        return self.chan[self.N]

    def previous_channel(self):
        if self.N == 0:
            self.N = len(self.chan) - 1        
        else:
            self.N -= 1
        self.print_message()
        return self.chan[self.N]

    def current_channel(self): 
        self.print_message()      
        return self.chan[self.N]

    def is_exist(self, ex):
        if type(ex) == str:
            if ex in self.chan:
                return 'Yes'
            else:
                return 'No'
        elif type(ex) == int:
            if 0 < ex <= len(self.chan):
                return 'Yes'
            else:
                return 'No'
        else:
            raise ValueError('Не тот тип ввода!')
        
        return self.chan[self.N]
    
    def print_message(self):
        print(f'The channel: {self.N+1}. {self.chan[self.N]}')
    
    def print_menu(self):
        print(f'1: {self.chan[self.N]}, 2: {self.chan[self.N+1]}, 3: {self.chan[self.N+2]}')
        
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

'''
assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel() == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
'''
