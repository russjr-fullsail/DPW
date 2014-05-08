'''
Russell Chatham
5/8/2014
DPW
Assignment
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything.  Catalyst
        self.response.write('Hello world!')
        #code goes here

    def additional_functions(self):
        pass
        #code goes here

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
