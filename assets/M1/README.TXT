
Authentication and Authorisation system to protect against malicious individuals logging into the Queens Medical Centre. 

This is a representation of the Behavoural sequence diagram, submitted in Unit 9, for the Queens Medical Centre report detailing the initial security measures taken when a user logs into the system.  
The first part of the sequence diagram is to ensure only the correct authorised user can log into the system.
It is the first security checkpoint in the sequence diagram and shows a way of securing the edge of the platform by requiring a username and password to gain access to the system.
The script "Login_test.py" is run and by choosing the run ion at the top of the page.
It requires a username to be entered along with a password to gain entrance
This shows a user by the name of 'Craig' and a password of 'python' if both username and password are correct then the user can access the Queens Medical centre. If either the username or the password are incorrect the user will not be able to access the system and will receive an error message.
This is the first step on the Behavoural sequence diagram to enable authentiation of a user and then authorisation of access to the system 

"auth.py" is a file that will go into more depth with exception statements. These statements will enable the password to be encrypted.
It will also check to see if the username is already in use. It will also authorise and give permissions to users.

"testdata.py" is a file that will test the auth.py file

Code has been used for the auth.py and testdata.py from the book by Dusty Phillips referenced below:

Reference - Phillips, D. (2018) Python 3 Object-Oriented Programming: Build robust and maintainable software with object-oriented design patterns in Python 3.8. 3rd ed. Birmingham:Packt Publishing 





















References

Phillips, D. (2018) Python 3 Object-Oriented Programming: Build robust and maintainable software with object-oriented design patterns in Python 3.8. 3rd ed. Birmingham:Packt Publishing """

