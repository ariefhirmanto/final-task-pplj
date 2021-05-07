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
    var.token = buffer['accessvar.token']
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
    response = requests.post(bill_url,json=form_json, headers = var.token)
    print('Creating bill to ' + bill_url)

def GetBill(_username, _bill_id, var.token) :
    if(_bill_id == ''):
        url = _bill_URL + '/' + _username
    else :
        url = _bill_URL +'/'+ _username +'/'+_bill_id
    
    response = requests.get(url, headers = var.token)
    
    #Return response as Json data
    bill_json = response.json().load()
    #Parsing bill_json and save it (not yet implemented)
    print("Requesting "+_username + " bill's to " + url)

def UpdateBill(_bill_id) :
    url = _bill_URL +'/'+ _bill_id
    response = requests.put(url, headers = var.token)

def DeleteBill(_bill_id):
    url = _bill_URL +'/'+ _bill_id
    response = requests.delete(url, headers = var.token)


def GetCredit (credit_url, _username, var.token) :
    #Get Credit from server
    url = credit_url + _username
    response = requests.get(url, headers = var.token)

    credit = response.json()
    return(credit['amount_credit'])

def ChangeCredit(credit_url, _username,_amount_, var.token):
    #Put new data to server
    url = credit_url + _username
    response = requests.put(url, _amount_, headers = var.token)

def TransferMoney(_recipient, _amount_, _description,var.token):
    credit_url = _user_URL + '/'
    #Get recipient credit
    recipient_credit = GetCredit(credit_url, _recipient, var.token)
    #get sender credit
    sender_credit = GetCredit(credit_url, username, var.token)
    
    #adding recipient credit
    recipient_credit_buffer = recipient_credit + _amount_
    #reducing sender credit
    sender_credit_buffer = sender_credit - _amount_
    
    #Change Recipient Credit
    ChangeCredit(credit_url, _recipient, recipient_credit_buffer, var.token)
    #Change Sender Credit
    ChangeCredit(credit_url, username, sender_credit_buffer, var.token)

    print("Transfering Money Rp"+str(_amount_)+" to "+_recipient)

def FillSignin() :
    print('Sign in')
    _username   = input('username: ')
    _password   = input('password: ')
