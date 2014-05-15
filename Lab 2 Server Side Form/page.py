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
            <label for="bday">D.O.B:</label>
			<select name="bday" id="firstselect">
				<option value="na">Day</option>
				<option value="1">1</option>
				<option value="2">2</option>
				<option value="3">3</option>
				<option value="4">4</option>
				<option value="5">5</option>
				<option value="6">6</option>
				<option value="7">7</option>
				<option value="8">8</option>
				<option value="9">9</option>
				<option value="10">10</option>
				<option value="11">11</option>
				<option value="12">12</option>
				<option value="13">13</option>
				<option value="14">14</option>
				<option value="15">15</option>
				<option value="16">16</option>
				<option value="17">17</option>
				<option value="18">18</option>
				<option value="19">19</option>
				<option value="20">20</option>
				<option value="21">21</option>
				<option value="22">22</option>
				<option value="23">23</option>
				<option value="24">24</option>
				<option value="25">25</option>
				<option value="26">26</option>
				<option value="27">27</option>
				<option value="28">28</option>
				<option value="29">29</option>
				<option value="30">30</option>
				<option value="31">31</option>
            </select>
            <label> Sex: </label>
            <div id="radio">
                <input type="radio" name="sex" value="male" id="male">
                <label for="male">Male</label>
                <input type="radio" name="sex" value="female" id="female">
                <label for="female">Female</label>
            </div>

            <label for="member">Please vote for your favorite vehicle</label>

            <div class="form-checkbox"><input type="checkbox" name="member" id="jeep" value="jeep" /><label for="jeep"><img src="images/jeep.png" alt="Jeep Rubicon"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="1963chevytruck" value="1963chevytruck" /><label for="1963chevytruck"><img src="images/1963_chevy_truck.png" alt="1963 Chevy Truck"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="1968shelbycobra" value="1968shelbycobra" /><label for="1968shelbycobra"><img src="images/1968_shelby_cobra.png" alt="1968 Shelby Cobra"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="1970oldsmobile442" value="1970oldsmobile442" /><label for="1970oldsmobile442"><img src="images/1070_oldsmobile_442.png" alt="1070 Oldsmobile 442"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="1973roadrunner" value="1973roadrunner" /><label for="1973roadrunner"><img src="images/1973_roadrunner.png" alt="1973 Roadrunner"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="chevycamaro" value="chevycamaro" /><label for="chevycamaro"><img src="images/chevy_camaro.png" alt="Chevy Camaro"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="chevytahoe" value="chevytahoe" /><label for="chevytahoe"><img src="images/chevy_tahoe.png" alt="Chevy Tahoe"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="dodgecharger" value="dodgecharger" /><label for="dodgecharger"><img src="images/dodge_charger.png" alt="Dodge Charger"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="fordraptor" value="fordraptor" /><label for="fordraptor"><img src="images/ford_raptor.png" alt="Ford Raptor"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="dodgeram" value="dodgeram" /><label for="dodgeram"><img src="images/dodge_ram.png" alt="Dodge Ram"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="fordmustang" value="fordmustang" /><label for="fordmustang"><img src="images/ford_mustang.png" alt="Ford Mustang"/></label></div>
            <div class="form-checkbox"><input type="checkbox" name="member" id="shelbygt500" value="shelbygt500" /><label for="shelbygt500"><img src="images/shelby_gt500.png" alt="Shelby GT500"/></label></div>