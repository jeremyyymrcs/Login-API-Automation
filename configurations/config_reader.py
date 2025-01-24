import configparser

config = configparser.RawConfigParser()
config.read("..//configurations/config.ini")


class ReadConfig:

    @staticmethod
    def get_mfa_login_url():
        log_in_url = config.get("url", "mfa_login_link")
        return log_in_url

    @staticmethod
    def get_user_name():
        user_name = config.get("credentials", "user_name")
        return user_name

    @staticmethod
    def get_secret_password():
        password = config.get("credentials", "pass_word")
        return password

    @staticmethod
    def get_wrong_password():
        password = config.get("credentials", "wrong_password")
        return password

    @staticmethod
    def get_secret_key():
        password = config.get("credentials", "secret_key")
        return password
