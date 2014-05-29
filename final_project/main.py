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

        if self.request.GET: #will only work if city and state are in url
            #gets the info from the API and creates the model
            hm = HouseModel()
            hm.city = self.request.GET['city']
            hm.state = self.request.GET['state']
            hm.callApi()
            #takes the data from model class and sends it to the view class
            hv = HouseView()
            hv.housedo = hm.houses
            p._body = hv.content

        self.response.write(p.print_out())


class MainHandler(webapp2.RequestHandler):
    def get(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
