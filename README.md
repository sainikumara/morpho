# Morpho

Helsingin yliopiston tietojenkäsittelytieteen aineopintojen harjoitustyökurssilla Tietokantasovellus (4 op) tehtävä tietokantaa käyttävä websovellus.

Sovellus on käytettävissä Heroku-palvelussa, osoitteessa https://morphoapp.herokuapp.com/

## Kuvaus
Sovelluksen tarkoituksena on tarjota hupia ja hyötyä kiipeilyharrastukseen antamalla käyttäjälle suosituksia reiteistä, jotka voisivat olla juuri hänestä kivoja. Sovellus perustaa suosituksensa käyttäjän kokoon ja ruumiinrakenteeseen sekä muiden, kooltaan ja ruumiinrakenteeltaan samankaltaisten, käyttäjien tekemiin arvosteluihin.

## Toimintoja
- käyttäjätilin luominen
  - ylläpitäjä voi myös poistaa käyttäjiä, jotka eivät ole ylläpitäjiä, ja antaa ja poistaa ylläpito-oikeuksia
- kirjautuminen sisään ja ulos
- omien mittojen lisääminen ja muokkaus
- reitin luominen
  - ylläpitäjä ja reitin luoja voivat myös poistaa reitin
- reittien selaaminen
- reitin arvostelu, oman arvostelun muokkaus
- suositusten haku

Suosituksia muodostavaa järjestelmää voi kehittää varmasti loputtomasti, mutta aluksi lähdetään liikkeelle yksinkertaisesta konseptista.

## Dokumentaatio
- [User stories](https://github.com/sainikumara/morpho/blob/master/documentation/userstories.md)
- [Käyttöohje](https://github.com/sainikumara/morpho/blob/master/documentation/kayttoohje.md)
- [Asennusohje](https://github.com/sainikumara/morpho/blob/master/documentation/asennusohje.md)
- [CREATE TABLE -lauseet](https://github.com/sainikumara/morpho/blob/master/documentation/createtable.md)

## Tietokantakaavio
![alt text](https://github.com/sainikumara/morpho/blob/master/documentation/tietokantakaavio.png "Tietokantakaavio")
