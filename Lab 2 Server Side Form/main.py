'''
Russell Chatham Jr.
5/15/14
DPW
Server Side Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page() #Creates the instance of imported class page

        if self.request.GET: #if a URL variable then print this
            myList = self.request.get_all("member") #get_all makes it a list

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
