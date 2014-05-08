'''
Russell Chatham
5/8/15
Web App
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>
        """

        self.body = "Welcome to my Python Page!"
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        return self.head + self.body + self.close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
