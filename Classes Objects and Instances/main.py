__author__ = 'russjr'

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world')

class Button(object):
    def __init__(self):
        pass

    def click(self):

app = webapp2.WSGIApppplication([
    ('/', MainHandler)
], debug=True)