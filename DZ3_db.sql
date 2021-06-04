create table if not exists Perfomer(
	id serial primary key,
	name varchar(100) not null
);

create table if not exists Genre(
	id serial primary key,
	name varchar(100) not null unique
);

create table if not exists GenrePerfomer(
	genre_id integer references Genre(id),
	perfomer_id integer references Perfomer(id),
	constraint GenrePerfomer_pk primary key (genre_id, perfomer_id)
);

create table if not exists Album(
	id serial primary key,
	name varchar(200) not null,
	year integer not null check(year>1900 and year<=2021)
);

create table if not exists AlbumPerfomer(
	perfomer_id integer references Perfomer(id),
	album_id integer references Album(id),
	constraint AlbumPerfomer_pk primary key (perfomer_id, album_id)
);

create table if not exists Track(
	id serial primary key,
	name varchar(300) not null,
	duration numeric not null check(duration>0),
	album_id integer references Album(id)
);

create table if not exists Collection(
	id serial primary key,
	name varchar(200) not null,
	year integer not null check(year>1900 and year<=2021)
);

create table if not exists CollectionTrack(
	track_id integer references Track(id),
	collection_id integer references Collection(id),
	constraint CollectionTrack_pk primary key (track_id, collection_id)
);
