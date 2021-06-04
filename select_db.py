import sqlalchemy

class SelectDatabase:
    #подключение к бд
    def connection_db(self):
        db = 'postgresql://postgres:pass@localhost:5432/DZ3_db1'
        engine = sqlalchemy.create_engine(db)
        connection = engine.connect()
        return connection

    #преобразование в список без символов
    @staticmethod
    def change_list(other_list):
        new_list = []
        for el in other_list:
            new_list.append(el[0])
        return new_list

    #запрос альбомов 2018 года
    def select_album(self, connection):
        return connection.execute("""SELECT name, year FROM Album WHERE year=2018;""").fetchall()

    #самый длинный трек
    def select_max_track(self, connection):
        max_track = connection.execute("""SELECT name, duration FROM Track ORDER BY duration DESC LIMIT 1;""").fetchall()
        return {max_track[0][0]:float(max_track[0][1])}

    #треки, продолжительность которых>= 3,5
    def select_tracks(self, connection):
        tracks = connection.execute("""SELECT name FROM Track WHERE duration>=3.5;""").fetchall()
        return self.change_list(tracks)

    #сборники 2018-2020
    def select_collections(self, connection):
        collections = connection.execute("""SELECT name FROM Collection WHERE year BETWEEN 2018 AND 2020;""").fetchall()
        return self.change_list(collections)

    #исполнители с одним словом в имени
    def select_perfomer(self, connection):
        perfomers = connection.execute("""SELECT name FROM Perfomer WHERE name NOT LIKE '%% %%';""").fetchall()
        return self.change_list(perfomers)
    #треки, которые содержать мой/my в названии
    def select_track_my(self, connection):
        tracks = connection.execute("""SELECT name FROM Track WHERE name iLIKE '%%my%%' OR name iLIKE '%%мой%%';""").fetchall()
        return self.change_list(tracks)

db1 = SelectDatabase()

print(db1.select_album(db1.connection_db()),"\n")
print(db1.select_max_track(db1.connection_db()),"\n")
print(db1.select_tracks(db1.connection_db()),"\n")
print(db1.select_collections(db1.connection_db()),"\n")
print(db1.select_perfomer(db1.connection_db()),"\n")
print(db1.select_track_my(db1.connection_db()))
