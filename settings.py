import json
import os

class Settings():

    BROWSER_KEY_NAME = "browser"
    ACCESS_TIMES_KEY_NAME = "access_times"
    FIRST_WAIT_SEC_KEY_NAME = "first_wait_sec"
    URL_DICT_KEY_NAME = "url_dict"

    def __init__(self) -> None:
        self._settings = self.read_settings()

    def read_settings(self) -> dict:
        """設定ファイル読込"""
        file_name = "settings.json"
        file_path = os.path.join(os.path.dirname(__file__), file_name)

        try:
            with open(file_path, "r", encoding="utf-8") as read_file:
                return json.load(read_file)
        except FileNotFoundError as e:
            print(f"Error: 設定ファイル({file_name})が見つかりません")
            return {}

    def validate_settings(self) -> None:
        """設定ファイル検証"""
        setting = self._settings

        # 必要なキー
        required_keys = (self.BROWSER_KEY_NAME, self.ACCESS_TIMES_KEY_NAME, self.FIRST_WAIT_SEC_KEY_NAME, self.URL_DICT_KEY_NAME)

        # 必要なキーの存在可否確認
        missing_keys = [key for key in required_keys if key not in setting]

        if missing_keys:
            raise ValueError(f"設定ファイルに以下のパラメータが存在しません: {', '.join(missing_keys)}")

        if not setting[self.URL_DICT_KEY_NAME]:
            raise ValueError(f"設定ファイルのパラメータ'{self.URL_DICT_KEY_NAME}'に要素がありません")

        if not isinstance(setting[self.BROWSER_KEY_NAME], str):
            raise ValueError(f"設定ファイルのパラメータ'{self.BROWSER_KEY_NAME}'の値'{setting[self.BROWSER_KEY_NAME]}'が文字列ではありません")

        if not isinstance(setting[self.ACCESS_TIMES_KEY_NAME], int):
            raise ValueError(f"設定ファイルのパラメータ'{self.ACCESS_TIMES_KEY_NAME}'の値'{setting[self.ACCESS_TIMES_KEY_NAME]}'が整数ではありません")

        if not isinstance(setting[self.FIRST_WAIT_SEC_KEY_NAME], int):
            raise ValueError(f"設定ファイルのパラメータ'{self.FIRST_WAIT_SEC_KEY_NAME}'の値'{setting[self.FIRST_WAIT_SEC_KEY_NAME]}'が整数ではありません")

    def get_settings(self) -> dict:
        return self._settings
