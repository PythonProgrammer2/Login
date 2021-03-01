fh = open('logininfo.txt', 'a') #userinformation will go to loginifo.txt
fh1 = open('logininfo.txt', 'r')
fh2 = open('logininfo.txt', 'r')
choice = input('login or register: ')
sets = fh2.readlines()
gs = 0

for set in sets:
  gs = gs + 1

class User:
  def __init__(self, password, username):
    self.password = password
    self.username = username

  def get_password(self):
    return self.password

  def get_username(self):
    return(self.username)

if choice == 'register':
  user = User(password = input('Please make a password: '),
  username = input('Please input a valid Username: '))
  password = (user.get_password())
  username = (user.get_username())
  register_info = (f'{password}, {username} \n')
  fh.write(register_info)
  print(f'Your verification is {gs}')
  print('Account made sucessfully!')
  fh.close()

elif choice == 'login':
  password1 = input('What was your password: ')
  username1 = input('What is your username: ')
  line = int(input('What was you verification number: '))
  login_info = (f'{password1}, {username1} \n')
  c = fh1.readlines()[line]
  if c == login_info:
    print('Sucessful')
  else:
    print('Account not found')

