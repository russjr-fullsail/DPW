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
        lion.img = 'http://animaldiversity.ummz.umich.edu/accounts/Panthera_leo/pictures/collections/contributors/christopher_jameson/panthera_leo_9/'
        lion.lifespan = '14'
        lion.habitat = 'temperate, tropical and terrestrial'
        lion.geolocation = 'sub-Saharian'
        lion.sound = 'Rawr'
        lion.update()

        # seal
        seal = Sound()
        seal.name = 'Gray Seal'
        seal.phylum = 'Chordata'
        seal.classs = 'Mammalia'
        seal.order = 'Carnivore'
        seal.family = 'Phocidae'
        seal.genus = 'Halichoerus'
        seal.species = 'Halichoerus grypus'
        seal.img = 'http://animaldiversity.ummz.umich.edu/accounts/Halichoerus_grypus/pictures/collections/contributors/Grzimek_mammals/Phocidae/Halichoerus_grypus_male/'
        seal.lifespan = '15 to 25'
        seal.habitat = 'temperate, polar, terrestrial, saltwater or marine'
        seal.geolocation = 'temperate and subartic waters'
        seal.sound = 'arr arr arr'
        seal.update()

        # fox
        fox = Sound()
        fox.name = 'Red Fox'
        fox.phylum = 'Chordata'
        fox.classs = 'Mammalia'
        fox.order = 'Carnivore'
        fox.family = 'Canidae'
        fox.genus = 'Vulpes'
        fox.species = 'Vulpes vulpes'
        fox.img = 'http://animaldiversity.ummz.umich.edu/accounts/Vulpes_vulpes/pictures/collections/contributors/phil_myers/ADW_mammals/Carnivora/Canidae/fox1374/'
        fox.lifespan = '12'
        fox.habitat = 'temperate, terrestrial'
        fox.geolocation = 'desert or dune, savanna, forest, mountains'
        fox.sound = 'yit yit'
        fox.update()

        anim = [lion, seal, fox]

        self.response.write(page.header)
        self.response.write(page.getForm)
        if self.request.GET:
            button = int(self.request.GET['animal'])
            self.response.write(self.html(anim[button]))
        self.response.write(page.closer)

    def html(selfself,obj):
        result ='''
    <div id="result">
        <h2>{obj.name}</h2>
        {obj.soundPass}
        <img src={obj.img} alt="{obj.name}" height="320"
        <ul>
            <li>
                <p>Phylum: {obj.phylum}</p>

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
