# localhost = 'http://localhost:'
# PORT = 8080
# _signup_URL = localhost+str(PORT)+'/api/auth/signup' 
# _signin_URL = localhost+str(PORT)+'/api/auth/signin'
# _bill_URL = localhost+str(PORT)+'/api/bill'
# _user_URL = localhost+str(PORT)+'/api/user'

import requests
import sys
import json
import variable as var

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

def SignUp(form) :
    url = var._signup_URL
    # Getting Header
    # response = requests.get(url)
    # headers = response.headers
    # print(headers)

    # Post form to server
    requests.post(url, json = form)
    print(form)

def Signin(_username, _password) :
    form = {
        "username" : _username,
        "password" : _password
    }
    status = 0

    url = var._signin_URL
    response = requests.post(url, json = form)
    if (response.status_code == 200):
        status = 0
    elif (response.status_code == 404): #User not found
        status = 1
    elif (response.status_code == 401) : #Wrong Password
        status = 2
    #saving var.token session    
    print("Posting to " + url)
    buffer = response.json()
    var.token = buffer['accessToken']
    print(form)
    print(var.token)
    return status

def CreateBill(bill_url, _bill_name, _recipient, _amount, _description):
    form = {
        "bill_name" : _bill_name,
        "bill_sender" : username,
        "bill_owner" : _recipient,
        "amount" : _amount,
        "description" : _description 
    }
    #Create JSON Object
    form_json = json.dumps(form)

    #Post to server
    response = requests.post(bill_url,json=form_json, headers = token)
    print('Creating bill to ' + bill_url)

def GetBill(_username, _bill_id, token) :
    if(_bill_id == ''):
        url = _bill_URL + '/' + _username
    else :
        url = _bill_URL +'/'+ _username +'/'+_bill_id
    
    response = requests.get(url, headers = token)
    
    #Return response as Json data
    bill_json = response.json().load()
    #Parsing bill_json and save it (not yet implemented)
    print("Requesting "+_username + " bill's to " + url)

def UpdateBill(_bill_id) :
    url = _bill_URL +'/'+ _bill_id
    response = requests.put(url, headers = var.token)

def DeleteBill(_bill_id):
    url = _bill_URL +'/'+ _bill_id
    response = requests.delete(url, headers = token)


def GetCredit (credit_url, _username, token) :
    #Get Credit from server
    url = credit_url + _username
    response = requests.get(url, headers = {'X-Access-Token': token})

    credit = response.json()
    return(credit['amount_credit'])

def ChangeCredit(credit_url, _username,_amount_, token):
    #Put new data to server
    url = credit_url
    response = requests.put(url, json = {'amount_credit' : _amount_, 'username':_username}, headers = {'X-Access-Token': token})

    print(response.json())

def TransferMoney(_recipient, _amount_, _description,token):
    credit_url = var._user_URL + '/transfer'
    
    #Change Recipient Credit
    ChangeCredit(credit_url, _recipient, (int(_amount_)), token)
    #Change Sender Credit
    ChangeCredit(credit_url, var.username, (-1)*(int(_amount_)), token)

    # print("Transfering Money Rp"+str(_amount_)+" to "+_recipient)

def FillSignin() :
    print('Sign in')
    _username   = input('username: ')
    _password   = input('password: ')
