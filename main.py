from control_browser import Browser
from settings import Settings
from logging import getLogger, basicConfig, ERROR
import os
import coloredlogs

# エラーログ設定
file_path = os.path.join(os.path.dirname(__file__), "app.log")
log_format = "%(asctime)s %(name)s %(levelname)s %(message)s"
date_format = "%Y-%m-%d %I:%M:%S"
basicConfig(filename=file_path, encoding="utf-8", format=log_format, datefmt=date_format, level=ERROR)

def main():
    # ログ設定
    logger = getLogger()
    coloredlogs.install(level='INFO')

    # 設定ファイル読込
    settings = Settings()

    try:
        # 設定ファイルチェック
        settings.validate_settings()

    except ValueError as e:
        logger.error(e)
        return

    setting = settings.get_settings()

    url_dict = setting[settings.URL_DICT_KEY_NAME]

    browser = Browser()

    for key in url_dict:
        for i in range(setting[settings.ACCESS_TIMES_KEY_NAME]):
            logger.info(f"{key}: {i + 1}回目")
            try:
                # 1回目
                if i == 0:
                    browser.exec_to_quit_chrome(url_dict[key], setting[settings.FIRST_WAIT_SEC_KEY_NAME])
                else:
                    browser.exec_to_quit_chrome(url_dict[key])

            except Exception as e:
                logger.error(e)
                return


if __name__ == "__main__":
    main()