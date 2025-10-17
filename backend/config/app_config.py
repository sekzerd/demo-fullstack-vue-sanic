import json

CONFIG_PATH = "./config.json"
APPX_PATH = "../../appx"
FILE_PATH = "../file"


class Config:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3000
        self.mysql_ip = "db"
        self.mysql_port = 3306
        self.user = "user"
        self.password = "password"
        self.db = "db"

    def load(self):
        try:
            raw = open(CONFIG_PATH, "r")
            obj = json.loads(raw)

            self.host = obj["host"]
            self.port = obj["port"]
            self.mysql_ip = obj["mysql_ip"]
            self.mysql_port = obj["mysql_port"]
            self.user = obj["user"]
            self.password = obj["password"]
            self.db = obj["db ="]
            return True
        except Exception as _:
            return False
