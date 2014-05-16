'''
Russell Chatham Jr.
DPW
Encapsulated Calculator
5/15/14
'''
class Page():
    def __init__(self):
        self.header = '''<!DOCTYPE>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Star Wars Movie Sales</title>
            <link rel="stlesheet" href="css/main.css" type="text/css" />
        </head>
        <body>
            <div id="container">
            <h1>Star Wars Theater Sales</h1>

        self.links = '''<a href="?movie=0" class="links">Star Wars - Episode IV - A New Hope (1977)"</a>
        <a href="?movie=1" class="links">Star Wars - Episode V - Empire Strikes Back (1980) </a>
		<a href="?movie=2" class="links">Star Wars - Episode VI - Return of the Jedi (1983)</a>
		<a href="?movie=3" class="links">Star Wars - Episode I - The Phantom Menace (1999)</a>
		<a href="?movie=4" class="links">Star Wars - Episode II - Attack of the Clones (2002)</a>
        <a href="?movie=5" class="links">Star Wars - Episode III - Revenge of the Sith (2005)</a>
		<a href="?movie=6" class="links">Star Wars - The Clone Wars (2008)</a>

        self.footer = '''
        </body>

        <footer>
            