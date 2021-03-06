# *************************
# 型と内容の確認
# *************************
def typrint(obj):
    print(type(obj))
    print(obj)
    print("")

# *************************
# ライブラリ
# *************************
# import ssl
import smtplib
from email.mime.text import MIMEText
import datetime
from  email.charset import Charset

# *************************
# 日付のテスト
# *************************
# 日付だけ欲しい場合はこちら
today = datetime.date.today()
typrint(today)

# datetime オブジェクトは date オブジェクトおよび time オブジェクトの全ての情報が入っている単一のオブジェクトです。
today = datetime.datetime.today()
typrint(today)

# 書式 : https://docs.python.jp/3/library/datetime.html#strftime-strptime-behavior
strdate = today.strftime("%Y-%m-%d %H:%M:%S")
typrint(strdate)

# *************************
# メール用キャラクタセット
# *************************
jis='iso-2022-jp'

# *************************
# 本文
# *************************
text = "Python\n日本語\nUTF-8\n"
text += "さくらは 587\n"
text += "サーバは 初期ドメイン(個人毎)"
text = text.encode(jis)     # iso-2022-jp でテキスト全体をエンコード
typrint(text)
msg = MIMEText(text, 'plain', jis)      # メール送信用データのベースを作成

# *************************
# 送信用情報
# *************************
user = "メールユーザ名@ユーザ名.sakura.ne.jp"
password = ""
port = 587
to = "宛先メールアドレス"

# *************************
# メールヘッダ
# *************************
charset = Charset(jis)      # Subject 用エンコードに使用( これをしないと utf-8 が使用される )
msg["Subject"] = charset.header_encode("Python から UTF-8 の文字列 : " + strdate )
msg["From"] = user
msg["To"] = to

# *************************
# 確認用出力
# *************************
print(msg)

# *************************
# メール送信
# *************************
try:

    smtp_server = smtplib.SMTP("ユーザ名.sakura.ne.jp",port)
    smtp_server.starttls()
    smtp_server.login(user, password)
    smtp_server.send_message( msg )
    smtp_server.quit()

    print("メールを送信しました")

except Exception as err:

    print(err)
    print("メール送信に失敗しました" )
