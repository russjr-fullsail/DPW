'''
Russell Chatham Jr.
DPW
What Does The Fox Say
5/21/14
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Form()
        page.title = "What Does the Fox Say"
        page.css = '<link href="css/main.css" rel="stylesheet" type="text/css">'
        page.method= 'GET'
        page.update()

        # Lion
        lion = Sound()
        lion.name = 'African lion'
        lion.phylum = 'Chordata'
        lion.class = 'Mammalia'
        lion.order = 'Carnivore'
        lion.family = 'Felidae'
        lion.genus = 'Panthera'
        lion.species = 'Panthera Leo'
        lion.img = 'http://animaldiversity.ummz.umich.edu/accounts/Panthera_leo/pictures/collections/contributors/kay_holekamp/PrideofLions9_91'
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
