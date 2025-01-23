import configparser

config = configparser.RawConfigParser()
config.read("..//configurations/config.ini")


class ReadConfig:

    @staticmethod
    def get_mfa_login_url():
        log_in_url = config.get("url", "mfa_login_link")
        return log_in_url


