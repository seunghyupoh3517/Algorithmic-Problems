-- #1050. Actors and Directors Who Cooperated At Least Three Times
-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

-- CREATE DATABASE My_db
-- USE My_db

-- CREATE TABLE ActorDirector (
--    actor_id int,
--    director_id int,
--    timestamp int
-- )

-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '0')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '1')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '2')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '3')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '4')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '5')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '6')

-- select * from ActorDirector

select actor_id, director_id 
from ActorDirector
GROUP BY actor_id, director_id
HAVING count(1) >= 3


-- #1083. Sales Analysis 2
-- https://leetcode.com/problems/sales-analysis-ii/

-- CREATE TABLE Product (
--    product_id int,
--    product_name varchar(10),
--    unit_price int,
--    PRIMARY KEY (product_id)
--    )
-- TRUNCATE table Product

-- insert into Product (product_id, product_name, unit_price) values('1', 'S8', '1000')
-- insert into Product (product_id, product_name, unit_price) values('2', 'G4', '800')
-- insert into Product (product_id, product_name, unit_price) values('3', 'iphone', '1400')

-- CREATE TABLE Sales  (
--   seller_id int,
--   product_id int,
--   buyer_id int,
--   sale_date date,
--   quantity int,
--   price int
--  )
-- TRUNCATE table Sales 

-- insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '1', '1', '2019-01-21', '2', '2000')
-- insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '2', '2', '2019-02-17', '1', '800')
-- insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('2', '1', '3', '2019-06-02', '1', '800')
-- insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('3', '3', '3', '2019-05-13', '2', '2800')

-- select * from Product, Sales

-- select distinct : uedto return only distinct(different) values
-- AS alias_name : gives a  table or column in table a temporary name
-- Join : used to  combine rows from two or more tables
-- ON: join columns that have different names
SELECT DISTINCT buyer_id
FROM Sales as A
Join Product as B
ON A.product_id = B.product_id
WHERE B.product_name = 'S8'
AND A.buyer_id
NOT IN (
    SELECT DISTINCT buyer_id
    FROM Sales as A
    Join Product as B
    ON A.product_id = B.product_id
    WHERE B.product_name = 'iphone'
)
-- This is basically saying selecting buyer_id of which Sales's product_id and Product's product_id of 'S8' is same
-- But not Sales's buyer_id of which product_id is same as Product's product_id of 'iphone'

