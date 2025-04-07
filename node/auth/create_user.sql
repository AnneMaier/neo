##  1. mysql을 이용하여 user table을 생성하고 데이터를 삽입하는 sql을 작성하시오

use testdb;
drop table user;
create table user(userid char(8), passwd char(8));

show tables;
alter table user add constraint pk_userid primary key(userid);
explain user;

insert into user values('adnin', '1234');
insert into user values('moon', '1234');
insert into user values('root', '1234');

select * from user;