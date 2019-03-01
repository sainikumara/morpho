# User stories

## Peruskäyttäjä
- Peruskäyttäjänä haluan nähdä kaikki reitit listattuna. (toteutettu)
```
SELECT * from route ORDER BY route.grade;
```
- Peruskäyttäjänä haluan luoda sovellukseen yksilöllisen käyttäjätunnuksen. (toteutettu)
```
INSERT INTO account (username, _password) VALUES ('apina', 'banaani');
```
- Peruskäyttäjänä haluan kirjautua sovellukseen sisään, jotta voin saada yksilöidyn käyttökokemuksen. (toteutettu)
- Peruskäyttäjänä haluan lisätä sovellukseen reittejä. (toteutettu)
- Peruskäyttäjänä haluan voida antaa reiteille arvosanoja ja muokata tai poistaa niitä. (toteutettu)
- Peruskäyttäjänä haluan nähdä, mitä arvosanoja olen itse ja mitä arvosanoja muut käyttäjät ovat antaneet reiteille. (toteutettu)
```
SELECT value FROM Rating WHERE route_id = 1 AND account_id = 2;
SELECT AVG(value) FROM Rating WHERE route_id = 1;
SELECT COUNT(Rating.id) FROM Rating WHERE Rating.route_id = 1;
```
- Peruskäyttäjänä haluan syöttää sovellukseen tiedot pituudestani, painostani sekä käsieni kärkivälistä ja muokata näitä tietoja. (toteutettu)
```
UPDATE account SET height = 163 WHERE account.id = 2;
UPDATE account SET weight = 55 WHERE account.id = 2;
UPDATE account SET arm_span = 160 WHERE account.id = 2;
```
- Peruskäyttäjänä haluan saada suosituksia reiteistä, joista ruumiinrakenteeltaan samankaltaiset käyttäjät ovat pitäneet. (toteutettu)
```
SELECT route.name, route.grade, COUNT(rating.value) as ratings, AVG(rating.value) AS avg FROM
route INNER JOIN rating ON route.id = rating.route_id
WHERE NOT route.id IN
(SELECT rating.route_id from rating WHERE rating.account_id = 2)
AND rater_height BETWEEN 163 - 3 AND 163 + 3
AND rater_weight BETWEEN 55 - 3 AND 55 + 3
AND rater_arm_span BETWEEN 160 - 3 AND 160 + 3
GROUP BY route.name, route.grade
ORDER BY avg DESC
LIMIT 5;
```
- peruskäyttäjänä haluan rajata suositeltuja reittejä sen mukaan, mitkä greidit kiinnostavat juuri minua. (toteutettu)
```
INSERT INTO grades_of_users (user_id, grade_id) VALUES (2, '6C');

DELETE FROM grades_of_users WHERE user_id = 2 AND grade_id = '5B';

SELECT route.name, route.grade, COUNT(rating.value) as ratings, AVG(rating.value) AS avg FROM
route INNER JOIN rating ON route.id = rating.route_id
INNER JOIN grades_of_users ON route.grade = grades_of_users.grade_id
WHERE NOT route.id IN
(SELECT rating.route_id from rating WHERE rating.account_id = 2)
AND rater_height BETWEEN 163 - 3 AND 163 + 3
AND rater_weight BETWEEN 55 - 3 AND 55 + 3
AND rater_arm_span BETWEEN 160 - 3 AND 160 + 3
AND grades_of_users.user_id = 2 
GROUP BY route.name, route.grade
ORDER BY avg DESC
LIMIT 5;
```

## Ylläpitäjä
- Ylläpitäjänä haluan voida poistaa reitin. (toteutettu)
- Ylläpitäjänä haluan nähdä listan kaikista käyttäjistä. (toteutettu)
```
SELECT * FROM account ORDER BY account.username;
```
- Ylläpitäjänä haluan voida poistaa käyttäjän, joka häiriköi sovelluksessa.(toteutettu)
- Ylläpitäjänä haluan voida antaa ylläpito-oikeuksia muille käyttäjille ja tarvittaessa ottaa niitä pois. (toteutettu)
