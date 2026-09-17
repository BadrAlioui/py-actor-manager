import sqlite3

from app.models import Actor

# add manager here


class ActorManager:
    def __init__(self, db_name, table_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.db = db_name
        self.table = table_name

    def create(self, first_name, last_name):
        self.cursor.execute(
            "INSERT INTO actors (first_name, last_name) VALUES (?,?)",
            (first_name, last_name),
        )
        self.connection.commit()

    def all(self):
        self.cursor.execute("SELECT * FROM actors")
        rows = self.cursor.fetchall()
        actors = []
        for row in rows:
            actors.append(Actor(row[0], row[1], row[2]))
        return actors

    def update(self, pk, new_first_name, new_last_name):
        self.cursor.execute(
            "UPDATE actors SET first_name = ?, last_name = ? WHERE id=?",
            (new_first_name, new_last_name, pk),
        )
        self.connection.commit()

    def delete(self, pk):
        self.cursor.execute("DELETE FROM actors WHERE id=?", (pk,))
        self.connection.commit()
