# Global Variables

# Network
localhost = 'http://localhost:'
PORT = 8080
_signup_URL = localhost+str(PORT)+'/api/auth/signup' 
_signin_URL = localhost+str(PORT)+'/api/auth/signin'
_bill_URL = localhost+str(PORT)+'/api/bill'
_user_URL = localhost+str(PORT)+'/api/user'
_otp_URL = localhost+str(PORT)+'/api/processing'

# Variables
token = " "
username = " "
name = " "
amount_credit = " "
bill = []
bill_form = []

bill_name = " "
bill_id = " "
bill_serder = " "
bill_amount = 0
bill_description = " "