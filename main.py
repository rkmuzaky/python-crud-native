from database.db import MySQLDatabase
from repository.mahasiswa import MahasiswaRepo
from logic.mahasiswa import MahasiswaLogic
from entity.mahasiswa import MahasiswaEntity
import config

# Configuration
mysql_config = {
    "host": config.DB_HOST,
    "user": config.DB_USER,
    "password": config.DB_PASSWORD,
    "database": config.DB_DATABASE,
}

# Initialization
mysql_db = MySQLDatabase(**mysql_config)
mhs_repo = MahasiswaRepo(db=mysql_db)
mhs_logic = MahasiswaLogic(repo=mhs_repo)

# Usage
mhs = [
    MahasiswaEntity("2207013", "Rifky Khoerul Muzaky", "Samarang Pride"),
    MahasiswaEntity("2207014", "Sahil Mulahela", "Bandung"),
    ]
mhs_logic.creates(mhs)
#mhs_logic.delete("2207014")
#mhs_logic.update("2207013","Samarang")

