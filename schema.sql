-- Source
drop table if exists Source;
create table if not exists Source (
    idSource integer primary key autoincrement,
    nameSource text
);

-- User
drop table if exists User;
create table if not exists User (
    idUser integer primary key autoincrement,
    idStringUser text
);

-- Type
drop table if exists TypePers;
create table if not exists TypePers (
    idTypePers integer primary key autoincrement,
    nameType text
);

-- Waifu
drop table if exists Waifu;
create table if not exists Waifu (
    idWaifu integer primary key autoincrement,
    nameWaifu text,
    age integer,
    Source_idSource integer,
    User_idUser integer,
    foreign key (Source_idSource) references Source(idSource),
    foreign key (User_idUser) references User(idUser)
);

-- Alias
drop table if exists Alias;
create table if not exists Alias (
    idAlias integer primary key autoincrement,
    nameAlias text,
    Waifu_idWaifu integer,
    foreign key (Waifu_idWaifu) references Waifu(idWaifu)
);

-- Type_Waifu
drop table if exists TypePers_Waifu;
create table if not exists TypePers_Waifu (
    TypePers_idTypePers integer,
    Waifu_idWaifu integer,
    foreign key (TypePers_idTypePers) references TypePers(idTypePers),
    foreign key (Waifu_idWaifu) references Waifu(idWaifu)
);