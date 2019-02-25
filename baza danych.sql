DROP TABLE oddzial;
DROP TABLE pracownik;
DROP TABLE lekarz;
DROP TABLE pacjent;
DROP TABLE test_medyczny;
DROP TABLE technik;
DROP TABLE przedmiot;
DROP TABLE zabieg;
DROP TABLE lozko;
DROP TABLE lek;
DROP TABLE wizyta;
DROP TABLE pensja;

CREATE TABLE oddzial
	(nr_oddzialu INTEGER(2) UNIQUE PRIMARY KEY,
	NAZWA CHARACTER VARYING(20) NOT NULL,
	Nr_pielegniarki CONSTRAINT nr_pielegniarki REFERENCES pracownik(nr_pracownika) NOT NULL);

CREATE TABLE pracownik
	(nr_pracownika NUMERIC(2) UNIQUE PRIMARY KEY NOT NULL,
	Imie TEXT NOT NULL,
	Nazwisko TEXT NOT NULL,
	Adres_zamieszkania TEXT NOT NULL,
	Ilosc_godzin INTEGER NOT NULL,
	nr_oddzialu CONSTRAINT nr_oddzialu REFERENCES oddzial(nr_oddzialu) NOT NULL);

CREATE TABLE lekarz
	(nr_lekarza REFERENCES pracownik(nr_pracownika) UNIQUE,
	Nr_telefonu NUMERIC(9) UNIQUE NOT NULL,
	Ordynator CONSTRAINT ordynator REFERENCES lekarz(nr_lekarza),
	Specjalnosc TEXT NULL,
	Nr_oddzialu CONSTRAINT nr_oddzialu REFERENCES oddzial(Nr_oddzialu));

CREATE TABLE pacjent
	(nr_pacjenta NUMERIC(2) UNIQUE PRIMARY KEY,
	Imie TEXT NOT NULL,
	Nazwisko TEXT NOT NULL,
	Adres TEXT NOT NULL,
	Najblizszy_krewny TEXT NULL,
	Data DATE NOT NULL,
	Nr_lekarza CONSTRAINT nr_lekarza REFERENCES lekarz(nr_lekarza),
	Nr_lozka CONSTRAINT nr_lozka REFERENCES Lozko(Nr_lozka),
	Choroba TEXT NULL,
	Sposob_opieki TEXT NOT NULL,
	Test_medyczny CONSTRAINT test_medyczny REFERENCES Test_medyczny(nr_testu) NULL,
	Nr_oddzialu NUMERIC(2));

CREATE TABLE lozko
	(Nr_lozka NUMERIC(3) UNIQUE PRIMARY KEY,
	Nr_pokoju NUMERIC(3) NOT NULL,
	Nr_oddzialu CONSTRAINT nr_oddzialu REFERENCES Nr_oddzialu(oddzial));

CREATE TABLE test_medyczny
	(nr_testu NUMERIC(3) UNIQUE PRIMARY KEY,
	nr_technika NUMERIC(2),
	data DATE NOT NULL,
	wynik_testu TEXT NOT NULL);

CREATE TABLE przedmiot
	(Nazwa TEXT NOT NULL PRIMARY KEY,
	Data DATE NOT NULL,
	Ilosc NUMERIC(2) NOT NULL,
	Koszt_1 NUMERIC(4));

CREATE TABLE technik
	(nr_pracownika CONSTRAINT nr_pracownika REFERENCES pracownik(nr_pracownika),
	nr_testu CONSTRAINT nr_testu REFERENCES test_medyczny(nr_testu));

CREATE TABLE lek
	(nazwa_leku TEXT NULL,
	Nr_pacjenta CONSTRAINT nr_pacjenta REFERENCES pacjent(nr_pacjenta));

CREATE TABLE wizyta
	(nr_lekarza CONSTRAINT nr_lekarza REFERENCES lekarz(nr_lekarza),
	nr_pacjenta CONSTRAINT nr_pacjenta REFERENCES pacjent(nr_pacjenta),
	Data DATE);

CREATE TABLE pensja
	(wysokosc NUMERIC,
	cykl_rozliczeniowy NUMERIC,
	nr_pracownika CONSTRAINT nr_pracownika REFERENCES pracownik(nr_pracownika));

CREATE TABLE zabieg
	(Nr_zabiegu NUMERIC UNIQUE PRIMARY KEY, 
	Data_leczenia DATE,
	Czas_leczenia NUMERIC,
	Wynik TEXT,	
	nr_lekarza CONSTRAINT nr_lekarza REFERENCES lekarz(nr_lekarza));


INSERT INTO oddzial VALUES (1, 'PEDIATRIA', 1);
INSERT INTO oddzial VALUES (2, 'CHIRURGIA', 2);
INSERT INTO oddzial VALUES (3, 'KARDIOLOGICZNY', 2);

INSERT INTO pracownik VALUES(1, 'Agata', 'Bylica', 'Wroc³aw, ul. Witelona 7', 5, 1);
INSERT INTO pracownik VALUES(2, 'Anna', 'Maækowska', 'Wroc³aw, ul. Piêkna 5', 10,2);
INSERT INTO pracownik VALUES(3, 'Katarzyna', 'Lalek', 'Wroc³aw, ul. Parkowa 4', 20,1);
INSERT INTO pracownik VALUES(4, 'Tomasz', 'Schmidt', 'Wroc³aw, ul. Mickiewicza 2', 20, 2);
INSERT INTO pracownik VALUES(5, 'Olek', 'Kamieñ', 'Wroc³aw, ul. Joliot-Curie 5', 40, 3);
INSERT INTO pracownik VALUES(6, 'Adam', 'Krawczyk', 'Wroc³aw, ul. Joliot-Curie 10', 40, 1);
INSERT INTO pracownik VALUES(7, 'Jolanta', 'Olczyk', 'Wroc³aw, ul. Joliot-Curie 10', 40, 2);
INSERT INTO pracownik VALUES(8, 'Daria', 'Ryba', 'Wroc³aw, ul. Joliot-Curie 10', 40, 2);
INSERT INTO pracownik VALUES(9, 'Izabela', 'Maretla', 'Wroc³aw, ul. Joliot-Curie 10', 40, 2);
INSERT INTO pracownik VALUES(10, 'Marek', 'Maj', 'Wroc³aw, ul. Joliot-Curie 10', 40, 3);
INSERT INTO pracownik VALUES(11, 'Maciej', 'Paj¹k', 'Wroc³aw, ul. Joliot-Curie 10', 40, 1);
INSERT INTO pracownik VALUES(12, 'Samuel', 'Samuel', 'Wroc³aw, ul. Joliot-Curie 10', 40, 1);
INSERT INTO pracownik VALUES(13, 'Miros³aw', 'G¹ska', 'Wroc³aw, ul. Joliot-Curie 10', 40, 1);


INSERT INTO lekarz VALUES(3, 664884444 , 3 , 'Lekarz ogólny', 1);
INSERT INTO lekarz VALUES(4, 553555363, 9 , 'Chirurg', 2);
INSERT INTO lekarz VALUES(5, 552559313, 3 , 'Kardiolog', 3);
INSERT INTO lekarz VALUES(6, 551552333, 9 , 'Lekarz ogólny', 1);
INSERT INTO lekarz VALUES(7, 554552133, 9 , 'Chirurg',2);
INSERT INTO lekarz VALUES(8, 554555333, 9 , 'Chirurg',2);
INSERT INTO lekarz VALUES(9, 554555323, 9 , 'Chirurg',2);
INSERT INTO lekarz VALUES(11, 554885313, 3 , 'Lekarz ogólny', 1);
INSERT INTO lekarz VALUES(12, 553355343, 3 , 'Lekarz ogólny', 1);
INSERT INTO lekarz VALUES(13, 573555373, 3 , 'Lekarz ogólny', 1);


INSERT INTO pacjent VALUES(1, 'Aleksandra', 'Sznajder', 'Wroc³aw, ul. Inna 2', 'Katarzyna Nowak', date('1990-10-10'), 3, 1, 'Cukrzyca','Szpital', NULL, 1);
INSERT INTO pacjent VALUES(2, 'Anna', 'Konowo³', 'Wroc³aw, ul. Sienkiewicza 5', 'Jolanta Kowalska',date('1960-10-10'), 4, 2, 'Cukrzyca', 'Szpital', NULL, 1);
INSERT INTO pacjent VALUES(3, 'Pawe³', 'Maækowski', 'Wroc³aw, ul. Piramowicza 5', 'Anna Sznajder', date('1950-10-10'), 3, 3, 'Cukrzyca','Szpital', NULL, 2);
INSERT INTO pacjent VALUES(4, 'Ma³gorzata', 'Szczodra', 'Wroc³aw, ul. Inna 2', 'Katarzyna Nowak', date('1946-10-10'), 3, 1, 'Zawa³','Szpital', NULL, 2);
INSERT INTO pacjent VALUES(5, 'Filip', 'Papier', 'Wroc³aw, ul. Inna 2', 'Katarzyna Nowak', date('1990-10-10'), 3, 1, 'Cukrzyca','Szpital', NULL, 2);
INSERT INTO pacjent VALUES(6, 'Ola', 'Królik', 'Wroc³aw, ul. Sienkiewicza 5', 'Jolanta Kowalska',date('1960-10-10'), 4, 2, 'Cukrzyca', 'Szpital', NULL, 3);


INSERT INTO lozko VALUES(1, 1, 1);
INSERT INTO lozko VALUES(2,1,1);

INSERT INTO test_medyczny VALUES(1, 5, date('2018-08-10'), 'pozytywny');
INSERT INTO test_medyczny VALUES(2, 6, date('2019-10-10'), 'negatywny');

INSERT INTO przedmiot VALUES('pielucha', date('2018-10-10'), 3, 25);
INSERT INTO przedmiot VALUES('kroplówka', date('2019-05-25'), 2, 50);

INSERT INTO technik VALUES(5,1);
INSERT INTO technik VALUES (6,2);
 
INSERT INTO lek VALUES('paracetamol', 1);
INSERT INTO lek VALUES('nospa', 2);
INSERT INTO lek VALUES('Cetol-2', 1);
INSERT INTO lek VALUES('Cetol-2', 2);

INSERT INTO wizyta VALUES(3,1, date('2015-10-10'));
INSERT INTO wizyta VALUES(4,2, date('2015-11-05'));
INSERT INTO wizyta VALUES(11,4, date('2015-10-02'));
INSERT INTO wizyta VALUES(13,2, date('2015-10-03'));
INSERT INTO wizyta VALUES(12, 1, date('2015-10-11'));
INSERT INTO wizyta VALUES(4, 4, date('2015-01-11'));
INSERT INTO wizyta VALUES(12, 1, date('2015-10-11'));
INSERT INTO wizyta VALUES(13, 4, date('2015-01-11'));
INSERT INTO wizyta VALUES(12, 4, date('2015-02-11'));
INSERT INTO wizyta VALUES(13, 3, date('2015-01-11'));


INSERT INTO pensja VALUES(5000, 1, 1);
INSERT INTO pensja VALUES(400, 4, 2);
INSERT INTO pensja VALUES(2500, 1, 3);
INSERT INTO pensja VALUES(400, 4, 4);
INSERT INTO pensja VALUES(2400, 1, 5);
INSERT INTO pensja VALUES(400, 4, 6);
INSERT INTO pensja VALUES(4000, 1, 7);
INSERT INTO pensja VALUES(3500, 1, 8);
INSERT INTO pensja VALUES(100, 1, 9);
INSERT INTO pensja VALUES(400, 4, 10);
INSERT INTO pensja VALUES(3500, 1, 11);
INSERT INTO pensja VALUES(1000, 1, 12);
INSERT INTO pensja VALUES(400, 4, 13);
