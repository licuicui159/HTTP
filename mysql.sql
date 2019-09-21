show databases;
use database

desc [tb]
show create table [tb]
drop table [tb]

default [val] 设置默认值

insert into [tb] values(val1,val2...)
delete from [tb] where ...;

alter table book add publication_date date after price;

update book set publication_date='2004-01-07' where id=2;
update book set publication_date='2018-01-07' where id=3;
update book set publication_date='2017-01-07' where id=4;

select * from book where publication_date > (now()-interval 3 year);

select * from book order by publication_date;

select * from book order by price limit 2;

select * from book where publication like '中国%';

