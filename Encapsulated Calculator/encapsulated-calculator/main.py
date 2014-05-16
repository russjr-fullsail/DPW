'''
Russell Chatham Jr
DPW
Encapsulated Calculator
5/15/14
'''

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page() #creates an instance of the Page function

       

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
