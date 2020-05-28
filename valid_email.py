import re
pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
email = input('Enter Email to Check: ')
print('Your Email: ' + email)
print('\n')

mail = pattern.search(email)
print(mail)
