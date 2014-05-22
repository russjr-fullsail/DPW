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
        lion.name = 'African Lion'
        lion.phylum = 'Chordata'
        lion.classs = 'Mammalia'
        lion.order = 'Carnivore'
        lion.family = 'Felidae'
        lion.genus = 'Panthera'
        lion.species = 'Panthera Leo'
        lion.img = 'http://animaldiversity.ummz.umich.edu/accounts/Panthera_leo/pictures/collections/contributors/kay_holekamp/PrideofLions9_91'
        lion.lifespan = '14'
        lion.habitat = 'temperate; tropical and terrestrial'
        lion.geolocation = 'sub-Saharian'
        lion.sound = 'Rawr Rawr'
        lion.update()

        # seal
        seal = Sound()
        seal.name = 'Grey Seal'
        seal.phylum = 'Chordata'
        seal.classs = 'Mammalia'
        seal.order = 'Carnivore'
        seal.family = 'Phocidae'
        seal.genus = 'Halichoerus'
        seal.species = 'Halichoerus grypus'
        seal.img = 'http://animaldiversity.ummz.umich.edu/accounts/Halichoerus_grypus/pictures/collections/contributors/Grzimek_mammals/Phocidae/Halichoerus_grypus_male'
        seal.lifespan = '15 to 25'
        seal.habitat = 'temperate; polar; terrestrial; saltwater or marine'
        seal.geolocation = 'temperate and subartic waters'
        seal.sound = ''
        seal.update()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
