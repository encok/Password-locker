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

def del_user(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()