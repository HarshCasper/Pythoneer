import random
import pyperclip
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
password = ''
for c in range(6):
   password += random.choice(chars)
print('The Generated Password is %r and it has been copied to your clipboard' %(password))
pyperclip.copy(password)
