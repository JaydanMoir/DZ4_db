import sqlalchemy

class FillDatabase:
    #подключение к БД
    def connection_db(self):
        db = 'postgresql://postgres:pass@localhost:5432/DZ3_db1'
        engine = sqlalchemy.create_engine(db)
        connection = engine.connect()
        return connection

    #добавить в БД исполнителей
    def adding_perfomer(self, connection):
        artist = ['ATL', 'Feduk', 'Travis Scott', 'Max Korzh', 'Ariana Grande', 'MiyaGi & Andy Panda', 'Linkin Park', 'Rihanna']
        for i, name in enumerate(artist):
            connection.execute(f"""INSERT INTO Perfomer
            VALUES({i+1}, '{name}');
            """)
        return connection

    #добавить в БД жанры
    def adding_genre(self, connection):
        genre = ['RAP', 'ROCK', 'POP', 'HIP-HOP', 'R&B', 'Electronic music']
        for i, name in enumerate(genre):
            connection.execute(f"""INSERT INTO Genre
            VALUES({i+1}, '{name}');
            """)
        return connection

    #добавить в БД связь исполнителей с их жанрами
    def genre_perfomer(self, connection):
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(1, 1);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(1, 2);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(1, 3);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(1, 6);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(2, 7);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(3, 5);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(3, 8);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(4, 4);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(4, 2);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(5, 8);""")
        connection.execute("""INSERT INTO GenrePerfomer(genre_id, perfomer_id) VALUES(6, 1);""")
        return connection

    #добавить в БД альбомы
    def adding_album(self, connection):
        album = {'Марабу':2015, 'Лимб':2017, 'Кривой эфир':2019, 'More Love':2018, 'Фри':2016, 'Rodeo':2015, 'Astroworld':2018, 'Жить в кайф':2013, 'Малый повзрослел ч.2':2017, 'Dangerous Woman':2016, 'Hajime, pt. 3':2018, 'YAMAKASI':2020, 'One More Light':2017, 'Anti':2016}
        i=1
        for name, year in album.items():
            connection.execute(f"""INSERT INTO Album
            VALUES({i}, '{name}','{year}');
            """)
            i+=1
        return connection

    #добавить в БД связь альбомов с исполнителями
    def album_perfomer(self, connection):
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(1, 1);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(1, 2);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(1, 3);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(2, 4);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(2, 5);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(3, 6);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(3, 7);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(4, 8);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(4, 9);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(5, 10);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(6, 11);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(6, 12);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(7, 13);""")
        connection.execute("""INSERT INTO AlbumPerfomer(perfomer_id, album_id) VALUES(8, 14);""")
        return connection

    #добавить в БД треки
    def adding_track(self, connection):
        connection.execute("""INSERT INTO Track VALUES(1, 'Марабу', 2.53, 1); """)
        connection.execute("""INSERT INTO Track VALUES(2, 'Демоны', 3.53, 1); """)
        connection.execute("""INSERT INTO Track VALUES(3, 'Танцуйте', 3.40, 2); """)
        connection.execute("""INSERT INTO Track VALUES(4, 'Грустный диджей', 3.53, 3); """)
        connection.execute("""INSERT INTO Track VALUES(5, 'Woo', 3.55, 14); """)
        connection.execute("""INSERT INTO Track VALUES(6, 'One More Light', 4.15, 13); """)
        connection.execute("""INSERT INTO Track VALUES(7, 'Invisible', 3.34, 13); """)
        connection.execute("""INSERT INTO Track VALUES(8, 'Minor', 2.55, 12); """)
        connection.execute("""INSERT INTO Track VALUES(9, 'Atlant', 3.07, 12); """)
        connection.execute("""INSERT INTO Track VALUES(10, 'Колизей', 4.27, 11); """)
        connection.execute("""INSERT INTO Track VALUES(11, 'Everyday', 3.14, 10); """)
        connection.execute("""INSERT INTO Track VALUES(12, 'You', 2.59, 4); """)
        connection.execute("""INSERT INTO Track VALUES(13, 'My Time', 2.40, 5); """)
        connection.execute("""INSERT INTO Track VALUES(14, 'Oh My Dis Side', 5.51, 6); """)
        connection.execute("""INSERT INTO Track VALUES(15, 'Cant Say', 3.18, 7); """)
        connection.execute("""INSERT INTO Track VALUES(16, 'Мотылёк', 3.56, 8); """)
        connection.execute("""INSERT INTO Track VALUES(17, 'Малиновый закат', 2.57, 9); """)
        return connection

    #добавить в БД сборники
    def adding_collection(self, connection):
        collection = {'Топ 100 зарубежных песен 2019':2019, 'Лучшие новинки 2020':2020, 'Рок':2018, 'Русский рэп':2018, 'Hip-Hop':2017, 'Зарубежная музыка':2017, 'Хиты 2013':2013, 'ACIDHOUZE':2016}
        i = 1
        for name, year in collection.items():
            connection.execute(f"""INSERT INTO Collection
                    VALUES({i}, '{name}','{year}');
                    """)
            i += 1
        return connection

    #добавить связь в БД сбоников с треками
    def collection_track(self, connection):
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(15, 1);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(14, 1);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(5, 1);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(7, 1);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(8, 2);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(6, 3);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(1, 4);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(2, 4);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(3, 4);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(10, 4);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(5, 4);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(17, 5);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(13, 5);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(14, 6);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(11, 6);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(15, 6);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(7, 6);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(6, 6);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(16, 7);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(1, 8);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(2, 8);""")
        connection.execute("""INSERT INTO CollectionTrack(track_id, collection_id) VALUES(3, 8);""")
        return connection


db1 = FillDatabase()
print(db1.connection_db())
print(db1.adding_perfomer(db1.connection_db()))
print(db1.adding_genre(db1.connection_db()))
print(db1.adding_track(db1.connection_db()))
print(db1.adding_collection(db1.connection_db()))
print(db1.genre_perfomer(db1.connection_db()))
print(db1.album_perfomer(db1.connection_db()))
print(db1.collection_track(db1.connection_db()))


