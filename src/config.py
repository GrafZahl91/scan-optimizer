from pathlib import Path
import yaml


CONFIG_PATH = Path("/config/config.yaml")


class Config:

    def __init__(self):

        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, key, default=None):

        value = self.data

        for part in key.split("."):

            if not isinstance(value, dict):
                return default

            value = value.get(part)

            if value is None:
                return default

        return value


config = Config()
