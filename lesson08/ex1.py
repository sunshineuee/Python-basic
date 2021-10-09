
import re


re_username = re.compile(r'[a-zA-Z0-9._-]+(?=[@])')
re_domain = re.compile('(?<=@)+[a-zA-z]+\.+[a-zA-z0-9]+')

all_emails = {}


def email_parse(user_input):
    if re_domain.search(user_input) and re_username.search(user_input):
        domain = re_domain.search(user_input)
        username = re_username.search(user_input)
        if username.group(0) not in all_emails:
            all_emails[username.group(0)] = domain.group(0)
            print('Valid email')
        else:
            print('Email already exists')
    else:
        print('Invalid email')


while True:
    email = input('Enter email: ')
    email_parse(email)
    print(all_emails)