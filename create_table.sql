create database douban;
use douban;

create table ranking_list (
  id int(11) primary key auto_increment,
  title varchar(64),
  url varchar(128)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into ranking_list (title, url) values ('test', 'http://test');

delete from ranking_list where title='test';
