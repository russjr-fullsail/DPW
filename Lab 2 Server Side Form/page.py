'''
Russell Chatham Jr.
DPW
Server Side Form
5/15/14
'''

def __init__(self):
		self.header ='''<!DOCTYPE>
<html>
    <head>
        <title>Welcome To Vehicle Chooser</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
    </head>
    <body>
    <header>
		<h1>Please Select Vehicle"></h1>
	</header>
       '''
		self.registration = form = '''

        <form method="GET" action="">
        	<label for="fName">First name:</label> <input type="text" name="fName" id="fName" />
        	<label for="lName">Last name:</label><input type="text" name="lName" id="lName"/>
