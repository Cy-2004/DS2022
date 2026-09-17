# Hands-On with SQL

Open a browser tab to https://demo.cloudbeaver.io/#/

1. Explore the MySQL database.
2. Find the tables
3. Describe tables using SQL
4. Select some rows from a table
5. Limit the select with a WHERE clause, or a LIMIT.

## CRUD Operations

### `CREATE`
```
create table nem2p_continents (
	continent_id VARCHAR(5),
	continent_name VARCHAR(30)
);
```
### `SELECT`
```
SELECT * FROM nem2p_continents;
SELECT COUNT(*) FROM nem2p_continents;
SELECT * FROM nem2p_continents WHERE continent_id = 'AS';
SELECT * FROM nem2p_continents WHERE id > 2 AND id < 4;
SELECT * FROM customer LIMIT 10;
```

### `INSERT`
```
INSERT INTO nem2p_continents (continent_id, continent_name) VALUES ('NA', 'North America');
INSERT INTO nem2p_continents (continent_id, continent_name) VALUES ('AS', 'Asia');
INSERT INTO nem2p_continents (continent_id, continent_name) VALUES ('SA', 'South America');
INSERT INTO nem2p_continents (continent_id, continent_name) VALUES ('AF', 'Africa');
INSERT INTO nem2p_continents (continent_id, continent_name) VALUES ('EU', 'Europe');
INSERT INTO nem2p_continents (continent_id, continent_name) VALUES ('OC', 'Oceania');
```
### `UPDATE`
```
UPDATE nem2p_continents SET continent_name = "Oceania and Beyond" WHERE continent_id = 'OC';
UPDATE customer SET store_id = 1 WHERE store_id IS NULL;
UPDATE customer SET store_id = 1 WHERE store_id = '';
```
### `DROP`
```
DELETE FROM nem2p_continents WHERE continent_id = 'EU';
DELETE FROM customer WHERE customer_id = '';
```

### `JOIN`
```
SELECT nem2p.first_name, nem2p.last_name, nem2p_continents.continent_name
FROM nem2p JOIN nem2p_continents 
  WHERE nem2p.continent = nem2p_continents.continent_id;
```

## Work with Mock Data

Generate mock data records from https://mockaroo.com/ and export as SQL. Be sure to include the "Create Table" option!
