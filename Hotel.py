import error
import os
import time
rooms = {1: (101, 102, 103, 104, 105), 2: (
    201, 202, 203, 204, 205), 3: (301, 302, 303, 304, 305), 4: (401, 402, 403, 404, 405)}
guest_info = {}
room_info = {}

def action(text) -> None:
    print('\n' + text)
    time.sleep(3)
    os.system('cls')


###################################################
 
    
class Hotel:
    def __init__(self) -> None:
        self.room = rooms
        self.guest = guest_info
        self.room_info = room_info

    def register(self) -> None:
        while True:

            # choosing room type

            try:
                room_type = input("enter room type: ")
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                temp = Hotel()
                temp.register()

            # invalid room type

            if error.just_number(room_type) == False or error.length(room_type, 1) == False:
                action("invalid value")

            elif int(room_type) not in list(self.room.keys()):
                action("invalid room number")

        #######################################################

            # choosing room number

            try:
                room_number = input("enter room number: ")
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                temp = Hotel()
                temp.register()

            # invalid room number

            if error.just_number(room_number) == False or error.length(room_number, 3) == False:
                action("invalid value")

            elif int(room_number) not in self.room[int(room_type)]:
                action("wrong room number for room type")

            # room is already in use

            elif room_number in list(self.room_info.keys()):
                action("the room number is already in use")

            else:
                break

        #######################################################

        while True:

            # days

            flag = False
            try:
                days = input("how many days: ") + "day"
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                flag = True

            if not flag:

                # invalid number

                if error.str_int(days) == False:
                    action("invalid value")

                elif int(days[0]) <= 0:
                    action("value must be greater than zero")
                else:
                    break

        #######################################################

        while True:

            # nights

            try:
                nights = input("how many nights: ") + "night"
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                flag = True

            if not flag:

                # invalid number

                if error.str_int(nights) == False:
                    action("invalid value")

                elif int(nights[0]) <= 0:
                    action("value must be greater than zero")

                else:
                    break

            else:
                break

        #######################################################

        i = 0
        temp_dic = []                    # for adding more than one id number to a room number key
        while i < int(room_type):    # user enters requested data

            while True:
                
                # entering first name

                flag = False

                try:
                    f_name = input("enter first name: ")        # f_name = first name
                except KeyboardInterrupt or EOFError:
                    action("enter a valid value")
                    flag = True

                if not flag:

                    # invalid character for first name

                    if error.just_str(f_name) == False:
                        action("invalid chracter for first name section")

                    else:
                        break

            #######################################################

            while True:

                # entering last name

                flag = False
                try:
                    l_name = input("enter last name: ")     # l_name = last name
                except KeyboardInterrupt or EOFError:
                    action("invalid value")
                    flag = True

                if not flag:

                    # invalid character for last name

                    if error.just_str(l_name) == False:
                        action("invalid character for last name section")

                    else:
                        break

            #######################################################

            while True:
                flag = False

                # entering age

                try:
                    age = input("enter age: ")
                except KeyboardInterrupt or EOFError:
                    action("invalid value entered")
                    flag = True

                if not flag:

                    # invalid chracter in age

                    if error.just_number(age) == False:
                        action("Numbers Only")
                    
                    else:
                        break

            #######################################################

            while True:

                # entering id

                flag = False

                try:
                    id = input("enter id number: ")
                except KeyboardInterrupt or EOFError:
                    action("invalid value")
                    flag = True

                if not flag:

                    # invalid character in id

                    if error.just_number(id) == False:
                        action("Numbers Only")

                    elif error.length(id, 9) == False:
                        action("ID must be exactly nine digits long")

                    else:
                        break

            self.guest[id] = f_name, l_name, age
            temp_dic.append(id)
            i += 1

        self.room_info[room_number] = temp_dic, days + ' & ' + nights

        print('\n\n')
        print("guest registered successfully")      # successful
        time.sleep(5)
        os.system('cls')


    #######################################################


    def info_room(self) -> None:

        while True:

            # choosing room type

            try:
                room_type = input("enter room type: ")

            except KeyboardInterrupt and EOFError:
                action("enter a valid value")
                temp = Hotel()
                temp.register()

            if error.just_number(room_type) == False or error.length(room_type, 1) == False:
                action("invalid value")

            # invalid room type

            elif int(room_type) not in list(self.room.keys()):
                action("invalid room number")

            else:
                break

        #######################################################

        while True:

            # choosing room number

            try:
                room_number = input("enter room number: ")
            except KeyboardInterrupt:
                action("enter a valid value")
                temp = Hotel()
                temp.register()

            # invalid room number

            if error.just_number(room_number) == False or error.length(room_number, 3) == False:
                action("invalid character in room number")

            elif int(room_number) not in self.room[int(room_type)]:
                action("wrong room number for room type")

            else:
                break

        try:
            print(self.room_info[room_number], '\n\n\n')
        except KeyError:
            print('\n\n')
            print("no information available about this room")
            time.sleep(3)
            return


    #######################################################


    def info_guest(self) -> None:

        while True:

            flag = False
            # entering id number

            try:
                id = input("enter id number: ")
            except KeyboardInterrupt or EOFError:
                action("invalid value")
                flag = True

            if not flag:

                # invalid id

                if error.just_number(id) == False:
                    action("Numbers Only")
                
                elif error.length(id, 9) == False:
                    action('ID Number must be of 8 digits')

                elif id not in self.guest.keys():
                    action("no id number found")
                    break

                else:
                    print(self.guest[id])
                    break
    

    ######################################################


    def delete_room(self) -> None:      # deleting room from room info

        while True:
            
            flag = False

            # entering room number

            try:
                room_number = input("enter room number: ")
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                flag = True

            if not flag:
                # invalid room number

                if error.just_number(room_number) == False or error.length(room_number, 3) == False:
                    action("invalid value")

                elif room_number not in self.room_info.keys():
                    action("no such Room Found")

                else:
                    self.room_info.pop(room_number, "no such room is in use")
                    action("room info successfully deleted")        # success
                    break
    

    ######################################################


    def delete_guest(self) -> None:     # deletes guest info

        while True:

            flag = False

            # entering id number

            try:
                id = input("enter id number: ")
            except KeyboardInterrupt or EOFError:
                action("invalid value")
                flag = True

            if not flag:
                
                # invalid id number

                if error.just_number(id) == False:
                    action("Numbers Only")

                elif error.length(id, 9) == False:
                    action("ID must be exactly nine digits long")

                elif id not in self.guest.keys():
                    action("No Such Guest Exists")

                else:
                    self.guest.pop(id)
                    action("guest info deleted successfully")        # success
                    break


    #################################################


        
    def change_id(self) -> None:
        while True:
                
            flag = False

            try:
                f_name = input("enter first name: ")        # f_name = first name
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                flag = True

            if not flag:

                # invalid character for first name

                if error.just_str(f_name) == False:
                    action("invalid chracter for first name section")

                else:
                    break

        #######################################################

        while True:

            # entering last name

            flag = False
            try:
                l_name = input("enter last name: ")     # l_name = last name
            except KeyboardInterrupt or EOFError:
                action("invalid value")
                flag = True

            if not flag:

                # invalid character for last name

                if error.just_str(l_name) == False:
                    action("invalid character for last name section")

                else:
                    break

        #######################################################

        while True:
            flag = False

            # entering age

            try:
                age = input("enter age: ")
            except KeyboardInterrupt or EOFError:
                action("invalid value entered")
                flag = True

            if not flag:

                # invalid chracter in age

                if error.just_number(age) == False:
                    action("Numbers Only")
                    
                else:
                    break

        #######################################################

        temp = list(self.guest.items())
        for i in range(0, len(temp)):

            flag = False

            if temp[i][1] == f_name and temp[i][2] == l_name and temp[i][3] == age:
                    
                key = temp[i][0]

                try:
                    id = input("enter id number: ")
                except KeyboardInterrupt or EOFError:
                    action("invalid value")
                    flag = True

            if not flag:
                
                # invalid id number

                if error.just_number(id) == False:
                    action("Numbers Only")

                elif error.length(id, 9) == False:
                    action("ID must be exactly nine digits long")

                else:
                    self.guest.pop(key)
                    self.guest[id] = f_name, l_name, age
                    action("guest id changed successfully")        # success
                    return
                    
        print("no such gues exist")


    #######################################################


    def change_other(self) -> None:
            
        while True:
                
            # entering first name

            flag = False

            try:
                f_name = input("enter first name: ")        # f_name = first name
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                flag = True

            if not flag:

                # invalid character for first name

                if error.just_str(f_name) == False:
                    action("invalid chracter for first name section")

                else:
                    break

        #######################################################

        while True:

            # entering last name

            flag = False
            try:
                l_name = input("enter last name: ")     # l_name = last name
            except KeyboardInterrupt or EOFError:
                action("invalid value")
                flag = True

            if not flag:

                # invalid character for last name

                if error.just_str(l_name) == False:
                    action("invalid character for last name section")

                else:
                    break

        #######################################################

        while True:
            flag = False

            # entering age

            try:
                age = input("enter age: ")
            except KeyboardInterrupt or EOFError:
                action("invalid value entered")
                flag = True

            if not flag:

                # invalid chracter in age

                if error.just_number(age) == False:
                    action("Numbers Only")
                    
                else:
                    break

        #######################################################

        while True:

            # entering id

            flag = False

            try:
                id = input("enter id number: ")
            except KeyboardInterrupt or EOFError:
                action("invalid value")
                flag = True

            if not flag:

                # invalid character in id

                if error.just_number(id) == False:
                    action("Numbers Only")

                elif error.length(id, 9) == False:
                    action("ID must be exactly nine digits long")

                else:
                    break

        self.guest.update({id: (f_name, l_name, age)})
        action("guest info updated successfully")       # success          

                
#######################################################
            

while True:
    while True:
        print("enter a number from menu below")
        print("1 - register a guest \t\t 2 - room info \t\t 3 - guest info")
        print("4 - delete room from room info \t 5 - delete guest info \t 6 - update guest info")
        x = input()

        if error.just_number(x) == False:
            action("enter a valid value")
            break

        elif error.length(x, 1) == False:
            action("enter a valid value")
            break

        temp = Hotel()
        if int(x) == 1:
            os.system('cls')
            temp.register()

        if int(x) == 2:
            os.system('cls')
            temp.info_room()
        
        if int(x) == 3:
            os.system('cls')
            temp.info_guest()
        
        if int(x) == 4:
            os.system('cls')
            temp.delete_room()
        
        if int(x) == 5:
            os.system('cls')
            temp.delete_guest()

        if int(x) == 6:
            os.system('cls')
            try:
                y = input("if you want to change id number enter \'i\' or else enter \'o\' \n")
            except KeyboardInterrupt or EOFError:
                action("enter a valid value")
                break

            if y == 'i':
                os.system('cls')
                temp.change_id()

            elif y == 'o':
                os.system('cls')
                temp.change_other()
            
            else:
                action("wrong letter")
                break 