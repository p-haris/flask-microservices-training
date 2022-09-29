from werkzeug.exceptions import HTTPException
#Werkzeug  is a utility library for the Python programming language for Web Server Gateway Interface (WSGI) applications. Werkzeug can instantiate objects for request, response, and utility functions.
#WSGI - is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. 

class ProductNotFount(HTTPException):
    def __init__(self, message='Product not found', code=400):
        self.message = message
        self.code = code
        super().__init__()
        #This initializes the parent class object into the child class.




