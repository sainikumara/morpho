```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(64) NOT NULL, 
	_password VARCHAR(128) NOT NULL, 
	role VARCHAR(10) NOT NULL, 
	height INTEGER, 
	weight INTEGER, 
	arm_span INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (username)
)
```

```
CREATE TABLE route (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	grade VARCHAR(2) NOT NULL, 
	creator_account_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(creator_account_id) REFERENCES account (id)
)
```

```
CREATE TABLE rating (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	value INTEGER NOT NULL, 
	rater_height INTEGER, 
	rater_weight INTEGER, 
	rater_arm_span INTEGER, 
	route_id INTEGER NOT NULL, 
	account_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(route_id) REFERENCES route (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

```
