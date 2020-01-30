--Assuming SQLite


/*
1)	Please aggregate the number of connections that each user has
*/


BEGIN TRANSACTION;

/* Create the table called user_connections */
CREATE TABLE user_connections(user_1 integer, user_2 integer);

/* Create few records in this table */
INSERT INTO user_connections VALUES(1,2);
INSERT INTO user_connections VALUES(1,3);
INSERT INTO user_connections VALUES(1,6);
INSERT INTO user_connections VALUES(2,1);
INSERT INTO user_connections VALUES(2,6);
INSERT INTO user_connections VALUES(2,12);
INSERT INTO user_connections VALUES(2,5);
INSERT INTO user_connections VALUES(3,1);
INSERT INTO user_connections VALUES(3,7);
INSERT INTO user_connections VALUES(3,6);
INSERT INTO user_connections VALUES(3,11);
INSERT INTO user_connections VALUES(6,1);
INSERT INTO user_connections VALUES(7,3);
INSERT INTO user_connections VALUES(12,2);
COMMIT;

/* Display all the aggregated number of connections per user from the table */
select distinct a as 'User', count(b) as 'No_Connections' from (
SELECT distinct user_1 as a, user_2 as b FROM user_connections
union
SELECT distinct user_2 as a, user_1 as b FROM user_connections
)
group by 1
order by 2 desc;



-- The users having ID 2 and 4 have the maximum number of connections.










/*
2)	How do we see how many mutual connections each pair of users have?
*/





BEGIN TRANSACTION;

/* Create the table called user_connections */
CREATE TABLE user_connections(user_1 integer, user_2 integer);

/* Create few records in this table */
INSERT INTO user_connections VALUES(1,2);
INSERT INTO user_connections VALUES(1,3);
INSERT INTO user_connections VALUES(1,6);
INSERT INTO user_connections VALUES(2,1);
INSERT INTO user_connections VALUES(2,6);
INSERT INTO user_connections VALUES(2,12);
INSERT INTO user_connections VALUES(2,5);
INSERT INTO user_connections VALUES(3,1);
INSERT INTO user_connections VALUES(3,7);
INSERT INTO user_connections VALUES(3,6);
INSERT INTO user_connections VALUES(3,11);
INSERT INTO user_connections VALUES(6,1);
INSERT INTO user_connections VALUES(7,3);
INSERT INTO user_connections VALUES(12,2);
COMMIT;

/* Display the number of mutual connections each pair of users have */

create table friendship as
select t1.a as a, t1.b as b, t2.a as c from
(select distinct a, b from (
SELECT distinct user_1 as a, user_2 as b FROM user_connections
union
SELECT distinct user_2 as a, user_1 as b FROM user_connections
)
group by 1,2) as t1
join
(select distinct a, b from 
(
SELECT distinct user_1 as a, user_2 as b FROM user_connections
union
SELECT distinct user_2 as a, user_1 as b FROM user_connections
)
group by 1,2) as t2
on t1.a = t2.b
group by 1,2,3;

select a,b, count(*) from
(select t1.* from (
(select a, b, c from friendship) t1
join
(select a, b, c from friendship) t2
on t1.a = t2.b and t1.b = t2.a and t1.c = t2.c
)
group by 1,2,3)
group by 1,2
order by 3 desc;


