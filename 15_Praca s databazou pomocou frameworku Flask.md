https://www.geeksforgeeks.org/how-to-use-sqlite-viewer-flask/

**SQLite** je populárny ľahký systém správy relačných databáz, ktorý sa používa v rôznych aplikáciách. **Flask** je populárny webový rámec na vytváranie webových aplikácií v Pythone . **SQLite Viewer Flask** je nástroj, ktorý vám umožňuje zobraziť obsah databázy SQLite v aplikácii Flask.

Flask je webový rámec na vytváranie webových aplikácií v programovacom jazyku Python. Ide o ľahký rámec, ktorý poskytuje potrebné nástroje a knižnice na rýchle a jednoduché vytváranie webových aplikácií. V tomto článku sa naučíme, ako používať SQLite Viewer vo Flasku.

**Krok 1: Inštalácia požadovaných knižníc**

Prvým krokom je inštalácia požadovaných knižníc. Budete musieť nainštalovať Flask a SQLite3 . Môžete ich nainštalovať pomocou pip.
~~~
pip install Flask
pip install sqlite3
~~~
**Krok 2: Vytvorenie štruktúry nášho projektu**

Vo VS-Code si vytvoríme nasledovnú štruktúru adresárov a súborov:
![](.SQLite01.png)

**Krok 3: Vytvorenie databázy SQLite a vloženie hodnôt do nej**

Ďalším krokom je vytvorenie databázy SQLite. Na vytvorenie databázy SQLite môžete použiť akýkoľvek nástroj na správu SQLiteako napr. DB Browser SQLite. Pre tento príklad vytvoríme jednoduchú databázu s jednou tabuľkou s názvom „users“ so stĺpcami pre „id“, „name“ a „email“. Kód na jej vytvorenie vložíme do súboru **sql.py**.
~~~
# sql.py

import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# create a table named 'users' with columns for id, name, and email
c.execute('''CREATE TABLE users
	(id INTEGER PRIMARY KEY, name TEXT, email TEXT)
''')

# insert five rows of data into the 'users' table
c.execute('''
INSERT INTO users (name, email) VALUES
	('John Doe', 'johndoe@example.com'),
	('Jane Smith', 'janesmith@example.com'),
	('Bob Johnson', 'bobjohnson@example.com'),
	('Emily Davis', 'emilydavis@example.com'),
	('Mike Lee', 'mikelee@example.com');
''')

# commit changes to the database
conn.commit()

# close the database connection
conn.close()
~~~
Vysledkom činnosti tohoto programu bude niečo takéto:
![](/obrazky/SQLite02.png)

**Krok 4: Vytvorenie aplikácie s flask-om**

Najprv si pomocou príkazu vytvoríme prázdny súbor nášho projektu s názvom **app.py** do ktorého budeme vkladať kód našej aplikácie:
~~~
$ touch app.py
~~~
Bude to kód Pythonu pre jednoduchú webovú aplikáciu s Flask-om, ktorá získava údaje z databázovej tabuľky SQLite ktorá má názov „users“ a vypisuje ich na webovú stránku pomocou HTML šablóny s názvom **index.html**. Aplikácia Flask je vytvorená pomocou triedy Flask a pre predvolenú adresu URL je definovaná trasa. Keď sa pristúpi k trase, aplikácia sa pripojí k databáze, načíta všetky údaje z tabuľky „users“, odovzdá ich ako premennú do šablóny „index.html“ a vykreslí šablónu s načítanými údajmi. Nakoniec sa aplikácia spustí v režime ladenia pomocou metódy **run()** alebo **stlačením šípky** „Run Python File“ vpravo hore.
~~~
# app.py

# import Flask and render_template
from flask import Flask, render_template
# import sqlite3 library for database connection
import sqlite3

# create a Flask instance called app
app = Flask(__name__)

# route the default URL

@app.route('/')
def home():
	# connect to the example.db database
	conn = sqlite3.connect('example.db')
	# create a cursor object to execute SQL commands
	c = conn.cursor()
	# execute a SQL command
	c.execute('SELECT * FROM users')
	# retrieve all the data from the users table
	users = c.fetchall()
	# close the database connection
	conn.close()
	# render the index.html template
	return render_template('index.html', users=users)

if __name__ == '__main__':
	app.run(debug=True)
~~~

**Krok 5: Vytvorenie šablóny HTML**

Nakoniec ešte musíme vytvoriť spomínanú šablónu HTML s názvom **index.html**, ktorá zobrazí obsah našej databázy SQLite. Kedže túto šablónu Python očakáva v adresári **templates** skôr než začneme s jej ko nštrukciou musíme si tento adresár vytvoriť. Následne do neho vytvoríme prázdny súbor index.html do ktorého budeme vkladať náš kód. Môžeme tak urobiť nástrojmi VS-Code, ale aj zadaním týchto príkazov do terminálového okna:
~~~
$ mkdir templates 
$ cd templates 
$ touch index.html
~~~
>#### Pozor musíme sa však nacháchadzať v adresári do ktorého vytvárame našu aplikáciu !
~~~
# index.html

<!DOCTYPE html>
<html>
<head>
<title>SQLite Viewer Flask</title>
</head>
<body>
<h1>Users</h1>
<table>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Email</th>
	</tr>
	{% for user in users %}
		<tr>
			<td>{{ user[0] }}</td>
			<td>{{ user[1] }}</td>
			<td>{{ user[2] }}</td>
		</tr>
	{% endfor %}
</table>
</body>
</html>
~~~
Výsledkom nášho kódu je takéto zobrazenie:
![](/obrazky/SQLite03.png)

A obsah databázy si môžeme pozriet pomocou SQLite Viewera ako to ukazuje animácia na git-e:
![](/obrazky/SQLite04.gif)

