import pyperclip
import random
import string

print("-"*100)

print("...............................PASSWORD LOCKER...............................")

class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty contact list

    def __init__(self,user_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_name : New contact user name.
            password: New contact password.
           
        '''
        
        self.user_name = user_name
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


class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []
    @classmethod
    def verify_user(cls,user_name, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.user_name == user_name and user.password == password):
                    a_user == user.user_name
        return a_user

    def __init__(self,account,user_name, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.user_name = user_name
        self.password = password
    
    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credentials_list