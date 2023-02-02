# BrowserController
Chromeをシークレットモードかつヘッドレスモード(非表示)で、以下を実行します。<br>
* 指定したURLにアクセス
* 一定時間待機後、ブラウザを閉じる

URLは複数指定可能

# setting.json
* browser<br>
str: ブラウザ名(未使用)
* access_times<br>
int: アクセス回数
* first_wait_sec<br>
int: 初回待機時間(秒)
* url_dict<br>
dict: URLディクショナリ
  * (key) str: 適当な文字列
  * (val) str: URL
