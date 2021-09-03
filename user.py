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
