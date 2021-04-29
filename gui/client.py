import requests
import sys
import json
import variable
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

def SignUp(form) :
    url = _signup_URL
    # Getting Header
    response = requests.get(url)
    headers = response.headers
    print(headers)

    # Post form to server
    requests.post(url, json = form)

def Signin(_username, _password) :
    form = {
        "username" : _username,
        "password" : _password
    }
    form_json = json.dumps(form)
    status = 0

    url = _signin_URL
    response = requests.post(url, json = form_json)
    if (response.status_code == 200):
        status = 0
    elif (response.status_code == 404): #User not found
        status = 1
    elif (response.status_code == 401) : #Wrong Password
        status = 2
    #saving token session
    token = response.headers 
    print("Posting to " + url)
    print(form)
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
    response = requests.put(url, headers = token)

def DeleteBill(_bill_id):
    url = _bill_URL +'/'+ _bill_id
    response = requests.delete(url, headers = token)


def GetCredit (credit_url, _username, token) :
    #Get Credit from server
    url = credit_url + _username
    response = requests.get(url, headers = token)

    credit = response.json().load()
    return(credit[amount_credit])

def ChangeCredit(credit_url, _username,_amount_, token):
    #Put new data to server
    url = credit_url + _username
    response = requests.put(url, _amount_, headers = token)

def TransferMoney(_recipient, _amount_, _description,token):
    credit_url = _user_URL + '/'
    #Get recipient credit
    recipient_credit = GetCredit(credit_url, _recipient, token)
    #get sender credit
    sender_credit = GetCredit(credit_url, username, token)
    
    #adding recipient credit
    recipient_credit_buffer = recipient_credit + _amount_
    #reducing sender credit
    sender_credit_buffer = sender_credit - _amount_
    
    #Change Recipient Credit
    ChangeCredit(credit_url, _recipient, recipient_credit_buffer, token)
    #Change Sender Credit
    ChangeCredit(credit_url, username, sender_credit_buffer, token)

    print("Transfering Money Rp"+str(_amount_)+" to "+_recipient)

def FillSignin() :
    print('Sign in')
    _username   = input('username: ')
    _password   = input('password: ')
    
if __name__ == '__main__':
    Main()