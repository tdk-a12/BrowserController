import time

import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Browser():

    # Seleniumオプション
    _options = Options()

    def __init__(self) -> None:
        # Seleniumオプション：GPU無効
        self._options.add_argument('--disable-gpu')

        # Seleniumオプション：すべての拡張機能無効
        self._options.add_argument('--disable-extensions')

        # Seleniumオプション：プロキシサーバ設定
        self._options.add_argument('--proxy-server="direct://"')

        # Seleniumオプション：プロキシバイパス設定
        self._options.add_argument('--proxy-bypass-list=*')

        # Seleniumオプション：ウィンドウ最大化で起動
        self._options.add_argument('--start-maximized')

        # Seleniumオプション：ヘッドレスモード
        self._options.add_argument('--headless')

        # Seleniumオプション：シークレットモード
        self._options.add_argument('--incognito')

    def exec_to_quit_chrome(self, url: str, second: int = 10) -> None:
        """Chromeでurlのページを開いて一定時間待機したら、開いたChromeを閉じる関数"""

        # Chrome起動
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=self._options)

        try:
            # Webページにアクセス
            driver.get(url)

            # 設定時間+0.000~2.000秒のランダムな乱数を生成する
            waitTime = float('{:.3f}'.format(np.random.rand() * 2 + second))

            # 待機
            time.sleep(waitTime)
            
        finally:
            # ドライバーで起動したブラウザを閉じる
            driver.quit()


if __name__ == "__main__":
    browser = Browser()
    browser.exec_to_quit_chrome("https://www.google.co.jp/", 3)