import pyperclip

print("...........................Password Locker...........................")

class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty contact list

    def __init__(self,user_name,first_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New contact first name.
            last_name : New contact last name.
            number: New contact phone number.
            email : New contact email address.
        '''
        
        self.user_name = user_name
        self.first_name = first_name
        self.password = password
    def save_user(self):

        '''
        save_user method saves contact objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: password to search for
        Returns :
            User of person that matches the password.
        '''

        for user in cls.user_list:
            if user.password == password:
                return user

    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.password == password:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    

    @classmethod
    def copy_user_name(cls,password):
        user_found = User.find_by_password(password)
        pyperclip.copy(user_found.user_name)
