from tkinter import *
import sqlite3
try:
    db = sqlite3.connect('baza.db')
    cursor=db.cursor()
except Exception:
    print("Nieprawidłowe dane")

# interface
root = Tk()
root.title("Baza danych Selly Oak Clinic")

window = Frame(root)
window.pack(side=TOP)

frame1=Frame(window)
frame1.pack(side=TOP)

frame2=Frame(window, width=100, height=60) #górny lewy róg
frame2.pack(side=TOP)

frame5=Frame(window, width=100, height=60) #górny prawy róg
frame5.pack(side=RIGHT)

podramka5=Frame(frame5) #podział prawej górnej strony
podramka5.pack(side=LEFT)

podramka25=Frame(frame5) #Podział prawej strony
podramka25.pack(side=RIGHT)

window2 = Frame(root)
window2.pack(side=BOTTOM)

podramka3=Frame(root)
podramka3.pack(side=LEFT)

frame3 = Frame(root, width=10000, height=6000) #lewy dolny róg
frame3.pack(side=LEFT)
Label(frame3, text="").pack()

frame4 = Frame(root, width=600, height=200) #prawy dolny róg
frame4.pack(side=RIGHT)

podramka3=Frame(frame3)
podramka3.pack(side=RIGHT)

#wyświetlanie wyników z zapytań

def akcja():
    print("Wykonanie pierwszej akcji")

def dodawaniedooddzialow():
    global e1, e2, e3, e4
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()

    Label(frame4, text="Nr oddziału").grid(row=0)
    Label(frame4, text="Nazwa oddziału").grid(row=1)
    Label(frame4, text="Nr pielegniarki").grid(row=2)
    e1=IntVar()

    e1 = Entry(frame4)
    e1.grid(row=0, column=1)
    e2 = Entry(frame4)
    e2.grid(row=1, column=1)
    e3 = Entry(frame4)
    e3.grid(row=2, column=1)

    b=Button(frame4, text="Dodaj do tabeli", command=wstawianieoddzialow)
    b.grid(row=3, column=1)

    cursor.execute('''SELECT * FROM oddzial''')
    a=cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Aktualne pozycje w tabeli:").pack()
    Label(frame3, text="Nr oddziału | Nazwa | Nr pielęgniarki").pack()
    listbox = Listbox(frame3, height=15, width=100)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

def wstawianieoddzialow():
    nr_oddzialu = e1.get()
    nazwa_oddzialu = e2.get()
    nr_pielegniarki = e3.get()
    try:
        with db:
            cursor.execute('''INSERT INTO oddzial VALUES(?, ?, ?)''',
                           (nr_oddzialu, nazwa_oddzialu, nr_pielegniarki))
            db.commit()
            print("Wszystko ok, dodano do tabeli oddziałów")
    except sqlite3.IntegrityError:
        print("Nie udało się dodać do tabeli - naruszona integralność")

    dodawaniedooddzialow()


def dodawaniepracownikow():
    global e1, e2, e3, e4, e5, e6
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame4, text="Dodaj do tabeli:").grid(row=0)
    Label(frame4, text="Nr pracownika").grid(row=1)
    Label(frame4, text="Imię").grid(row=2)
    Label(frame4, text="Nazwisko").grid(row=3)
    Label(frame4, text="Adres zamieszkania").grid(row=4)
    Label(frame4, text="Ilość godzin").grid(row=5)
    Label(frame4, text="Nr oddziału").grid(row=6)

    e1 = Entry(frame4)
    e1.grid(row=1, column=1)
    e2 = Entry(frame4)
    e2.grid(row=2, column=1)
    e3 = Entry(frame4)
    e3.grid(row=3, column=1)
    e4 = Entry(frame4)
    e4.grid(row=4, column=1)
    e5 = Entry(frame4)
    e5.grid(row=5, column=1)
    e6 = Entry(frame4)
    e6.grid(row=6, column=1)

    b = Button(frame4, text="Dodaj do tabeli", command=wstawianiepracownikow)
    b.grid(row=7, column=1)
    cursor.execute('''SELECT * FROM pracownik''')

    a=cursor.fetchall()

    Label(frame3, text="").pack()
    Label(frame3, text="Aktualne pozycje w tabeli:").pack()
    Label(frame3, text="Nr pracownika | Imię | Nazwisko | Adres | Ilość godzin | Nr oddziału").pack()
    listbox = Listbox(frame3, height=15, width=100)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)


def wstawianiepracownikow():
    nr_pracownika = e1.get()
    imie = e2.get()
    nazwisko = e3.get()
    adres = e4.get()
    godziny = e5.get()
    nr_oddzialu= e6.get()
    try:
        with db:
            db.execute('''INSERT INTO pracownik VALUES(?, ?, ?, ?, ?, ?)''',
                           (nr_pracownika, imie, nazwisko, adres, godziny, nr_oddzialu))
            db.commit()
            print("Wszystko ok, dodano do tabeli pracowników")
    except sqlite3.IntegrityError:
        print("Nie udało się dodać do tabeli - naruszona integralność")

    cursor.execute('''SELECT * FROM pracownik''')

    dodawaniepracownikow()

def dodanielekarzy():
    global e1, e2, e3, e4, e5
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame4, text="Dodaj do tabeli:").grid(row=0)
    Label(frame4, text="Nr lekarza").grid(row=1)
    Label(frame4, text="Nr telefonu").grid(row=2)
    Label(frame4, text="Specjalność").grid(row=3)
    Label(frame4, text="Ordynator").grid(row=4)
    Label(frame4, text="Nr oddziału").grid(row=5)

    e1 = Entry(frame4)
    e1.grid(row=1, column=1)
    e2 = Entry(frame4)
    e2.grid(row=2, column=1)
    e3 = Entry(frame4)
    e3.grid(row=3, column=1)
    e4 = Entry(frame4)
    e4.grid(row=4, column=1)
    e5 = Entry(frame4)
    e5.grid(row=5, column=1)
    b = Button(frame4, text="Dodaj do tabeli", command=wstawianielekarzy)
    b.grid(row=6, column=1)

    cursor.execute('''SELECT * FROM lekarz''')
    a=cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Aktualne pozycje w tabeli:").pack()
    Label(frame3, text="Nr lekarza | Nr telefonu | Specjalność | Ordynator | Nr oddziału").pack()
    listbox = Listbox(frame3, height=15, width=100)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

def wstawianielekarzy():
    nr_lekarza = e1.get()
    nr_telefonu = e2.get()
    specjalnosc = e3.get()
    ordynator = e4.get()
    nr_oddzialu= e5.get()
    try:
        with db:
            cursor.execute('''INSERT INTO lekarz VALUES(?, ?, ?, ?, ?)''',
                           (nr_lekarza, nr_telefonu, specjalnosc, ordynator, nr_oddzialu))
            print("Wszystko ok, dodano do tabeli pracowników")
    except sqlite3.IntegrityError:
        print("Nie udało się dodać do tabeli")
    db.commit()

    cursor.execute('''SELECT * FROM pracownik''')
    a=cursor.fetchall()

    dodanielekarzy()

def dodaniepacjentow():
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame4, text="Nr pacjenta").grid(row=0)
    Label(frame4, text="Imię").grid(row=1)
    Label(frame4, text="Nazwisko").grid(row=2)
    Label(frame4, text="Adres").grid(row=3)
    Label(frame4, text="Najbliższy krewny").grid(row=4)
    Label(frame4, text="Data urodzenia").grid(row=5)
    Label(frame4, text="Nr lekarza").grid(row=6)
    Label(frame4, text="Nr łóżka").grid(row=7)
    Label(frame4, text="Choroba").grid(row=8)
    Label(frame4, text="Sposób opieki").grid(row=9)
    Label(frame4, text="Testy medyczny").grid(row=10)
    Label(frame4, text="Nr oddziału").grid(row=11)

    e1 = Entry(frame4)
    e1.grid(row=0, column=1)
    e2 = Entry(frame4)
    e2.grid(row=1, column=1)
    e3 = Entry(frame4)
    e3.grid(row=2, column=1)
    e4 = Entry(frame4)
    e4.grid(row=3, column=1)
    e5 = Entry(frame4)
    e5.grid(row=4, column=1)
    e6 = Entry(frame4)
    e6.grid(row=5, column=1)
    e7 = Entry(frame4)
    e7.grid(row=6, column=1)
    e8 = Entry(frame4)
    e8.grid(row=7, column=1)
    e9 = Entry(frame4)
    e9.grid(row=8, column=1)
    e10 = Entry(frame4)
    e10.grid(row=9, column=1)
    e11 = Entry(frame4)
    e11.grid(row=10, column=1)
    e11 = Entry(frame4)
    e11.grid(row=11, column=1)

    b = Button(frame4, text="Dodaj do tabeli", command=wstawianiepacjentow)
    b.grid(row=12, column=1)
    cursor.execute('''SELECT * FROM pacjent''')
    a=cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Aktualne pozycje w tabeli:").pack()
    Label(frame3, text="Nr_pacjenta|Imię|Nazwisko|Adres|Krewny|Data|Nr_lekarza|Nr_lozka|Choroba|Sposob opieki|Testy|Oddział").pack()
    listbox = Listbox(frame3, height=15, width=100)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)



def wstawianiepacjentow():
    nr_pacjenta = e1.get()
    imie = e2.get()
    nazwisko = e3.get()
    adres = e4.get()
    krewny = e5.get()
    data= e6.get()
    nr_lekarza = e7.get()
    nr_lozka =e8.get()
    choroba=e9.get()
    sposobopieki=e10.get()
    testy=e11.get()
    oddzial=e12.get()
    try:
        with db:
            cursor.execute('''INSERT INTO pacjent VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nr_pacjenta, imie, nazwisko, adres, krewny, data, nr_lekarza, nr_lozka, choroba, sposobopieki, testy, oddzial))
            db.commit()
            print("Wszystko ok, dodano do tabeli pracowników")

    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    cursor.execute('''SELECT * FROM pacjent''')
    a = cursor.fetchall()
    Label(frame3, text="Aktualne pozycje w tabeli:").pack()
    Label(frame3, text="Nr_pacjenta, Imię, Nazwisko, Adres, Krewny, Nr_lekarza, Nr_lozka, Choroba, Sposob opieki, Testy, Oddział").pack()
    for row in a:
        Label(frame3, text=row).pack()
    dodaniepacjentow()

def przykladowe():
    s = e1.get()
    print(s)

#zapytania z zad 5
def zad1():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''
 Select nazwisko, pacjent.Data from pacjent join lek on (pacjent.nr_pacjenta=lek.Nr_pacjenta)  join wizyta on (pacjent.nr_pacjenta=wizyta.nr_pacjenta) 
 join lekarz on (wizyta.nr_lekarza=lekarz.nr_lekarza) where choroba="Cukrzyca" AND  nazwa_leku="Cetol-2" 
 group by pacjent.nr_pacjenta having count(wizyta.nr_pacjenta )>0 AND lekarz.Nr_oddzialu=1; ''')
            db.commit()
            print("Wyświetlono")

    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()

    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="1.").pack()
    Label(frame4, text="Select nazwisko, pacjent.Data from pacjent \n"
                       " join lek on (pacjent.nr_pacjenta=lek.Nr_pacjenta) \n "
                       " join wizyta on (pacjent.nr_pacjenta=wizyta.nr_pacjenta) \n"
                       "where choroba=”Cukrzyca” AND  nazwa_leku=”Cetol-2” \n"
                       " group by pacjent.nr_pacjenta having \n"
                       "count(wizyta.nr_pacjenta)>0 AND lekarz.Nr_oddzialu=1;").pack()


def zad2():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''
            select pacjent.nazwisko from pacjent join wizyta on (pacjent.nr_pacjenta=wizyta.nr_pacjenta)
             join lekarz on (wizyta.nr_lekarza=lekarz.nr_lekarza) join pracownik on (pracownik.nr_pracownika=lekarz.nr_lekarza)
              where pracownik.Nazwisko="Pająk" Or  pracownik.Nazwisko="Samuel" Or pracownik.Nazwisko="Gąska" group by pacjent.nr_pacjenta
               having count(wizyta.nr_pacjenta)>0 order by pacjent.nazwisko ASC; ''')
            db.commit()
            print("Wyświetlono")

    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()
    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="2.").pack()
    Label(frame4, text="select pacjent.nazwisko from pacjent join wizyta \n"
                       " on (pacjent.nr_pacjenta=wizyta.nr_pacjenta) \n"
                       "join lekarz on (wizyta.nr_lekarza=lekarz.nr_lekarza) \n"
                       " join pracownik on \n"
                       "(pracownik.nr_pracownika=lekarz.nr_lekarza) \n"
                       "where pracownik.Nazwisko=”Pająk” Or \n "
                       "pracownik.Nazwisko=”Samuel” Or \n"
                       "pracownik.Nazwisko=”Gąska” \n "
                       "group by pacjent.nr_pacjenta having \n"
                       "count(wizyta.nr_pacjenta)>0 \n"
                       "order by pacjent.nazwisko ASC;").pack()

def zad3():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''Select count(*) from pacjent join wizyta on (wizyta.nr_pacjenta=pacjent.nr_pacjenta)
             join lekarz on (wizyta.nr_lekarza=lekarz.nr_lekarza) where substr(pacjent.Nazwisko, 1,1)="S" AND lekarz.Nr_oddzialu=1 
             group by wizyta.nr_lekarza having (count(wizyta.nr_lekarza)>2); 
            ''')
            db.commit()
            print("Wyświetlono")

    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()
    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="3.").pack()
    Label(frame4, text="Select count(*) from pacjent join wizyta on \n"
                       "(wizyta.nr_pacjenta=pacjent.nr_pacjenta) \n"
                       " join lekarz on (wizyta.nr_lekarza=lekarz.nr_lekarza) \n"
                       " where substr(pacjent.Nazwisko, 1,1)=”S” \n "
                       "group by wizyta.nr_lekarza having \n"
                       "count(wizyta.nr_pacjenta)>2 AND lekarz.Nr_oddzialu=1;").pack()

def zad4():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''
            select imie from wizyta JOIN pracownik ON (pracownik.nr_pracownika=wizyta.nr_lekarza) where (strftime('%Y', Data) = '2015') group by pracownik.nr_pracownika order by count(wizyta.nr_lekarza) ASC limit 1;
            ''')
            db.commit()
            print("Wyświetlono")

    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="4.").pack()
    Label(frame4, text="select imie from wizyta JOIN pracownik ON \n"
                       " (pracownik.nr_pracownika=wizyta.nr_lekarza) where \n "
                       "(strftime('%Y', Data) = '2015') \n"
                       " group by pracownik.nr_pracownika \n "
                       "order by count(wizyta.nr_lekarza) \n ASC limit 1 ;").pack()

def zad5():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''
            Select nazwisko, round(wysokosc*1.15, 0) from pracownik JOIN pensja ON (pracownik.nr_pracownika=pensja.nr_pracownika);''')
            db.commit()
            print("Wyświetlono")
    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame4, text="5.").pack()

    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="Select nazwisko, round(wysokosc*1.15, 0) from pracownik \n  JOIN pensja ON (pracownik.nr_pracownika=pensja.nr_pracownika);").pack()

def zad6():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''SELECT nazwisko,
CASE WHEN lekarz.nr_lekarza=lekarz.Ordynator  THEN '***'
ELSE cast(pensja.wysokosc as charakter(10))
END as placa
From pracownik JOIN pensja ON (pracownik.nr_pracownika=pensja.nr_pracownika) JOIN lekarz ON (pracownik.nr_pracownika=lekarz.nr_lekarza);''')
            db.commit()
            print("Wyświetlono")

    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="SELECT nazwisko, \n CASE WHEN lekarz.nr_lekarza=lekarz.Ordynator  \n"
                       " THEN ''***'' ELSE cast(pensja.wysokosc as charakter(10)) \n "
                       "END as placa From pracownik JOIN pensja ON \n "
                       "(pracownik.nr_pracownika=pensja.nr_pracownika) \n"
                       " JOIN lekarz ON (pracownik.nr_pracownika=lekarz.nr_lekarza);").pack()


def zad7():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''SELECT NAZWA, COUNT(*) FROM oddzial JOIN pracownik ON (oddzial.nr_oddzialu=pracownik.nr_oddzialu) GROUP BY NAZWA;''')
            db.commit()
            print("Wyświetlono")

    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="7.").pack()
    Label(frame4, text="SELECT NAZWA, COUNT(*)FROM oddzial \n"
                       " JOIN pracownik ON (oddzial.nr_oddzialu=pracownik.nr_oddzialu) \n GROUP BY NAZWA);").pack()


def zad8():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute(''' SELECT Nazwisko, Specjalnosc from pracownik JOIN pensja ON (pracownik.nr_pracownika=pensja.nr_pracownika) JOIN lekarz ON(pracownik.nr_pracownika=lekarz.nr_lekarza) where (pensja.wysokosc*pensja.cykl_rozliczeniowy)<(SELECT 0.5*pensja.wysokosc*pensja.cykl_rozliczeniowy from pracownik JOIN pensja ON (pracownik.nr_pracownika=pensja.nr_pracownika) JOIN lekarz ON(pracownik.nr_pracownika=lekarz.nr_lekarza)  GROUP BY lekarz.Ordynator); ''')
            db.commit()
            print("Wyświetlono")
    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame4, text="8.").pack()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="SELECT Nazwisko, Specjalnosc from pracownik JOIN \n "
                       "pensja ON (pracownik.nr_pracownika=pensja.nr_pracownika) JOIN lekarz \n"
                       " ON(pracownik.nr_pracownika=lekarz.nr_lekarza) where \n"
                       "(pensja.wysokosc*pensja.cykl_rozliczeniowy)< \n"
                       "(SELECT 0.5*pensja.wysokosc*pensja.cykl_rozliczeniowy from pracownik \n"
                       " JOIN pensja ON (pracownik.nr_pracownika=pensja.nr_pracownika) \n "
                       "JOIN lekarz ON(pracownik.nr_pracownika=lekarz.nr_lekarza) \n "
                       " GROUP BY lekarz.Ordynator) ;").pack()


def zad9():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute('''Select nazwa, count(pacjent.nr_pacjenta) as PacjenciCount from pacjent inner join oddzial on pacjent.nr_oddzialu=oddzial.nr_oddzialu group by pacjent.nr_oddzialu having  PacjenciCount >((select count(*) from pacjent) * 1.0 / (select count(*) from oddzial) * 1.0); ''')
            db.commit()
            print("Wyświetlono")
    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame4, text="9.").pack()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)

    Label(frame4, text="Select nazwa, count(pacjent.nr_pacjenta) as PacjenciCount \n from pacjent "
                       "\n inner join oddzial on pacjent.nr_oddzialu=oddzial.nr_oddzialu \n group by pacjent.nr_"
                       " oddzialu having \n PacjenciCount >((select count(*) from pacjent) \n"
                       " * 1.0 / (select count(*) from oddzial) * 1.0);").pack()

def zad10():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    try:
        with db:
            cursor.execute(''' 
             SELECT NAZWA from pracownik join pensja on (pracownik.nr_pracownika=pensja.nr_pracownika) 
             join oddzial on (pracownik.nr_oddzialu=oddzial.nr_oddzialu) group by oddzial.nr_oddzialu 
             order by sum(pensja.wysokosc*pensja.cykl_rozliczeniowy) DESC limit 1; ''')
            db.commit()
            print("Wyświetlono")
    except sqlite3.IntegrityError:
        print("Nie można dodać do tabeli")

    a = cursor.fetchall()
    Label(frame3, text="").pack()
    Label(frame3, text="Wynik").pack()
    listbox = Listbox(frame3, height=15, width=40)
    listbox.pack()

    for item in a:
        listbox.insert(END, item)
    Label(frame4, text="10.").pack()

    Label(frame4,
          text="SELECT NAZWA from pracownik join pensja on \n (pracownik.nr_pracownika=pensja.nr_pracownika) \n  "
               "join oddzial on (pracownik.nr_oddzialu=oddzial.nr_oddzialu) \n group by oddzial.nr_oddzialu order by \n sum(pensja.wysokosc*pensja.cykl_rozliczeniowy) DESC limit 1;").pack()




#interface
#zakładka Wyświetl bazę danych
#zakładka Wyświetl zapytania

def wyswietlbazedanych():
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in podramka5.winfo_children():
        widget.destroy()
    for widget in podramka25.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in podramka25.winfo_children():
        widget.destroy()
    for widget in podramka5.winfo_children():
        widget.destroy()
    b1 = Button(frame2, text="Wyświetl oddziały",command=dodawaniedooddzialow)
    b2 = Button(frame2, text="Wyświetl pracowników",  command=dodawaniepracownikow)
    b3 = Button(frame2, text="Wyświetl lekarzy", command=dodanielekarzy)
    b4 = Button(frame2, text="Wyświetl pacjentów", command=dodaniepacjentow)
    button=(b1, b2, b3, b4)
    for b in button:
        b.pack(side=LEFT)
    Label(frame2, text="")

def zadanie5():
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame4.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    for widget in podramka25.winfo_children():
        widget.destroy()
    for widget in podramka5.winfo_children():
        widget.destroy()


    bu1 = Button(frame2, text="1.Wyświetl nazwiska i daty urodzenia\n osób, które zażywały Cetol-2, cierpią \nna cukrzyce oraz odbyli przynamniej\n jedną wizytę u lekarza pediatrii ", command=zad1)
    bu2 = Button(frame2, text="2.Wyświetl nazwiska pacjentów, którzy \nodwiedzili przynajmniej jednego lekarza \nogólnego: Dr Pająk, Dr Samuel, Dr Gąska",  justify=RIGHT, command=zad2)
    bu3 = Button(frame2, text="3.Wyświetl liczbę pacjentów, których \nnazwisko zaczyna się na literę S oraz \nodbyli więcej niż 2 wizyty u lekarza ogólnego", command=zad3)
    bu4 = Button(frame2, text="4.Wyświetl imię lekarza, który miał \nnajmniej wizyt pacjentów w 2015 roku", command=zad4)
    bu5 = Button(frame2, text="5.Wyświetl nazwiska i stawki godzinowe \npowiększone o 15% dla pracowników z pensją \nnaliczaną godzinowo (zaokrąglone)", command=zad5)
    bu6 = Button(frame2, text="6.Wyświetl wartość płacy podstawowej dla\npracowników pełnoetatowych - oprócz \nordynatora",command=zad6)
    bu7 = Button(frame2, text="7.Wyświetl liczbę zatrudnionych dla \nkażdego oddziału", command=zad7)
    bu8 = Button(frame2, text="8.Wyświetl nazwiska i etaty pracowników, \nktórych rzeczywiste zarobki nie przekraczają\n 50% ich szefów", command=zad8)
    bu9 = Button(frame2, text="9.Wyświetl nazwę oddziału i liczbę pacjentów, \nw których ilość pacjentów przekracza\n średnią ilość pacjentów na oddział", command=zad9)
    bu10 = Button(frame2, text="10.Wyświetl nazwę oddziału wypłacającego \npracownikom ze stałą pensją najwięcej pieniędzy",command=zad10)

    bu1.grid(row=0)
    bu2.grid(row=1)
    bu3.grid(row=2)
    bu4.grid(row=3)
    bu5.grid(row=4)
    bu6.grid(row=0, column=1)
    bu7.grid(row=1, column=1)
    bu8.grid(row=2, column=1)
    bu9.grid(row=3, column=1)
    bu10.grid(row=4, column=1)

    Label(podramka5, text="").pack()
    Label(podramka25, text="").pack()
    Label(podramka5, text="").pack()
    Label(podramka25, text="").pack()

button1 = Button(frame1, text="Przeglądaj bazę danych", command=wyswietlbazedanych)
button1.grid(row=0, column=0)

button2= Button(frame1, text="Przeglądaj zapytania", command=zadanie5)
button2.grid(row=0, column=1)
Label(frame1, text="_________________________").grid(row=1)
Label(frame1, text="_________________________").grid(row=1, column=1)


mainloop()
db.close()