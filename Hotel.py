import error
import os
import time
rooms = {1: (101, 102, 103, 104, 105), 2: (
    201, 202, 203, 204, 205), 3: (301, 302, 303, 304, 305), 4: (401, 402, 403, 404, 405)}
guest_info = {}
room_info = {}

class Hotel:
    def __init__(self) -> None:
        self.room = rooms
        self.guest = guest_info
        self.room_info = room_info


    def personal_info() -> str:
        
        while True:
                
            # entering first name

            f_name = ''     # f_name = first name
            flag, f_name = error.try_except(f_name, "first name: ")

            if flag:
                error.action("enter a valid value")

            else:
                # invalid character for first name

                if error.just_str(f_name) == False:
                    error.action("invalid chracter for first name section")

                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # entering last name

            l_name = ''         # l_name = last name
            flag, l_name = error.try_except(l_name, "last name: ")

            if flag:
                error.action("enter a valid value")

            else:

                # invalid character for last name

                if error.just_str(l_name) == False:
                        error.action("invalid character for last name section")

                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # entering age

            age = ''
            flag, age = error.try_except(age, "enter age: ")

            if flag:
                error.action("enter a valid value")

            else:

                # invalid chracter in age

                if error.just_number(age) == False:
                    error.action("only number is allowed")
                        
                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # entering id

            id = ''
            flag, id = error.try_except(id, "enter id number: ")

            if flag:
                error.action("enter a valid value")

            else:

                # invalid character in id

                if error.just_number(id) == False:
                    error.action("only number is allowed")

                elif error.length(id, 9) == False:
                    error.action("ID must be exactly nine digits long")

                else:
                    break
        
        return f_name, l_name, age, id


    ########################################################

            
    def register(self) -> None:
        while True:

            # choosing room type

            room_type = ''
            flag, room_type = error.try_except(room_type, "enter room type: ")

            if flag:
                error.action("enter a valid value")

            # invalid room type

            else:
                if error.just_number(room_type) == False:
                    error.action("only number is allowed")

                elif error.length(room_type, 1) == False:
                    error.action("only one digit number is allowed")

                elif int(room_type) not in list(self.room.keys()):
                    error.action("invalid room type")
            
                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # choosing room number

            room_number = ''
            flag, room_number = error.try_except(room_number, "enter room number: ")

            if flag:
                error.action("enter a valid value")

            else:
                # invalid room number

                if error.just_number(room_number) == False:
                    error.action("only number is allowed")

                elif error.length(room_number, 3) == False:
                    error.action("only a 3 digit number is allowed")

                elif int(room_number) not in self.room[int(room_type)]:
                    error.action("wrong room number for room type")

                # room is already in use

                elif room_number in list(self.room_info.keys()):
                    error.action("the room number is already in use")

                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # days

            days = ''
            flag, days = error.try_except(days, "how many days: ")

            if flag:
                error.action("enter a valid value")
            days = days + "days"

            if not flag:

                # invalid number

                if error.str_int(days) == False:
                    error.action("only number is allowed")

                elif int(days[0]) <= 0:
                    error.action("value must be greater than zero")
                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # nights

            nights = ''
            flag, nights = error.try_except(nights, "how many nights: ")

            if flag:
                error.action("enter a valid value")
            nights = nights + "nights"

            if not flag:
                # invalid number

                if error.str_int(nights) == False:
                    error.action("only number is allowed")

                elif int(nights[0]) <= 0:
                    error.action("value must be greater than zero")

                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        i = 0
        temp_dic = []                    # for adding more than one id number to a room number key
        while i < int(room_type):    # user enters requested data
            
            f_name, l_name, age, id = Hotel.personal_info()

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

            room_type = ''
            flag, room_type = error.try_except(room_type, "enter room type: ")

            if flag:
                error.action("enter a valid value")

            else:

                if error.just_number(room_type) == False:
                    error.action("only number is allowed")

                elif error.length(room_type, 1) == False:
                    error.action("only one digit number is allowed")

                # invalid room type

                elif int(room_type) not in list(self.room.keys()):
                    error.action("invalid room number")

                else:
                    break

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        while True:

            # choosing room number

            room_number = ''
            flag, room_number = error.try_except(room_number, "enter room number: ")

            if flag:
                error.action("enter a valid value")

            else:

                # invalid room number

                if error.just_number(room_number) == False:
                    error.action("invalid character in room number")

                elif error.length(room_number, 3) == False:
                    error.action("only 3 digit number is allowed")

                elif int(room_number) not in self.room[int(room_type)]:
                    error.action("wrong room number for room type")

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

            # entering id number

            id = ''
            flag, id = error.try_except(id, "enter id number: ")

            if flag:
                error.action("enter a valid value")

            else:

                # invalid id

                if error.just_number(id) == False:
                    error.action("only number is allowed")
                    
                elif error.length(id, 9) == False:
                    error.action('ID Number must be of 8 digits')

                elif id not in self.guest.keys():
                    error.action("no id number found")
                    break

                else:
                    print(self.guest[id])
                    break
        

    ######################################################


    def delete_room(self) -> None:      # deleting room from room info

        while True:

            # entering room number

            room_number = ''
            flag, room_number = error.try_except(room_number, "enter room number: ")

            if flag:
                error.action("enter a valid value")

            else:

                # invalid room number

                if error.just_number(room_number) == False:
                    error.action("only number is allowed")

                elif error.length(room_number, 3) == False:
                    error.action("only 3 digit number is allowed")

                elif room_number not in self.room_info.keys():
                    error.action("no such Room Found")

                else:
                    self.room_info.pop(room_number, "no such room is in use")
                    error.action("room info successfully deleted")        # success
                    break
    

    ######################################################


    def delete_guest(self) -> None:     # deletes guest info

        while True:

            # entering id number

            id = ''
            flag, id = error.try_except(id, "enter id number: ")

            if flag:
                error.action("enter a valid value")

            else:

                # invalid id number

                if error.just_number(id) == False:
                    error.action("only number is allowed")

                elif error.length(id, 9) == False:
                    error.action("ID must be exactly nine digits long")

                elif id not in self.guest.keys():
                    error.action("No Such Guest Exists")

                else:
                    self.guest.pop(id)
                    error.action("guest info deleted successfully")        # success
                    break


    #################################################


        
    def change_id(self) -> None:      

        # getting info

        f_name, l_name, age, id = Hotel.personal_info()

        # finding the id of guest
        
        temp = list(self.guest.items())
        for i in range(0, len(temp)):

            if temp[i][1] == f_name and temp[i][2] == l_name and temp[i][3] == age:
                    
                key = temp[i][0]

                self.guest.pop(key)
                self.guest[id] = f_name, l_name, age
                print("guest id changed successfully")        # success
                return
                    
        print("no such gues exist")


    #######################################################


    def change_other(self) -> None:     # changing first name, last name, age
        
        # getting info
        
        f_name, l_name, age, id = Hotel.personal_info()

        self.guest.update({id: (f_name, l_name, age)})
        print("guest info updated successfully")       # success          

                
#######################################################
            

while True:
    while True:
        print("enter a number from menu below")
        print("1 - register a guest \t\t 2 - room info \t\t 3 - guest info")
        print("4 - delete room from room info \t 5 - delete guest info \t 6 - update guest info")
        x = input()

        if error.just_number(x) == False:
            error.action("enter a valid value")
            break

        elif error.length(x, 1) == False:
            error.action("enter a valid value")
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
            y = ''
            flag, y = error.try_except(y, "if you want to change id number enter \'i\' or else enter \'o\' \n")

            if flag:
                error.action("enter a valid value")
                break

            if y == 'i':
                os.system('cls')
                temp.change_id()

            elif y == 'o':
                os.system('cls')
                temp.change_other()
            
            else:
                print("wrong letter")
                break 