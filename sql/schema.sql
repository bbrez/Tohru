-- Source
create table if not exists Source (
    idSource integer primary key autoincrement,
    nameSource text unique,
    aliasSource text unique
);

-- User
create table if not exists User (
    idUser integer primary key autoincrement,
    idStringUser text
);

-- Type
create table if not exists TypePers (
    idTypePers integer primary key autoincrement,
    nameType text
);

-- Waifu
create table if not exists Waifu (
    idWaifu integer primary key autoincrement,
    -- nameWaifu text,
    -- nickWaifu text,
    qtdNames integer not null,
    preferredName integer not null,
    tierWaifu integer not null ,
    imageURLWaifu text,
    User_idUser integer,
    Source_idSource integer not null,
    foreign key (User_idUser) references User(idUser),
    foreign key (Source_idSource) references Source(idSource)
);

-- NameWaifu
create table if not exists NameWaifu (
    idNameWaifu integer primary key autoincrement,
    nameWaifu text not null,
    Waifu_idWaifu integer not null,
    foreign key (Waifu_idWaifu) references Waifu(idWaifu)
);

-- Type_Waifu
create table if not exists TypePers_Waifu (
    TypePers_idTypePers integer,
    Waifu_idWaifu integer,
    foreign key (TypePers_idTypePers) references TypePers(idTypePers),
    foreign key (Waifu_idWaifu) references Waifu(idWaifu)
);