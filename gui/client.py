# Client

import requests
import sys
import json
import variable as var
from random import randint

# Sign Up API
# This api will post user registration to server and the server will save user registration in database
# Param :
# - Form : signup form in json format. 
def SignUp(form) :
    url = var._signup_URL
    
    # Post form to server
    requests.post(url, json = form)
    # print(form)

# Sign In API
# Param : 
# - _username : username of user account
# - _password : _password of user account
# return :
# - status : -> 0 : if user and password match
#            -> 1 : if user is not found in server database
#            -> 2 : if user is found but password doesn't match
 
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
        print(buffer)
    return status

# Create Bill API
# This API will create a bill form and post it to server
# Param :
# - _bill_name      : name of the bill
# - _recipient      : username of recipient's account
# - _description    : description of the bill
# - _OTP            : OTP
# Return :
# Success -> 1 : Bill creation failed due to wrong OTP
#         -> 0 : Bill creation is success
#   
def CreateBill(_bill_name, _recipient, _amount, _description,  _OTP):
    bill_id = str(randint(0,1000))
    form = {
        "bill_name"     : _bill_name,
        "bill_id"       : bill_id,
        "bill_sender"   : var.username,
        "bill_owner"    : _recipient,
        "amount"        : _amount,
        "description"   : _description, 
        "otp"           : _OTP
    }
    form_2 = {
        "bill_id": bill_id,
        "username" : _recipient,
        "otp"           : _OTP
    }
    #Post to server
    response = requests.post(var._bill_URL, json=form, headers = {'X-Access-Token': var.token})
    print('Creating bill to ' + var._bill_URL)
    response = requests.put(var._user_URL+'/bill', json=form_2, headers = {'X-Access-Token': var.token})

    if (response.status_code == 401): #wrong otp
        success = 1
    else:
        success = 0

    return success

# Get Bill API
# This API will perform request to get all of user's bill from server
# Param :
# - _username   : username of user's account
# - _bill_id    : unique code of bill

def GetBill(_username, _bill_id) :
    if(_bill_id == ''):
        url = var._bill_URL + '/' + _username
    else :
        url = var._bill_URL +'/'+_bill_id
    
    response = requests.get(url, headers = {'X-Access-Token': var.token})
    
    var.bill_form = response.json()
    print(var.bill_form)
  
# Find Bill API
# This fucntion is used to find user's bill by matching the bill id
# Param :
# - _bill_id : bill id of bill
# return :
# - found : True    -> bill id is found in user's bill collection
#           False   -> bill id is not found in user's bill collection
# - i     : array index of user's bill collection  
def FindBill(_bill_id):
    found = False
    for i in range(0,len(var.bill_form)):
        if (var.bill_form[i]['bill_id'] == _bill_id) :
            found = True
            break
    
    return (found,i)

# Update Bill API
# Currently not used
def UpdateBill(_bill_id) :
    url = _bill_URL +'/'+ _bill_id
    response = requests.put(url, headers = {'X-Access-Token': var.token})

# Delete Bill API
# This API performs request to delete user's bill in server database
# Param :
# - _bill_id    : unique code of bill that is going to be deleted
# - _OTP        : OTP

def DeleteBill(_bill_id, _OTP):
    url = var._bill_URL +'/'+ _bill_id
    response = requests.delete(url, json={"otp":_OTP}, headers = {'X-Access-Token': var.token})


# Get Credit API
# This API performs request to get the credit of an account from server database
# Param :
# - credit_url  : URL of Backend API
# - _username   : username of account whose credit is going to be gotten
# - token       : token of session
# Return :
# - Account's credit or balance 

def GetCredit (credit_url, _username, token) :
    #Get Credit from server
    url = credit_url + _username
    response = requests.get(url, headers = {'X-Access-Token': token})

    credit = response.json()
    return(credit['amount_credit'])

# Change Credit API
# This API performs request to change the credit (add or sub) of an account in server database
# Param :
# - credit_url  : URL of Backend API
# - amount      : amount of credit
# - _OTP        : OTP
# - _username   : username of account whose credit is going to be gotten
# - token       : token of session
# -_category    : "Transfer" or "Paybill"
# Return :
# - 1 -> change credit failed due to wrong otp
# - 0 -> change credit success due to wrong otp

def ChangeCredit(credit_url, _username,_amount_, _OTP, token, _category):
    #Put new data to server
    url = credit_url
    response = requests.put(url, json = {'amount_credit' : _amount_, 'username':_username, 'otp' : _OTP, 'category':_category}, headers = {'X-Access-Token': token})
    print(response.json())

    if(response.status_code==401):
        return 1
    else:
        return 0


# Check Recipient API
# This API checks if the recipient's username account does exist in server database
# Param :
# - _recipient : username of recipient's account
# return :
# 1 -> recipient not found
# 0 -> recipient exists
def CheckRecipient(_recipient):
    #Check if recipient does exist
    # Find recipient in database
    response = requests.get(var._user_URL, json = {'username':_recipient}, headers = {'X-Access-Token': var.token})
    if(response.status_code == 404):
        #User not found
        print(_recipient+ ' Not Found')
        return 1
    else :
        return 0

# Transfer Money API
# This API performs transfer money activity
# param :
# -  _recipient     : username of recipient's account
# - _amount_        : amount of money going to be transferred (string)
# - _description    : description of transfer
# - _OTP            : OTP
# - token           : token session
# _category         : "transfer" or "paybill"
# return :
# success -> 0 : Transfer money success
#         -> 1 : Transfer money failed

def TransferMoney(_recipient, _amount_,_description, _OTP, token, _category):
    credit_url = var._user_URL + '/transfer'
    success = 0
    #Change Recipient Credit
    success = ChangeCredit(credit_url, _recipient, (int(_amount_)),_OTP, token, _category)
    #Change Sender Credit
    success = ChangeCredit(credit_url, var.username, (-1)*(int(_amount_)),_OTP, token, _category)
    return success
    # print("Transfering Money Rp"+str(_amount_)+" to "+_recipient)

# Request OTP API
# This API ask server to generate OTP
def RequestOTP():
    response = requests.get(var._otp_URL, headers = {'X-Access-Token': var.token})
    print(response.json())

# Update Info API
# This performs request to get updated user's credit/balance from server database and update the amount_credit in global variable
def UpdateInfo():
    url = var._user_URL
    message = {
        'username' : var.username
    }
    response = requests.get(url,json = message, headers = {'X-Access-Token': var.token})

    user_form = response.json()
    #Update User Info
    var.amount_credit = user_form[0]['amount_credit']
    print(user_form)
