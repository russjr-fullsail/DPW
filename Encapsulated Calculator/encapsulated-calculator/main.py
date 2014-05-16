'''
Russell Chatham Jr
DPW
Encapsulated Calculator
5/15/14
'''

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page() #creates an instance of the Page function

        #Star Wars Episode IV (1977)
        self.epiv = Movie()
        self.epiv.title = "Star Wars Episode IV"
        self.epiv.ustheater = 460000000
        self.epiv.eutheater = 314000000
        self.epiv.calc_total_sales()
        print "The total number of ticket sales for " +self.epiv.title+ " is " +str(self.epiv.total_sales)

        




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
