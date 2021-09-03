print("...........................Password Locker...........................")
class User:
    """
    Class that generates new instances of contacts
    """

    user_list = []
    
    def__init__(self, username, first_name, password):
        """
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user usernaname.
            first_name : New user first name.
            password: New user password.
            
        """
        self.username = username
        self.first_name = first_name
        self.password = password
