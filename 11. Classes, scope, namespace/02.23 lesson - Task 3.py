# TV controller
class TVController:

    commands = {0: 'All channels', 1: 'First channel', 2: 'last_channel',
                3: 'turn_channel_1', 4: 'next_channel', 5: 'previous_channel',
                6: 'current_channel', 7: 'is_exist_4', 8: 'is_exist_BBC'}
    print(commands)

    def __init__(self, first, second, last):
        self.all_channels = first + ' ' + second + ' ' + last
        self.first_channel = first
        self.last_channel = last
        self.turn_channel_1 = first
        self.next_channel = second
        self.previous_channel = first
        self.current_channel = first
        self.is_exist_4 = 'No'
        self.is_exist_BBC = 'Yes'

    def show_my_channel(self):
        user_command = str(input('Please enter command number: '))
        if user_command == '0':
            return self.all_channels
        elif user_command == '1':
            return self.first_channel
        elif user_command == '2':
            return self.last_channel
        elif user_command == '3':
            return self.turn_channel_1
        elif user_command == '4':
            return self.next_channel
        elif user_command == '5':
            return self.previous_channel
        elif user_command == '6':
            return self.current_channel
        elif user_command == '7':
            return self.is_exist_4
        elif user_command == '8':
            return self.is_exist_BBC
        else:
            return print('TV is off')

commands = TVController('BBC', 'Discovery', 'TV1000')

print(commands.show_my_channel())