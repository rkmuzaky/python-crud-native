from interface import MahasiswaAbstract
from database.db import MySQLDatabase
from entity.mahasiswa import MahasiswaEntity

class MahasiswaRepo(MahasiswaAbstract):
    def __init__(self, db: MySQLDatabase):
        self.cursor = db.cursor
        self.conn = db.connection

    def create_mahasiswa(self, mhs: MahasiswaEntity):
        query = "INSERT INTO mahasiswa values (%s, %s, %s)"
        values =(mhs.nim, mhs.name, mhs.address)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_mhs(self, nim: str):
        query = "DELETE FROM mahasiswa WHERE nim= %s"
        values = (nim,)
        self.cursor.execute(query, values)
        self.conn.commit()
    
    def update_mhs(self, nim, address: str):
        query = "UPDATE mahasiswa SET address = (%s) WHERE nim= %s"
        values = (address, nim)
        self.cursor.execute(query, values)
        self.conn.commit()