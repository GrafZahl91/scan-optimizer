from pathlib import Path
import yaml

CONFIG_PATH = Path("/config/config.yaml")


class Config:
    def __init__(self):
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)


config = Config()
