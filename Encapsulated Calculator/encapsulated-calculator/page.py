'''
Russell Chatham Jr.
DPW
Encapsulated Calculator
5/15/14
'''

class Page():
    def __init__(self):
        self.header ='''<!DOCTYPE>
    <html>
        <head>
            <title>Star Wars Movie Sales</title>
            <link rel="stylesheet" href="css/main.css" type="text/css" />
        </head>
        <body>
            <div id="container">
            <h1>Star Wars Theater Sales</h1>'''

        self.links = '''<a href="?movie=0" class="links">Episode IV(1977)</a>
        <a href="?movie=1" class="links">Episode V(1980)</a>
		<a href="?movie=2" class="links">Episode VI(1983)</a>
		<a href="?movie=3" class="links">Episode I(1999)</a>
		<a href="?movie=4" class="links">Episode II(2002)</a>
        <a href="?movie=5" class="links">Episode III(2005)</a>
		<a href="?movie=6" class="links">The Clone Wars(2008)</a>
		'''

        self.footer = '''
        </body>

        <footer>
            <p>Copyright &copy; 2014 <strong>Star Wars Movie Sales</strong>. Figures of money made taken from <a href="http://www.the-numbers.com/movies/franchise/Star-Wars" target="_blank">The Numbers</a></p>
        </footer>
        </div> <!--Closes "container" --->
    </html>'''

    def header(self):
        return self.header

    def links(self):
        return self.links

    def footer(self):
        return self.footer
