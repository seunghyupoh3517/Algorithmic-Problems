-- #180. Consecutive Numbers
-- https://leetcode.com/problems/consecutive-numbers/

-- use My_db
-- CREATE TABLE Logs(Id int, Num int)

-- TRUNCATE TABLE Logs
-- insert into Logs (Id, Num) values ('1', '1')
-- insert into Logs (Id, Num) values ('2', '1')
-- insert into Logs (Id, Num) values ('3', '1')
-- insert into Logs (Id, Num) values ('4', '2')
-- insert into Logs (Id, Num) values ('5', '1')
-- insert into Logs (Id, Num) values ('6', '2')
-- insert into Logs (Id, Num) values ('7', '2')

-- join & on do not need
-- join: different rows from different tables on: different column
-- check same number occurs three times first 
SELECT DISTINCT Logs1.Num as result 
FROM Logs as Logs1, Logs as Logs2, Logs as Logs3
WHERE Logs1.Num = Logs2.Num AND Logs2.Num = Logs3.Num AND -- check if it is consecutive
Logs1.Id = Logs2.Id - 1 AND Logs2.Id = Logs3.Id - 1