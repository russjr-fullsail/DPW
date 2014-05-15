'''
Russell Chatham Jr.
DPW
Server Side Form
5/15/14
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page() #Creates the instance of imported class page

        if self.request.GET: #if a URL variable then print this
            myList = self.request.get_all("member") #get_all makes it a list
            myString = ",".join(myList) #seperates the list with commas, this will allow them to be put inside the write function as a string

            message ="Thank you for your vote" + " " + self.request.GET["fName"] + " " + self.request.GET["lName"] +"(" + self.request.GET["sex"] + ")" + ", Born on " + self.request.GET["bday"] + "th" + " of " + self.request.GET["bmonth"] + " " + self.request.GET["byear"] + ". You have voted for the following characters:" +myString
			self.response.write(page.header + message + page.closer)

            else:
			self.response.write(page.header + page.registration + page.closer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
