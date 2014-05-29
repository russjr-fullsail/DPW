'''
Russell Chatham Jr.
DPW
Application with API
5/28/14
'''
import webapp2
import urllib2 #python classes and code for requesting info, receiving info and opening
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):#controller class that is collecting and sending information from the view to model class
    def get(self):
        p = FormPage()
        p.inputs = [['city', 'text', 'City'],['state', 'text', 'State'],['Submit', 'submit']]
        

class MainHandler(webapp2.RequestHandler):
    def get(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
