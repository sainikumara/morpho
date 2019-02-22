# User stories

## Peruskäyttäjä
- Peruskäyttäjänä haluan luoda sovellukseen yksilöllisen käyttäjätunnuksen. (toteutettu)
- Peruskäyttäjänä haluan kirjautua sovellukseen sisään, jotta voin saada yksilöidyn käyttökokemuksen. (toteutettu)
- Peruskäyttäjänä haluan lisätä sovellukseen reittejä. (toteutettu)
- Peruskäyttäjänä haluan voida antaa reiteille arvosanoja ja muokata niitä. (toteutettu)
- Peruskäyttäjänä haluan nähdä, mitä arvosanoja olen itse ja mitä arvosanoja muut käyttäjät ovat antaneet reiteille. (toteutettu)
```
SELECT value FROM Rating WHERE route_id = ? AND account_id = ?;
SELECT AVG(value) FROM Rating WHERE route_id = ?;
SELECT COUNT(Rating.id) FROM Rating WHERE Rating.route_id = ?;
```
- Peruskäyttäjänä haluan syöttää sovellukseen tiedot pituudestani, painostani sekä käsieni kärkivälistä ja muokata näitä tietoja. (toteutettu)
- Peruskäyttäjänä haluan saada suosituksia reiteistä, joista ruumiinrakenteeltaan samankaltaiset käyttäjät ovat pitäneet. (toteutettu)
```
SELECT route_id, AVG(value) AS avg FROM
(SELECT * from rating WHERE NOT route_id IN
(SELECT rating.route_id from rating WHERE rating.account_id=?)
AND rater_height BETWEEN ? - 3 AND ? + 3
AND rater_weight BETWEEN ? - 3 AND ? + 3
AND rater_arm_span BETWEEN ? - 3 AND ? + 3) AS matching_ratings
GROUP BY route_id
ORDER BY avg DESC
LIMIT ?;
```


## Ylläpitäjä
- Ylläpitäjänä haluan voida poistaa reitin. (toteutettu)
- Ylläpitäjänä haluan voida poistaa käyttäjän, joka häiriköi sovelluksessa.(toteutettu)
- Ylläpitäjänä haluan voida antaa ylläpito-oikeuksia muille käyttäjille ja tarvittaessa ottaa niitä pois. (toteutettu)
- Ylläpitäjänä haluan voida poistaa asiattomina pitämiäni arvosteluja.
