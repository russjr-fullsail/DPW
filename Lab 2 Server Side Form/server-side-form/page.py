'''
Russell Chatham Jr.
DPW
Server Side Form
5/15/14
'''

class Page():
    def __init__(self):
		self.header ='''<!DOCTYPE>
<html>
    <head>
        <title>Welcome To Vehicle Chooser</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
    </head>
    <body>
    <header>
		<h1>Please Select your Favorite Vehicles (up to five please)</h1>
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
            <select name="bmonth">
				<option value="na">Month</option>
				<option value="January">January</option>
				<option value="February">Febrauary</option>
				<option value="March">March</option>
				<option value="April">April</option>
				<option value="May">May</option>
				<option value="June">June</option>
				<option value="July">July</option>
				<option value="August">August</option>
				<option value="September">September</option>
				<option value="October">October</option>
				<option value="November">November</option>
				<option value="December">December</option>
			</select>
			<select name="byear">
				<option value="1998">1998</option>
				<option value="1997">1997</option>
				<option value="1996">1996</option>
				<option value="1995">1995</option>
				<option value="1994">1994</option>
				<option value="1993">1993</option>
				<option value="1992">1992</option>
				<option value="1991">1991</option>
				<option value="1990">1990</option>
				<option value="1989">1989</option>
				<option value="1988">1988</option>
				<option value="1987">1987</option>
				<option value="1986">1986</option>
				<option value="1985">1985</option>
				<option value="1984">1984</option>
				<option value="1983">1983</option>
				<option value="1982">1982</option>
				<option value="1981">1981</option>
				<option value="1980">1980</option>
				<option value="1979">1979</option>
				<option value="1978">1978</option>
				<option value="1977">1977</option>
				<option value="1976">1976</option>
				<option value="1975">1975</option>
				<option value="1974">1974</option>
				<option value="1973">1973</option>
				<option value="1972">1972</option>
				<option value="1971">1971</option>
				<option value="1970">1970</option>
			</select>
            <label> Sex: </label>
            <div id="radio">
                <input type="radio" name="sex" value="male" id="male">
                <label for="male">Male</label>
                <input type="radio" name="sex" value="female" id="female">
                <label for="female">Female</label>
            </div>

            <label for="member">Please vote for your favorite vehicle</label>

                <div class="form-checkbox"><input type="checkbox" name="member" id="jeep" value=" 2014 Jeep Rubicon" /><label for="jeep"><img src="images/jeep.png" alt="Jeep Rubicon"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="1963chevytruck" value=" 1963 Chevy Truck" /><label for="1963chevytruck"><img src="images/1963_chevy_truck.png" alt="1963 Chevy Truck"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="1968shelbycobra" value=" 1968 Shelby Cobra" /><label for="1968shelbycobra"><img src="images/1968_shelby_cobra.png" alt="1968 Shelby Cobra"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="1970oldsmobile442" value=" 1970 Oldsmobile 442" /><label for="1970oldsmobile442"><img src="images/1970_oldsmobile_442.png" alt="1070 Oldsmobile 442"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="1973roadrunner" value=" 1973 Plymouth Roadrunner" /><label for="1973roadrunner"><img src="images/1973_roadrunner.png" alt="1973 Roadrunner"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="chevycamaro" value=" 2013 Chevy Camaro" /><label for="chevycamaro"><img src="images/chevy_camaro.png" alt="Chevy Camaro"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="chevytahoe" value=" 2015 Chevy Tahoe" /><label for="chevytahoe"><img src="images/chevy_tahoe.png" alt="Chevy Tahoe"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="dodgecharger" value=" 2014 Dodge Charger" /><label for="dodgecharger"><img src="images/dodge_charger.png" alt="Dodge Charger"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="fordraptor" value=" 2011 Ford Raptor" /><label for="fordraptor"><img src="images/ford_raptor.png" alt="Ford Raptor"/></label></div>
                <div class="form-checkbox"><input type="checkbox" name="member" id="shelbygt500" value=" 2014 Shelby GT500" /><label for="shelbygt500"><img src="images/shelby_gt500.png" alt="Shelby GT500"/></label></div>

            <input type="submit" value="Submit" />
        </form>'''
		self.closer = '''
    </body>
</html>'''
