'''
Russell Chatham
5/8/15
Web App
'''
import webapp2
from pages import Page #from package import Class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Miss Piggy like Kermit De Frog!"
        self.response.write (p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
