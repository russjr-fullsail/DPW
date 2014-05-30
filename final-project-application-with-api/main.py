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
    def get(self):
        p = FormPage()
        p.inputs = [['city', 'text', 'City'],['state', 'text', 'State'],['submit', 'Submit']]

        if self.request.GET: #will only work if city and State are in URL
            #get info from API and creates model
            hm = HomeMode()
            hm.city = self.request.GET['city']
            hm.state = self.request.GET['state']
            hm.callApi()

            #takes the data from model class and sends it to the view class
            hv = HomeView()
            hv.home = hm.homes
            p._body = hv.content

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
