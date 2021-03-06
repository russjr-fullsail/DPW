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

        #Star Wars Episode III (2005)
        self.epiii = Movie()
        self.epiii.title = "Star Wars Episode II"
        self.epiii.ustheater = 380270577
        self.epiii.wwtheater = 848998877
        self.epiii.calc_total_sales()
        print "The total number of ticket sales for " +self.epiii.title+ " is " +str(self.epiii.total_sales)

        #Star Wars Clone Wars (2008)
        self.clone = Movie()
        self.clone.title = "Star Wars Episode II"
        self.clone.ustheater = 35161554
        self.clone.wwtheater = 68161554
        self.clone.calc_total_sales()
        print "The total number of ticket sales for " +self.clone.title+ " is " +str(self.clone.total_sales)

        movies = [self.epiv, self.epv, self.epvi, self.epi, self.epii, self.epiii, self.clone]
        print movies

        self.response.write(page.header + page.links)
        if self.request.GET:
            movie = int(self.request.GET['movie'])

            title = movies[movie].title
            ustheater = movies[movie].ustheater
            wwtheater = movies[movie].wwtheater
            total_sales = movies[movie].total_sales

            info='''<div id="info">
			<h3>{title}</h3>
				<section id="sales">
					<p class="labels"><strong>US Theater Sales</strong></p>
					<p class="labels"><strong>Worldwide Theater Sales</strong></p>
					<p class="labels"><strong>Total sales:</strong></p>
				</section>

			    <section id="numbers">
			        <p class="stats">{ustheater}</p>
			        <p class="stats">{wwtheater}</p>
			        <p class="stats">{total_sales}</p>
			    </section>
		    </div>'''
            info = info.format(**locals())

            self.response.write(info)
            self.response.write(page.footer)

# Data-Object Class
class Movie(object):
    def __init__(self):
        self.title = ""
        self.ustheater = 0
        self.wwtheater = 0
        self.__total_sales = 0

    @property
    def total_sales(self):
        return self.__total_sales

    @total_sales.setter #setter
    def total_sales(self, sales):
        self.__total_sales = sales

    def calc_total_sales(self):
        total = self.ustheater + self.wwtheater
        self.__total_sales = total

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
