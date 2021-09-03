import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","12345") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.first_name,"Muriuki")
        self.assertEqual(self.new_user.password,"12345")

    def test_save_user(self):

        '''
        save_user method saves contact objects into contact_list
        '''

        User.user_list.append(self)
        


if __name__ == '__main__':
    unittest.main()
