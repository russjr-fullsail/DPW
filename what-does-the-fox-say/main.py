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
        page.method = 'GET'
        page.update()

        # Lion class that gets all the attributes from the Animals class
        lion = Sound()
        lion.name = 'African Lion'
        lion.phylum = 'Chordata'
        lion.classs = 'Mammalia'
        lion.order = 'Carnivore'
        lion.family = 'Felidae'
        lion.genus = 'Panthera'
        lion.species = 'Panthera Leo'
        lion.img = 'http://animaldiversity.ummz.umich.edu/collections/contributors/christopher_jameson/panthera_leo_9/large.jpg'
        lion.lifespan = '14'
        lion.habitat = 'temperate, tropical and terrestrial'
        lion.geolocation = 'sub-Saharian'
        lion.sound = 'Rawr'
        lion.update()

        # seal class that gets all the attributes from the Animals class
        seal = Sound()
        seal.name = 'Gray Seal'
        seal.phylum = 'Chordata'
        seal.classs = 'Mammalia'
        seal.order = 'Carnivore'
        seal.family = 'Phocidae'
        seal.genus = 'Halichoerus'
        seal.species = 'Halichoerus grypus'
        seal.img = 'http://animaldiversity.ummz.umich.edu/collections/contributors/tanya_dewey/grayseal/large.jpg'
        seal.lifespan = '15 to 25'
        seal.habitat = 'temperate, polar, terrestrial, saltwater or marine'
        seal.geolocation = 'temperate and subartic waters'
        seal.sound = 'arr arr arr'
        seal.update()

        # fox class that gets all the attributes from the Animals class
        fox = Sound()
        fox.name = 'Red Fox'
        fox.phylum = 'Chordata'
        fox.classs = 'Mammalia'
        fox.order = 'Carnivore'
        fox.family = 'Canidae'
        fox.genus = 'Vulpes'
        fox.species = 'Vulpes vulpes'
        fox.img = 'http://animaldiversity.ummz.umich.edu/collections/contributors/phil_myers/ADW_mammals/Carnivora/Canidae/fox1374/large.jpg'
        fox.lifespan = '12'
        fox.habitat = 'temperate, terrestrial'
        fox.geolocation = 'desert or dune, savanna, forest, mountains'
        fox.sound = 'yit yit'
        fox.update()

        #Array with all the animals in it
        anim = [lion, seal, fox]

        self.response.write(page.header)
        self.response.write(page.getForm)
        if self.request.GET:
            button = int(self.request.GET['animal'])
            self.response.write(self.html(anim[button]))
        self.response.write(page.closer)

    def html(self, obj):
        result = '''
    <div id="result">
        <h2>{obj.name}</h2>
        {obj.soundPass}
        <img src={obj.img} alt="{obj.name}" height="300">
        <ul>
            <li>
                <p>Phylum: {obj.phylum}</p>
            </li>
            <li>
                <p>Class: {obj.classs}</p>
            </li>
            <li>
                <p>Order: {obj.order}</p>
            </li>
            <li>
                <p>Family: {obj.family}</p>
            </li>
            <li>
                <p>Genus: {obj.genus}</p>
            </li>
            <li>
                <p>Species: {obj.species}</p>
            </li>
            <li>
                <p>Lifespan: {obj.lifespan} years</p>
            </li>
            <li>
                <p>Habitat: {obj.habitat}</p>
            </li>
            <li>
                <p>Geolocation: {obj.geolocation}</p>
            </li>
        </ul>
    </div>
        '''
        result = result.format(**locals())
        return result

class PageBase(object):
    def __init__(self):
        self.title = ""
        self.css = ''

        self._header = '''
<!DOCTYPE>
<html>
    <head>
        <title>{self.title}</title>
        {self.css}
    </head>
    <body>
        '''
        self.__closer = '''
    </body>
</html>
        '''

    @property
    def header(self):
        return self._header

    @property
    def closer(self):
        return self.__closer

    def update(self):
        self._header = self._header.format(**locals())

class Form(PageBase):
    def __init__(self):
        super(Form, self).__init__() #super --> calling PageBase's init

        self.method = "POST"
        self.action = ''

        self.__formOpen = '''
        <form action="{self.action}" method="{self.method}" name="foxSay" id="buttons">
            <a href="/?animal=0" name="animal" id="lion">African Lion</a>
            <a href="/?animal=1" name="animal" id="seal">Gray Seal</a>
            <a href="/?animal=2" name="animal" id="fox">Red Fox</a>
        </form>
        '''

        self.__formClose = '''
        </form>
        '''

    @property
    def getForm(self):
        return self.__formOpen + self.__formClose

    def update(self):
        self._header = self._header.format(**locals())
        self.__formOpen = self.__formOpen.format(**locals())

#Sets the original class where the smaller classes take note from
class Animal(object):
    def __init__(self):
        self._name = ''
        self.phylum = ''
        self.classs = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.species = ''
        self.img = ''
        self.lifespan = ''
        self.habitat = ''
        self.geolocation = ''
        self.sound = ''

        @property
        def Name(self):
            return self._name

class Sound(Animal): # makes a class Sound that is part of the Animal class
    def __init__(self):
        super(Sound, self).__init__()

        self.__soundP = '''
        <p id="sound">The {self.name} says {self.sound}</p>
    '''

    @property
    def soundPass(self):
        return self.__soundP

    def update(self):
        self.__soundP = self.__soundP.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
