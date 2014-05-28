'''
Russell Chatham Jr.
DPW
Application with API
5/28/14
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
