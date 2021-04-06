-- Source
drop table if exists Source;
create table if not exists Source (
    idSource integer primary key autoincrement,
    nameSource text unique
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
    preferredName integer,
    age integer,
    User_idUser integer,
    Source_idSource integer not null,
    foreign key (User_idUser) references User(idUser),
    foreign key (Source_idSource) references Source(idSource),
    foreign key (preferredName) references WaifuName(idWaifuName)
);

-- Alias
drop table if exists WaifuName;
create table if not exists WaifuName (
    idWaifuName integer primary key autoincrement,
    nameWaifuName text,
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