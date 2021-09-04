#!/usr/bin/env python3.8

from user import User
def function():
	print("               ____                             ")
	print("              |  _ \                            ")
	print("              | |_) )  ____  ___   ___          ")
	print("              |  __/  / _  |/ __  / __          ")
	print("              | |    / (_| |\__ \ \__ \         ")
	print("              |_|    \_____| ___/  ___/         ")
function()

def create_user(user_name,first_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,first_name,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_by_password(password)

def check_existing_users(password):
    '''
    Function that check if a user exists with that password and return a Boolean
    '''
    return User.user_exist(password)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user, dc - display users, fc -find a users, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cc':
                print("New User")
                print("-"*10)

                print("User Name ...")
                user_name= input()

                print ("First name ....")
                first_name = input()

                print("Password ...")
                password = input()


                save_users(create_user(user_name,first_name,password)) # create and save new contact.
                print ('\n')
                print(f"New User {user_name} {first_name} {password} created")
                print ('\n')

        elif short_code == 'dc':

            if display_users():
                        print("Here is a list of all your Accounts")
                        print('\n')

                        for user in display_users():
                                print(f"{user.user_name} {user.first_name} .....{user.password}")

                        print('\n')
            else:
                        print('\n')
                        print("You dont seem to have any accounts saved yet")
                        print('\n')

        elif short_code == 'fc':

                print("Enter the password you want to search for")

                search_password = input()
                if check_existing_users(search_password):
                        search_user = find_user(search_password)
                        print(f"{search_user.first_name} {search_user.user_name}")
                        print('-' * 20)

                        print(f"Password.......{search_user.password}")
                        
                else:
                        print("That user does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()