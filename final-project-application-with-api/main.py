'''
Russell Chatham Jr.
DPW
Final Project Application with API
5/29/14
'''
import webapp2
import urllib2 #python classes and code needed to requesting info, receiving, and opening
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    '''class controller for collecting and sending info from the view to model class'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
