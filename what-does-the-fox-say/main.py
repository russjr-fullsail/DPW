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
        lion.name = 'Panthera Leo'
        lion.phylum = 'Chordata'
        lion.class = 'Mammalia'
        lion.order = 'Carnivore'
        lion.family = ''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)