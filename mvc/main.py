'''
Russell Chatham Jr.
DPW
5/29/14
MVC
'''

import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [  ['zip', 'text','zip code'],['Submit', 'submit']]


        if self.request.GET:

            wm = WeatherModel() #creates our Model
            wm.zip = self.request.GET['zip'] #sends our zip from the url to our Model
            wm.callApi() #tells it to connect to the API
            wv = WeatherView() #creates our View
            wv.wdos = wm.dos #takes data objects form Model and gives them to View
            p._body = wv.content

            #self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
