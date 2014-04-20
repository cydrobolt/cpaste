drop table if exists pastes;
create table pastes (
  id integer primary key autoincrement,
  title text not null,
  paste text not null,
  timestamp text not null,
  lang text not null,
  baseid text not null
);