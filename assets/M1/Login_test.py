"""to create a login script to allow a user to login with a password and deny access if the password is incorrect"""
print ('Please enter your username')
username = input()
if username == 'Craig':
   print('Welcome to Queens Medical Centre ' + username + ' please enter your password')
   password =  input ()
   if password == 'python':
      print ('Access Granted have a nice day')
   else:
      print ('I am sorry that is the incorrect Password')
      print('At this time access is denied')
else:
      print('I am sorry I do not have a record of that username!')
      print('At this time access is denied')
      