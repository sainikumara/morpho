# Morpho

Helsingin yliopiston tietojenkäsittelytieteen aineopintojen harjoitustyökurssilla Tietokantasovellus (4 op) tehty tietokantaa käyttävä websovellus.

Sovellus on toistaiseksi alkutekijöissään, mutta se julkaistaan Heroku-palvelussa, osoitteessa https://morphoapp.herokuapp.com/

## Kuvaus
Sovelluksen tarkoituksena on tarjota hupia ja hyötyä kiipeilyharrastukseen antamalla käyttäjälle suosituksia reiteistä, jotka voisivat olla juuri hänestä kivoja. Sovellus perustaa suosituksensa käyttäjän kokoon ja ruumiinrakenteeseen sekä muiden, kooltaan ja ruumiinrakenteeltaan samankaltaisten, käyttäjien tekemiin arvosteluihin.

## Toimintoja
- käyttäjätilin luominen ja poistaminen
- kirjautuminen sisään ja ulos
- omien mittojen muokkaus
- reitin luominen
  - ylläpitäjä voi myös poistaa reitin
- reittien selaaminen (sovelluksen edistyessä selailu voi monipuolistua erilaisin kriteerein ja tägein)
- reitin arvostelu, oman arvostelun muokkaus ja poisto
  - ylläpitäjä voi myös poistaa asiattomina pitämiään arvosteluja
- suositusten haku

Suosituksia muodostavaa järjestelmää voi kehittää varmasti loputtomasti, mutta aluksi lähdetään liikkeelle yksinkertaisesta konseptista.
