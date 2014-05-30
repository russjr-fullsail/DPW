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

class HomeView(object):
    '''this class shows info from the API call'''
    def __init__(self):
        self.__home = []
        self.__content = '<br/>'

    def update(self):
        for do in self.__home:
            self.__content += "<p>Please choose a category to see homes for: <br/> " + do.city + ", " + do.state + "</p>"
            self.__content += '<p><ul><li><a href="' + do.for_sale + '">For Sale</a></li><li><a href="' + do.owner_sale + '">For Sale By Owner</a></li><li><a href="' + do.foreclosure + '">Foreclosures</a></li><li><a href="' + do.recently_sold + '">Recently Sold</a></li><li><a href="' + do.affordability + '">Area Affordability</a></li><p class="footer">Home Value In This Area: $' + do.home_value + '<br/>Property Tax In This Area: $' + do.property_tax + '</p>'

     @property
    def content(self):
        return self.__content

    @property
    def home(self):
        pass

    @home.setter
    def home(self, arr):
        self.__home = arr
        self.update()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
