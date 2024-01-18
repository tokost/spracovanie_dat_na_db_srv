># Ako vytvoriť webovú aplikáciu pomocou Flask a SQLite v Pythone

https://www.geeksforgeeks.org/how-to-build-a-web-app-using-flask-and-sqlite-in-python/

Flask je založený na Pythone a je to svojím rozsahom a poskytovanými možnosťami menší webový framework (rámec). Preto má zvyčajne malú alebo žiadnu závislosť od vonkajších robustných rámcov ako je napr. Django. Napriek tomu, že ide o mikrorámec, prakticky všetko ummožňuje kedykoľvek vytvoriť a pomáhajú mu k tomu podľa potreby iba knižnice Pythonu a v niektorých prípadoch aj knižnice externé. V tomto príspevku vytvoríme aplikáciu na báze Flask, ktorá bude zhromažďovať vstupy používateľov do formulára a zobrazí ich na ďalšej webovej stránke pomocou databázy SQLite v Pythone .

## Inštalácia Flask

Aby sme mohli začať s vývojom našej tzv. front-end-ovej časti t.j. časti s ktorou prichádza do styku užívateľ a preto svoju činnosť vykonáva na popredí celej webovej aplikácie, musíme najprv nainštalovať Flask. Pre úplnosť treba povedať že niektoré časti spomínanej aplikácie svoju činnosť nevykonávajú na úrovni klienta, ale na serveri t.j. na pozadí tzv. back-end-e. Flask a databázový SW SQLLite nainštalujeme do virtuálneho prostredia (2. Krok) týmito príkazmi:
~~~
pip install flask
pip install db-sqlite3
~~~
## Postup vytvorenia aplikácie pomocou Flask a SQLite
1. Krok: Vytvoríme si virtuálne prostredie v ktorom 

2. Krok: Nainštalujeme požadované moduly

3. Krok: Začneme vytvárať frontend webovej aplikácie do jednotlivých súborov kódu:

* **index.html**

Súbor index.html bude obsahovať dve tlačidlá, jedno tlačidlo na kontrolu všetkých zoznamov účastníkov (prevzaté z databázy). A ďalšie tlačidlo na vytvorenie nového záznamu. Tu je jeho obsah:
~~~
<!DOCTYPE html>
<html>
	<head>
		<title>Flask and SQLite </title>
	</head>
	<body>
		<h1>Build Web App Using Flask and SQLite</h1>
		<button class="btn" type="button" onclick="window.location.href='{{ url_for('join') }}';">Fill form to get updates</button><br/>
		<button class="btn" type="button" onclick="window.location.href='{{ url_for('participants') }}';">Check participant list</button>
	</body>
</html>
~~~
* **join.html**

V join.html vytvoríme jednoduchý formulár, ktorý bude obsahovať meno, e-mail, mesto, krajinu a telefón za účelom získania vstupných údajov ktoré budú uložené do databázy. Metódou [POST](https://cs.wikipedia.org/wiki/POST) prijmeme žiadosť o formulár jednotlivých databázových stĺpcov a po vložení údajov do tabuľky potvrdíme ňou zmeny v databáze. 
~~~
<!DOCTYPE html>
<html>
	<head>
		<title>Flask and SQLite </title>
	</head>
	<body>
		<form method="POST">
			<label>Enter Name:</label>
			<input type="name" name="name" placeholder="Enter your name" required><br/>
			<label>Enter Email:</label>
			<input type="email" name="email" placeholder="Enter your email" required><br/>
			<label>Enter City:</label>
			<input type="name" name="city" placeholder="Enter your City name" required><br/>
			<label>Enter Country:</label>
			<input type="name" name="country" placeholder="Enter the Country name" required><br/>
			<label>Enter phone num:</label>
			<input type="name" name="phone" placeholder="Your Phone Number" required><br/>
			<input type = "submit" value = "submit"/><br/>
		</form>
	</body>
</html>
~~~
* **participants.html**

V súbore pre užívateĽov budemne používať tag (značku) <th> ako pre tabuľku, tak aj pre priraďovanie nadpisov pre jednotlivé údaje. Ak chceme pri novom zázname automaticky uskutočniť zvýšenie o jeden riadok tabuľky, použijeme šablónu For loop jinja. Vo vnútri cyklu For pridáme značky <tr> a <td>. 

~~~
<!DOCTYPE html>
<html>
	<head>
		<title>Flask and SQLite </title>
	</head>
	<style>
		table, th, td {
		border:1px solid black;
		}
		</style>
	<body>
		<table style="width:100%">
			<tr>
			<th>Name</th>
			<th>Email</th>
			<th>City</th>
			<th>Country</th>
			<th>Phone Number</th>
			</tr>
			{%for participant in data%}
			<tr>
				<td>{{participant[0]}}</td>
				<td>{{participant[1]}}</td>
				<td>{{participant[2]}}</td>
				<td>{{participant[3]}}</td>
				<td>{{participant[4]}}</td>
				</tr>
			{%endfor%}
		</table>		
	</body>
</html>
~~~
>#### Pozor: Tieto súbory musia byť uložené v adresári adresar_projektu/templates lebo práve tu sú šablóny vždy hľadané !!!
4. Krok: Vytvoríme hlavný - počiatočný súbor app.py

Súbor s názvom **app.py** je súbor ktorým našu webovú aplikáciu budeme spúšťať. Urobíme tak po tom čo sme si vytvorili klientské rozhranie webovej aplikácie vytvorením vyššie uvedených HTML šablón. Následne budeme postupovať po jednotlivých bodoch nasledovne: 
* Na vloženie údajov do databázy musíme najskôr vytvoriť novú databázovú tabuľku. Stĺpce, ktoré sa majú vložiť do databázy, sú Meno, E-mail, Mesto, Krajina a Telefónne číslo. 
* Základnou podmienkou pre používanie sqlite3 je najprv vytvoriť danú databázu (ručne alebo príkazom cez inicializáciu). Zápisom sqlite3.connect(“database.db”) sa vytvorí spojenie s novou databázou ktorá má v našom príklade meno **database.db**. Ak ešte naša tabuľka v databáze neexistuje (skontrolujeme si to napr. s DB Browser for SQLite) tak ďalším krokom je vytvorenie novej tabuľky. 
* Jedno tlačidlo v index.html vyzve na zoznam účastníkov, a teda pomocou existujúcej databázy vyberte * z tabuľky a zobrazte ju pomocou šablóny Python, tj šablóny Jinja, aby ste prešli slučkou v rámci HTML. V nasledujúcom kóde sme vytvorili značku tabuľky, do značky tabuľky pre každé nové vloženie do databázy pridáme šablónu Loop Jinja na automatické zvýšenie nového riadku tabuľky. 
* Vo funkcii účastníkov používame výber všetkých stĺpcov z názvu tabuľky, na získanie údajov používame metódu fetchall(). 
~~~
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')


connect = sqlite3.connect('database.db')
connect.execute(
	'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, \
	email TEXT, city TEXT, country TEXT, phone TEXT)')


@app.route('/join', methods=['GET', 'POST'])
def join():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		city = request.form['city']
		country = request.form['country']
		phone = request.form['phone']

		with sqlite3.connect("database.db") as users:
			cursor = users.cursor()
			cursor.execute("INSERT INTO PARTICIPANTS \
			(name,email,city,country,phone) VALUES (?,?,?,?,?)",
						(name, email, city, country, phone))
			users.commit()
		return render_template("index.html")
	else:
		return render_template('join.html')


@app.route('/participants')
def participants():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM PARTICIPANTS')

	data = cursor.fetchall()
	return render_template("participants.html", data=data)


if __name__ == '__main__':
	app.run(debug=False)
~~~

Výkon: 

Pre trasu: http://127.0.0.1:5000/ 

![](f/obrazky/obr01.png)

Pre trasu: http://127.0.0.1:5000/join

Tu pridávame do databázy dva nové údaje. 
![](/obrazky/obr02.png)

![](/obrazky/obr03.png)

![](/obrazky/obr04.png)

![](/obrazky/obr15.png)
