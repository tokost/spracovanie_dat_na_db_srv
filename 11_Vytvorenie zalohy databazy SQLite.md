># Ako vytvoriť tabuľku a zálohu databázy SQLite pomocou Pythonu?

## Vytvorenie tabuľky
V tomto článku sa naučíme, ako vytvoriť zálohu databázy SQLite pomocou Pythonu. Na vytvorenie zálohy databázy SQLite pomocou Pythonu sú požadované moduly SQLite3 a IO .

Najprv vytvorte pôvodnú databázu, aby ste to urobili podľa nižšie uvedeného programu:
~~~
import sqlite3
import io
from sqlite3 import Error


def SQLite_connection():
	
	try:	
		conn = sqlite3.connect('Originaldatabase.db')
		print("Connection is established successfully!")
		print("'originaldatabase.db' is created ")
		return conn
		
	except Error:
		print(Error)
		
	finally:
		conn.close()

SQLite_connection()
~~~
Výsledkom bude oznámenie:
![](/obrazky/sqlite_zal01.png)

Pôvodnná databáza v pamäti bude uložená napr. tu:
![](/obrazky/sqlite_zal02.png)

Následne vytvoríme študentskú tabuľku v pôvodnej databáze. Spustíme syntax SQLite na vytvorenie tabuľky v objekte kurzora.

~~~
kurzor_objekt = conn.cursor()

 kurzor_object.execute(“CREATE TABLE Name Table()”)
~~~
Ak použijeme túto syntax, tak kompletný program na vytvorenie tabuľky študentov v pôvodnej databáze bude:
~~~
import sqlite3
import io
from sqlite3 import Error

def sql_connection():
	try:
		conn = sqlite3.connect('Originaldatabase.db')
		return conn
	except Error:
		print(Error)

def sql_table(conn):
	
	cursor_object = conn.cursor()
	cursor_object.execute(
		"CREATE TABLE student(roll_no integer PRIMARY KEY,first_name text,\
		last_name text, class text, stream text,address text)")
	conn.commit()

conn = sql_connection()
sql_table(conn)
~~~
Ak chcete skontrolovať, či je naša tabuľka vytvorená, môžeme použiť prehliadač DB pre SQLite na zobrazenie našej tabuľky. Otvorte súbor „originaldatabase.db“ s programom a mali by sme vidieť našu tabuľku:

![](/obrazky/sqlite_zal03.png)

## Vytvorenie zálohy databázy
Vytvoríme zálohu databázy. Aby sme to urobili, zavoláme funkciu **open()** z IO modulu. Táto funkcia poskytne celkový počet riadkov databázy, ktoré budú upravené, vložené alebo vymazané od otvorenia pripojenia k databáze. Tiež použijeme funkciu **iterdump()** . V textovom formáte SQL poskytuje funkcia iterdump() iterátor na výpis databázy. Ktorý sa používa na uloženie databázy v pamäti pre neskoršie obnovenie. V prostredí sqlite3 poskytuje táto funkcia rovnaké možnosti ako príkaz **.dump** .

**Syntax:**
~~~
with io.open('backupdatabase.sql', 'w') as p:
  for line in conn.iterdump():
      p.write('%s\n' % line)
~~~
Podľa danej syntaxe bude záloha úspešne vykonaná a dáta budú uložené ako **backupdatabase_dump.sql** .
~~~
import sqlite3
import io
conn = sqlite3.connect('Originaldatabase.db')

# Open() function
with io.open('backupdatabase_dump.sql', 'w') as p:
		
	# iterdump() function
	for line in conn.iterdump():
		
		p.write('%s\n' % line)
	
print(' Backup performed successfully!')
print(' Data Saved as backupdatabase_dump.sql')

conn.close()
~~~
Výsledkom bude oznámenie takéhoto obsahu:
![](/obrazky/sqlite_zal04.png)

a záloha sa bude nachádzať napr. tu:
![](/obrazky/sqlite_zal05.png)

Keď sa pozrieme na obsah súboru .sql ktorý je tzv. **backup**-om našej SQLite viewer-om vidíme zoznam príkazov jazyka SQL. Jeho obnovenie tzv. **restore** do pôvodnej formy sa uskutoční príkazom shellu danej databázy ktorý je v našom prípade sqlite3. Tento shell musíme mať najprv ako balík nástrojov nainštalovaný z [sqlite stránky](https://www.sqlite.org/download.htmlv+sak )
Restore alebo Import údajov zo súborov SQL
Po použití .dump príkazu vo sqlite3 výzve na export vašej databázy SQLite ako súboru SQL môžete obnoviť stav databázy vložením súboru SQL späť sqlite3pomocou .read príkazu.

Pred použitím .read príkazu musíte zadať sqlite3 informáciu o tom v ktorom adresári sa má restore súbor vytvoriť a ako sa bude volať spolu s prípanou (db, .sqlite, .sqlite3, .db3, .s3db, .sl3):
~~~
sqlite3 ./restore.db
~~~
Teraz môžete importovať údaje zo súborov SQL [takto](https://www.prisma.io/dataguide/sqlite/importing-and-exporting-data-in-sqlite):
~~~
.read ./backup.sql
.exit
~~~
![](/obrazky/sqlite_zal06.png)