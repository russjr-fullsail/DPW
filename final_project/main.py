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
            hm = HomeModel()
            hm.city = self.request.GET['city']
            hm.state = self.request.GET['state']
            hm.callApi()
            #takes the data from model class and sends it to the view class
            hv = HomeView()
            hv.homedo = hm.homes
            p._body = hv.content

        self.response.write(p.print_out())

class HomeView(object): #this is what the user will view and shows the info from the API call
    def __init__(self):
        self._homedo = []
        self._content = '</br>'

    def update(self):
        for do in self._homedo:
            self._content += "<p>Showing home information in: </br>" + do.city + ", " + do.state + "</p>"
            self._content += '<p><ul><li><a href="' + do.for_sale + '">For Sale</a></li><li><a href="' + do.owner_sale + '">For Sale by Owner</a></li><a href="' + do.foreclosure + '">Foreclosure</a></li></p>'


    @property
    def content(self):
        return self._content

    @property
    def homedo(self):
        pass

    @homedo.setter
    def homedo(self, arr):
        self._homedo = arr
        self.update()

class homeModel(object): #the class for where the data is fetched, parsed and sorted from the Zillow API
    def __inti__(self):
        self._url = "http://www.zillow.com/static/xsd/SearchResults.xsd"
        self.__city = ''
        self.__state = ''
        self.__xmldoc = ''

    def callApi(self): #puts request together
        request = urllib2.Request(self._url + self._state + "&city=" + self._city)

        #







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
