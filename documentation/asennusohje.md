# Sovelluksen asentaminen paikallisesti

Ohjeet toimivat Linux-käyttöjärjestelmällä. Koneessa tulee olla asennettuna python3 ja sqlite3.

## Asennus

1. Kloonaa projekti haluamaasi hakemistoon:
```
$ git@github.com:sainikumara/morpho.git
```
Tai lataa se osoitteesta https://github.com/sainikumara/morpho/ .ZIP-tiedostona ja pura se (haluamaasi hakemistoon).

2. Luo projektin hakemiston juuressa komentoriviä käyttäen Pythonin virtuaaliympäristö ja ota se käyttöön:
```
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Asenna Flask-kirjasto käyttäen pip-pakettimanageria:
```
$ pip install Flask
```

4. Asenna sovelluksen riippuvuudet:
```
$ pip install -r requirements.txt
```

5. Nyt sovellusksen voi käynnistää:
```
$ python3 run.py
```

6. Avaa selain osoitteessa http://localhost:5000/

7. Voit nyt käyttää sovellusta paikallisessa verkkoympäristössä. Syöttämäsi tiedot tallentuvat omalla koneellasi sqlite-tietokantaan.

8. Ensimmäinen luotu käyttäjätunnus saa automaattisesti admin-oikeudet sovellukseen


## Sovelluksen asentaminen Herokuun

1. Asenna sovellus paikallisesti kuten yllä

2. Luo käyttäjätunnus [Herokuun](https://www.heroku.com/), jos sinulla ei sellaista vielä ole

3. Asenna Herokun komentorivisovellus
```
$ sudo snap install heroku --classic
```

4. Kirjaudu sisään Herokuun
```
$ heroku login
```

5. Luo paikallisesti asentamasi projektin juurihakemistossa Heroku-projekti
```
$ heroku create haluamasi_nimi_projektille
```

6. Lisää paikalliseen versionhallintaan tieto Herokusta ja lähetä projekti Herokuun
```
$ git remote add heroku
$ git add .
$ git commit -m "heroku setup"
$ git push heroku master
```

7. Lisää sovelluksen käyttöön tieto siitä, että sovellus on Herokussa:
```
$ heroku config:set HEROKU=1
```

8. Lisää Herokuun PostgreSQL-tietokanta:
```
$ heroku addons:add heroku-postgresql:hobby-dev
```

9. Avaa selain osoitteessa https://haluamasi_nimi_projektille.herokuapp.com/

10. Ensimmäinen luotu käyttäjätunnus saa automaattisesti admin-oikeudet sovellukseen
