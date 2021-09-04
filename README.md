# Application Name
 Password Locker
# Brief description of application
This is a password store application that is used to remember passwords.
## Date of current version
6/9/2021
## Contributors
By Enock Kipronoh
## Description
This is Password Locker application that one can use to store passwords for different accounts so one can be able to rememeber them.Here you create new account, login and then proceed to interact with the application which includes creating an account and paswword which you can generate or create your own. You can also search and delete your account.
## screenshots
<img src="images/Screenshot from 2021-09-04 23-14-19.png">
## Setup/Installation Requirements
* python3.8
* pyperclip
* pip
For one to be able to use this application, you are supposed to have installed python3.8 or 3.6. The Pyperclip and pip dependencies are also supposed to be insyalled in one's machine.

## Cloning
* Open Terminal {Ctrl+Alt+T}

* git clone ```  ```

* cd PassLock

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py
* To run test for the application
        $ python3.8 pass_test.py 

## Behavior Driven Development
  | Behavior          |           input             |                output                 |
 ___________________________________________________________________________________________
 | Open the application on the terminal | run the command ```./run.py```| Hello welcome to the apllication
 ____________________________________________________________________________________________
 | CA.. create an account   HA... have an account| CA.. input username and password | Hello {user_name}, your account has been created successfully|
 ____________________________________________________________________________________________
 | HA.. have an account  | enter your username and password | username <br> Password
 ____________________________________________________________________________________________
 |use these short codes: <br>``CC``: create new account <br>``DC``: Display credentials <br> ``FC``: find credentials <br>``GP``: Generate a random password<br>``D``:Delete credentials<br>``EX``: Exit the application| ``CC``: input account name, username and password<br> | Your credentials have been saved successfully!|
 ____________________________________________________________________________________________
 |``DC``: Display credentials| ``DC``                   | Saved credentials whenever they exist|
 ____________________________________________________________________________________________
 |``FC``: find credentials<br> enter the account name to search | account name                       | the account name, username and password|
 ____________________________________________________________________________________________
 |``GP``: Generate a random password| ``GP``                   | a random string of password|
 ____________________________________________________________________________________________
 | ``D``:Delete credentials<br>Enter the account name of the Credentials you want to delete   | The account name | Your stored credentials for : {search_credential.account} successfully deleted!!!|
 ____________________________________________________________________________________________
 | ``EX``: Exit the application | ``EX``                   | Thanks for using passwords store manager.. See you next time|
 ___________________________________________________________________________________________ 


## Known Bugs
No known bugs as of now, any bugs discovered, pull requests will be appreaciated
## Technologies Used
The technologies used include python3.8, figlet in python that was used to draw the pass drawing in the first section. 
Pyperclip is another technology used to facilitate copying and pasting.
## Support and contact details
For any questions or contributions, these are my email addresses:
* enckkipronoh@gmail.com<br>
* enock.kipronoh@student.moringaschool.com
## License
Link to the MIT license in my Github account

