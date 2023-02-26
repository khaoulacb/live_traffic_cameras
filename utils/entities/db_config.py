import yaml


class DBConfig:
    def __init__(self, db_name: str):

        yaml_path = "../config/database_config.yaml"
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        databases = data["databases"]
        database_index = next((index for (index, d) in enumerate(databases) if d["database"] == db_name), None)
        database_info = databases[database_index]

        self.host = database_info["host"]
        self.port = database_info["port"]
        self.database = database_info["database"]
        self.username = database_info["username"]
        self.password = database_info["password"]
        