# Käyttöohje

Sovellusta voi tällä hetkellä käyttää osoitteessa https://morphoapp.herokuapp.com. Lisäksi sen voi asentaa [asennusohjeen](https://github.com/sainikumara/morpho/blob/master/documentation/asennusohje.md) mukaisesti ja käyttää paikallisesti tai asentaa Herokuun itse.


## Etusivu

Sovelluksen etusivulla näkyy kirjautumattomalle käyttäjälle **suosituksena** viisi reittiä, joilla on parhaat arvostelut kaikilta käyttäjiltä.

Kirjautuneelle käyttäjälle, joka on syöttänyt sovellukseen strategiset mittansa, siinä näkyy viisi reittiä, jotka ovat saaneet parhaat arvostelut mitoiltaan samankaltaisilta muilta käyttäjiltä.

Etusivulle pääsee miltä tahansa muulta sivulta klikkaamalla sovelluksen nimeä yläpalkin vasemmassa reunassa. Yläpalkissa on linkit kaikille sovelluksen sisältösivuille sekä lisäksi kirjautumis- ja rekisteröitymissivuille.


## Rekisteröityminen

Sign up -sivulla on yksi tekstikenttä käyttäjänimen syöttämiseen ja toinen salasanan. Käyttäjänimen on oltava uniikki, joten käyttäjä näkee virheilmoituksen, jos yrittää rekisteröidä jo käytössä olevan tunnuksen. Rekisteröitymisen jälkeen käyttäjä ohjataan kirjautumissivulle.


## Kirjautuminen

Login-sivulla on tekstikenttä käyttäjänimelle ja toinen salasanalle. Jos ne eivät täsmää tietokannasta löytyvien kanssa, käyttäjä näkee virheilmoituksen.


## Kaikkien reittien listaus

List routes -sivulla on nimensä mukaisesti listattu kaikki sovellukseen syötetyt reitit, niiden greidit, arvostelujen keskiarvot ja lukumäärät. Kaikille käyttäjille näkyy näiden lisäksi **mahdollisuus antaa kullekin reitille arvosana välillä 1-5**, mutta jos kirjautumaton käyttäjä yrittää lähettää arvionsa, ohjataan hänet kirjautumissivulle.

Kirjautuneelle käyttäjälle näkyy edellisten lisäksi omassa sarakkeessaan hänen itse antamansa arvosana kullekin reitille.

Admin-oikeuksin varustetulle käyttäjälle ja reitin luojalle näkyy myös mahdollisuus **poistaa reitti** halutessaan kokonaan sovelluksesta.


## Reitin lisääminen sovellukseen

Add a route -sivulle pääsee vain kirjautunut käyttäjä, muut ohjataan kirjautumissivulle. Reitille syötetään tekstikenttään nimi ja valitaan alasvetovalikosta kuvaava greidi.


## Käyttäjän strategiset mitat

Anthropometry-sivulla rekisteröitynyt käyttäjä näkee mahdollisesti aiemmin syöttämänsä **pituuden, painon ja käsien kärkivälin** ja voi syöttää uudet. Pituus ja käsien kärkiväli syötetään kokonaisina senttimetreinä ja paino kokonaisina kilogrammoina. Jos syöte ei ole näiden sääntöjen mukainen ja muutenkin inhimillisissä rajoissa, seuraa virheilmoitus. Rekisteröitymätön käyttäjä ohjataan kirjautumissivulle.


## Käyttäjien hallinta

Admin-oikeuksin varustettu käyttäjä näkee yläpalkissa myös linkin Manage Users -sivulle, jolla on listattu kaikki sovelluksen käyttäjät ja heidän liittymispäivänsä. Tällä sivulla **admin voi jakaa ja poistaa admin-oikeuksia** ja halutessaan **poistaa käyttäjän** sovelluksesta kokonaan.
