__author__ = 'russjr'

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()
        
class Button(object):
    def __init__(self):
        self.label = ""
        #self.on_roll_over("Hello!!")

    def click(self):
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button" + message

     def show_label(self):
         print "My label is" + self.label

app = webapp2.WSGIApppplication([
    ('/', MainHandler)
], debug=True)