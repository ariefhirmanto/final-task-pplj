# Client

import requests
import sys
import json
import variable as var
from random import randint

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
    
    # Post form to server
    requests.post(url, json = form)
    # print(form)

def Signin(_username, _password) :
    form = {
        "username" : _username,
        "password" : _password
    }
    status = 0

    url = var._signin_URL
    response = requests.post(url, json = form)
    if (response.status_code == 404): #User not found
        status = 1
    elif (response.status_code == 401) : #Wrong Password
        status = 2
    else :
        status = 0
        #saving var.token session    
        print("Posting to " + url)
        buffer = response.json()
        var.token = buffer['accessToken']
        var.username = buffer['username']
        var.name = buffer['name']
        var.amount_credit = buffer['amount_credit']
        print(var.token )
        # print(var.username)
        # print(buffer)
    return status

def CreateBill(_bill_name, _recipient, _amount, _description):
    bill_id = str(randint(0,1000))
    #finding recipient
     # Find recipient in database
<<<<<<< Updated upstream
    if(CheckRecipient(_recipient) == 1):
=======
    response = requests.get(var._user_URL, json = {'username':_recipient}, headers = {'X-Access-Token': var.token})
    if(response.status_code == 404):
>>>>>>> Stashed changes
        #User not found
        return 1
    
    form = {
        "bill_name"     : _bill_name,
        "bill_id"       : bill_id,
        "bill_sender"   : var.username,
        "bill_owner"    : _recipient,
        "amount"        : _amount,
        "description"   : _description 
    }
    form_2 = {
        "bill_id": bill_id,
        "bill_owner" : _recipient,
    }
    #Post to server
    response = requests.post(var._bill_URL, json=form, headers = {'X-Access-Token': var.token})
    print('Creating bill to ' + var._bill_URL)
    response = requests.put(var._user_URL+'/bill', json=form_2, headers = {'X-Access-Token': var.token})

def GetBill(_username, _bill_id) :
    if(_bill_id == ''):
        url = var._bill_URL + '/' + _username
    else :
        url = var._bill_URL +'/'+_bill_id
    
    response = requests.get(url, headers = {'X-Access-Token': var.token})
    
    var.bill_form = response.json()
    print(var.bill_form)
  
        
def UpdateBill(_bill_id) :
    url = _bill_URL +'/'+ _bill_id
    response = requests.put(url, headers = {'X-Access-Token': var.token})

def DeleteBill(_bill_id):
    url = _bill_URL +'/'+ _bill_id
    response = requests.delete(url, headers = {'X-Access-Token': var.token})

def GetCredit (credit_url, _username, token) :
    #Get Credit from server
    url = credit_url + _username
    response = requests.get(url, headers = {'X-Access-Token': token})

    credit = response.json()
    return(credit['amount_credit'])

def ChangeCredit(credit_url, _username,_amount_, _OTP, token):
    #Put new data to server
    url = credit_url
    response = requests.put(url, json = {'amount_credit' : _amount_, 'username':_username, 'otp' : _OTP}, headers = {'X-Access-Token': token})
    print(response.json())

    if(response.status_code==401){
        return 1
    }

def CheckRecipient(_recipient):
    #Check if recipient does exist
    # Find recipient in database
    response = requests.get(var._user_URL, json = {'username':_recipient}, headers = {'X-Access-Token': token})
    if(response.status_code == 404):
        #User not found
        print(_recipient+ ' Not Found')
        return 1
    else :
        return 0

def TransferMoney(_recipient, _amount_,_description, _OTP, token):
    credit_url = var._user_URL + '/transfer'

    #Change Recipient Credit
    success = ChangeCredit(credit_url, _recipient, (int(_amount_)),_OTP, token)
    #Change Sender Credit
    success = ChangeCredit(credit_url, var.username, (-1)*(int(_amount_)),_OTP, token)
    return success
    # print("Transfering Money Rp"+str(_amount_)+" to "+_recipient)

def RequestOTP():
    response = requests.get(var._otp_URL)
    print(response.json())

def UpdateInfo():
    url = var._user_URL
    message = {
        'username' : var.username
    }
    response = requests.get(url,json = message, var.token)

    user_form = response.json()
    #Update User Info
    var.amount_credit = user_form['amount']
    


def FillSignin() :
    print('Sign in')
    _username   = input('username: ')
    _password   = input('password: ')
