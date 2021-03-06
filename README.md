# sha256-service

###Dependencies:

Python 2.7.x  
pip  
virtualenv  


###Run:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Or to run the tests:

```
python test.py
```

###Caveats

For the sake of this challenge, I am holding data entered by the user in memory. The data does not persistence after killing the server, and concurrent requests are sure to cause problems.

The SHA256 hash created is with hex encoding. To retreive the data associated with that hash, the hash must be entered in hex.


###Endpoints:

####POST /hash/
Request Headers Content-Type must be "application/json"

Example:

Request
```
"headers": {
  "content-type": "application/json"
},
"data": {
  "foo": "bar"
}
```
Response
```
201
{
  "hash": "426fc04f04bf8fdb5831dc37bbb6dcf70f63a37e05a68c6ea5f63e85ae579376"
}
```

Error Responses
```
400 - Content-Type not application/json

400 - Post Data not valid JSON
```

####GET /hash/:hash

Example:

Request
```
GET /hash/426fc04f04bf8fdb5831dc37bbb6dcf70f63a37e05a68c6ea5f63e85ae579376/
```

Response
```
200
{
  "foo": "bar"
}
```

Error Responses
```
400 - not a valid SHA256 Hash

404 - resource not found
```
