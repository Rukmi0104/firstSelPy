import configparser

config_reader = configparser.RawConfigParser()
config_reader.read(r"D:\\SeleniumPython\\Projects\\FITA\\pythonProject1_FITA\\hybrid_framework\\configurations\\config.ini")


class read_config_class:
    @staticmethod
    def getURL():
        return config_reader.get("common info", "url")

    @staticmethod
    def getEmail():
        return config_reader.get("common info", "email")

    @staticmethod
    def getPassword():
        return config_reader.get("common info", "password")
