create database test;

use database test;

create table customers (id SMALLINT, first_name varchar(64), last_name varchar(64));

create table campaigns (id SMALLINT, customer_id SMALLINT, name varchar(64), dt varchar(19), campaign_id SMALLINT, status varchar(64));

create table events (dt varchar(19), campaign_id SMALLINT, status varchar(64));

insert into customers (id, first_name, last_name) values (1, "Whitney", "Ferrero");
insert into customers (id, first_name, last_name) values (2, "Dickie", "Romera");

insert into campaigns (id, customer_id, name) values (1, 1, "Upton Group");
insert into campaigns (id, customer_id, name) values (2, 1, "Roob, Hudson and Rippin");
insert into campaigns (id, customer_id, name) values (3, 1, "McCullough, Rempel andLarson");
insert into campaigns (id, customer_id, name) values (4, 1, "Lang and Sons");
insert into campaigns (id, customer_id, name) values (5, 2, "Ruecker, Hand and Haley");

insert into events (dt, campaign_id, status) values ('2021-12-0213:52:00', 1, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0208:17:48', 2, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0208:18:17', 2, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0111:55:32', 3, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0106:53:16', 4, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0204:51:09', 4, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0106:34:04', 5, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0203:21:18', 5, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0103:18:24', 5, 'failure');
insert into events (dt, campaign_id, status) values ('2021-12-0215:32:37', 1, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0104:23:20', 1, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0206:53:24', 1, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0208:01:02', 2, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0115:57:19', 2, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0216:14:34', 3, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0221:56:38', 3, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0105:54:43', 4, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0217:56:45', 4, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0211:56:50', 4, 'success');
insert into events (dt, campaign_id, status) values ('2021-12-0206:08:20', 5, 'success');