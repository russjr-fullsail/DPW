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

class WeatherView(object):
    '''This class handles how the data is shown to the user'''
    def __init__(self):
        self.__wdos = []
        self.__content = '<br />'

    def update(self):
        for do in self.__wdos:
            self.__content += do.day + "      HIGH:  " + do.high + "      Low:  " + do.low + "      CONDITION:  "+ do.condition + '<br />'

    @property
    def content(self):
        return self.__content

    @property
    def wdos(self):
        pass

    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr
        self.update()

class WeatherModel(object):
    '''This model handels fetching, parsing and sorting data form Yahoo's weather APT'''
    def __init__(self):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.__zip = ''
        self.__xmldoc = ''


    def callApi(self):
        request = urllib2.Request(self.__url+self.__zip)
        opener = urllib2.build_opener()
        result = opener.open(request)
        self.__xmldoc = minidom.parse(result)

        self.content = '<br/>'
        list = self.__xmldoc.getElementsByTagName("yweather:forecast")
        self._dos = []

        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes['low'].value
            do.code = tag.attributes['code'].value
            do.condition = tag.attributes['text'].value
            do.date = tag.attributes['date'].value
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z

class WeatherData(object):
    ''' This data object holds the data fetched by the model and shown by the view'''
    def __init__(self):
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''

class Page(object):
    def __init__(self):
        self._head = '''
<html>
    <head>
        <title></title>
    </head>
    <body>'''
        self._body = ''
        self._close = '''
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
                self._form_inputs += '" placeholder="' + item[2] + '" required/>'

            except:
                self._form_inputs += '" />'

    def print_out(self):
        return self._head + "Weather App" + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
