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

###Endpoints:

####POST /hash
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

####GET /hash/`<hash>`/

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
