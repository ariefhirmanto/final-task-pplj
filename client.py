import sys
import http.client

if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 8080
signup = "localhost:"+ str(PORT)+"/api/auth/signup"
print(signup)
connection = http.client.HTTPConnection("127.0.0.1", 8080)

data = {"username" : "test",
        "email" : "testing@test",
        "name" : "Testing",
        "password": "testing",
        "roles" : ["user"],
        "amount_credit" : "100000",
        "bill_ID" : ["10", "11"],
        "contact" : "0812121"
        }
connection.request('POST', '/api/auth/signup', )
response = connection.getresponse()
# print("Status: {} and reason: {}".format(response.status, response.reason))
# connection.close()
