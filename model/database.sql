create database mft;

create table mft.user_tbl(
    username varchar(20) primary key ,
    password varchar(20),
    name varchar(20),
    family varchar(20),
    is_active tinyint
);
