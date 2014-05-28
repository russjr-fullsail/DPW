'''
Russell Chatham Jr.
DPW
APIAPPProofofConcept
5/22/14
'''

import webapp2
import urllib2
from xml.dom import minidom
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):

    	page = FormPage()
    	#options to be passed into FormPage Class to create options
    	page.options = {'baseball':'Baseball', 'basketball':'Basketball', 'boxing':'Boxing', 'football':'Football', 'golf':'Golf', 'hockey':'Hockey', 'racing':'Racing', 'tennis':'Tennis'}
    	#running the create_options function
    	page.create_options()

    	#looking for request
    	if self.request.GET:
    		#GET the value from select sport
    		zip = self.request.GET['sport']

    		#writing the highlights view to browser
    		sm = SportModel(zip)
        	sm.send()
        	sv = SportView()
        	sv.do = sm.do
        	self.response.write(page._header)
        	self.response.write(page._body)
        	self.response.write(page.get_form)
        	self.response.write(sv.content)
        	self.response.write(page._close)
        else:
        	#write main page to browser
        	self.response.write(page.print_out())


class SportModel(object):
	"""This class is a model and handles the activities to be ran
	"""
	#Using JSON to recieve the url
	def __init__(self,zip):
		self.__url = 'http://api.espn.com/v1/sports/' + zip + '/news?apikey=utmcdhgdbrbsvcz3uvhsxqhy'
		self.__req = urllib2.Request(self.__url)
		self.__opener = urllib2.build_opener()
	#sending to be opened
	def send(self):
		self.__result = self.__opener.open(self.__req)
		self.sort()
	#sort first by loading the json doc
	def sort(self):
		self.__jsondoc = json.load(self.__result)
		self.__do = SportData()

		items = self.__jsondoc['resultsLimit']
		self.__do.items = items
		for l in range(items):
			headlines = self.__jsondoc['headlines'][l]
			#if it has a headline
			try:
				self.__do.headline = headlines['headline']
				self.__do.link = headlines['links']['web']['href']
			#missing a headline use a title instead
			except:
				self.__do.headline = headlines['title']
				self.__do.link = headlines['links']['web']['href']
			#placing results in an array
			self.__do.headline_array.append({'headline': self.__do.headline, 'link': self.__do.link})
			print self.__do.headline_array

	@property
	def do(self):
		return self.__do

class SportData(object):
	"""This class holds the data that is to be received from url
	"""
	def __init__(self):
		self.headline_array = []
		self.headline = ''
		self.link = ''
		self.items = 10

class SportView(object):

	def __init__(self):
		self.__do = SportData()
	#view of item to be printed
	def update(self):
		self.__content = '''
			<div id="result_listings">'''
		#looping through to print items in array
		for l in range(self.__do.items):
			self.__content += '''
				<div class="result_items">
					<h3>''' + self.__do.headline_array[l]['headline'] + '''</h3>'''
			self.__content += '''
					<a href="''' + self.__do.headline_array[l]['link'] + '''">Read More...</a>
				</div>'''
		self.__content += '''
			</div>
		</div>'''

	@property
	def do(self):
		return self.__do

	#refresh what is shown
	@do.setter
	def do(self,new_do):
		self.__do = new_do
		self.update()

	@property
	def content(self):
		return self.__content
#basic html for page
class Page(object):
	def __init__(self):
		self._header = """<!DOCTYPE html>
<html>
	<head>
		<title>The Sports That Matter To You</title>
		<link rel="stylesheet" href="css/main.css">
		<link href='http://fonts.googleapis.com/css?family=PT+Sans: 700' rel='stylesheet' type='text/css'>
	</head>
	<body>
	    <h1>The Sports Highlight Center</h1>
	    <h4>Sports Feed Authority</h4>
	    <p>Please select from the menu the sports you would like to see the news for.</p>
		<div id="container">"""
		self._body = ""
		self._close = """
		</div>
	</body>
</html>"""

	@property
	def body(self):
		pass

	@body.setter
	def body(self, b):
		self._body = b


	def print_out(self):
		return self._header + self._body + self._close
#select and options for user
class FormPage(Page):
	def __init__(self):
		#run instantiating function for super class
		super(FormPage, self).__init__()

		self.__form_open = '''
		<form method="GET">
			<div id="sport_choice">
			<select name="sport">
				<option selected disabled> Choose A Sport...</option>'''
		self.__form_close = '''
			</select>
			<input type="submit" value="SUBMIT" name="submit"/>
			</div>
		</form>'''
		self.__options = dict()
		self.__option_string = ''

	def create_options(self):
		for i in self.__options:
			self.__option_string += '''
				<option value="''' + i + '''">''' + self.__options[i] + '''</option>'''

	def print_out(self):
		return self._header + self.__form_open + self.__option_string + self.__form_close + self._close

	@property
	def get_form(self):
		return self.__form_open + self.__option_string + self.__form_close

	@property
	def options(self):
		pass

	@options.setter
	def options(self, dict):
		self.__options = dict


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

