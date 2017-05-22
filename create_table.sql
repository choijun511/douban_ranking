create database douban;
use douban;

create table ranking_list (
  id int(11) primary key auto_increment,
  title varchar(64),
  url varchar(128)
);
