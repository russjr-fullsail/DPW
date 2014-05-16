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
        self.epiv.ustheater = 460998007
        self.epiv.wwtheater = 797900000
        self.epiv.calc_total_sales()
        print "The total number of ticket sales for " +self.epiv.title+ " is " +str(self.epiv.total_sales)

        #Star Wars Episode V (1980)
        self.epv = Movie()
        self.epv.title = "Star Wars Episode V"
        self.epv.ustheater = 290271960
        self.epv.wwtheater = 534171960
        self.epv.calc_total_sales()
        print "The total number of ticket sales for " +self.epv.title+ " is " +str(self.epv.total_sales)

        #Star Wars Episode VI (1983)
        self.epvi = Movie()
        self.epvi.title = "Star Wars Episode VI"
        self.epvi.ustheater = 309205079
        self.epvi.wwtheater = 572700000
        self.epvi.calc_total_sales()
        print "The total number of ticket sales for " +self.epvi.title+ " is " +str(self.epvi.total_sales)

        #Star Wars Episode I (1999)
        self.epi = Movie()
        self.epi.title = "Star Wars Episode I"
        self.epi.ustheater = 474544677
        self.epi.wwtheater = 1007044677
        self.epi.calc_total_sales()
        print "The total number of ticket sales for " +self.epi.title+ " is " +str(self.epi.total_sales)

        #Star Wars Episode II (2002)
        self.epii = Movie()
        self.epii.title = "Star Wars Episode II"
        self.epii.ustheater = 310676740
        self.epii.wwtheater = 656695615
        self.epii.calc_total_sales()
        print "The total number of ticket sales for " +self.epii.title+ " is " +str(self.epii.total_sales)

        







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
