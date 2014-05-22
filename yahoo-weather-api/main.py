'''
Russell Chatham Jr.
DPW
Weather App
5/22/14
'''
import webapp2
import urllib2 #python classes and code needed to open url info
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'zip code'],['Submit', 'submit']]
        self.response.write(p.print_out())

        if self.request.GET:
            #get info from API
            zip = self.request.GET['zip']
            url = "http://xml.weather.yahoo.com/forecastrss?p=" + zip
            #assemble the request
            request = urllib2.Request(url)
            #use the urllib2 library to create an object to get url
            opener = urllib2.build_opener()
            #use url to get results - requesting info from the API
            result = opener.open(request)

            #parse xml
            xmldoc = minidom.parse(result)
            self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
            self.content = ''
            list = xmldoc.getElementsByTagName("yweather:forecast")
            for item in list:
                self.content += item.attributes['day'].value
                self.content += '</br>'

            self.response.write(self.content)



class Page(object): #borrowing stuff form the object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>
        '''
        self._body = 'Weather App'
        self._close = '''
    </body>
</html>
        '''
    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constrctor function for the super class
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        #<input type="text" value="" name="first_name" placeholder="First Name" />
        # ['first_name', 'text', 'First Name']
        #<input type="text" value="" name="last_name" placeholder="Last Name" />
        #<input type="submit" value="Submit" />

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through the mega array and cresate HTML inputs based on the info there.
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '"name="' + item[0]
            #if there is a third item add it in
            try:
                self._form_inputs += '"placeholder="' + item[2] + '" />'
            #otherwise end the tag
            except:
                self._form_inputs += '" />'

        print self._form_inputs

    #Polymorphism - method overriding
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
