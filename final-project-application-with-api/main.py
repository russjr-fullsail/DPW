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

class HomeModel(object):
    '''the class that is where the data is fetched, parsed and sorted from the Zillow API'''
    def __init__(self):
        self.__url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1du3zc6q5mz_8tgid&state="
        self.__city = ''
        self.__state = ''
        self.__xmldoc = ''

    def callApi(self):
        #this is used to assemble the request
        request = urllib2.Request(self.__url + self.__state + "&city=" + self.__city)

        #use the urllib2 library to create an object to get the url
        opener = urllib2.build_opener()

        #use the url to get a result - requesting info from the API
        result = opener.open(request)

        #parse the XML
        self.__xmldoc = minidom.parse(result)

        self._homes = []
        home = HomeData()
        home.city = self.__xmldoc.getElementsByTagName('city')[1].firstChild.nodeValue
        home.state = self.__xmldoc.getElementsByTagName('state')[1].firstChild.nodeValue
        home.for_sale = self.__xmldoc.getElementsByTagName('forSale')[0].firstChild.nodeValue
        home.owner_sale = self.__xmldoc.getElementsByTagName('forSaleByOwner')[0].firstChild.nodeValue
        home.foreclosure = self.__xmldoc.getElementsByTagName('foreclosures')[0].firstChild.nodeValue
        home.recently_sold = self.__xmldoc.getElementsByTagName('recentlySold')[0].firstChild.nodeValue
        home.affordability = self.__xmldoc.getElementsByTagName('affordability')[0].firstChild.nodeValue
        home.home_value = self.__xmldoc.getElementsByTagName('value')[2].firstChild.nodeValue
        home.property_tax = self.__xmldoc.getElementsByTagName('value')[26].firstChild.nodeValue
        self._homes.append(home)

    @property
    def homes(self):
        return self._homes

    @property
    def city(self):
        pass

    @property
    def state(self):
        pass

    @city.setter
    def city(self, c):
        self.__city = c

    @state.setter
    def state(self, s):
        self.__state = s

class homeData(object):
    '''this holds the data that is fetched from the model class and is what the view class will show'''
    def __init__(self):
        self.city = ''
        self.state = ''
        self.for_sale = ''
        self.owner_sale = ''
        self.foreclosure = ''
        self.recently_sold = ''
        self.affordability = ''
        self.home_value = ''
        self.property_tax = ''

class Page(object):
    '''the class that holds the main page info and skeleton'''
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Find Your Next Home</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <h1></h1>
        <div class="display">'''

        self._body = ''
        self._close = '''
        </div
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2]+'" />'
            except:
                self._form_inputs += '" />'

    def print_out(self):
        return self._head + "<h3>Please enter city and state to start your search</h3>" + self._form_open + self._form_inputs + self._form_close + self._body +  self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
