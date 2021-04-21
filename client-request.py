import requests
import sys
import json

if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 8080

def Main() :
    localhost = '127.0.0.1'
    _signup = localhost+str(PORT)+'api/auth/signup'
    _signin = localhost+str(PORT)+'api/auth/signin'

    fill_signup = FillSignUp()
    print(fill_signup)


def FillSignUp():
    _username   = input('username: ')
    _password   = input('password: ')
    _name       = input('name: ')
    _email      = input('email: ')
    _role       = input('role (array): ')
    _amount     = input('amount credit: ')
    _bill_id    = input('bill id (array): ')
    _contact    = input('contact: ')

    form =  {"username" : _username,
            "email" : _email,
            "name" : _name,
            "password": _password,
            "roles" : _role,
            "amount_credit" : _amount,
            "bill_ID" : _bill_id,
            "contact" : _contact
            }

    # Serializing form
    form_json = json.dumps(form)
    return form_json

def SignUp(url, form) :
    # Getting Header
    response = requests.get(url)
    headers = response.headers
    print(headers)

    # Post form to server
    requests.post(url, json = form)

def FillSignin() :
    print('Sign in')
    _username   = input('username: ')
    _password   = input('password: ')
    
if __name__ == '__main__':
    Main()