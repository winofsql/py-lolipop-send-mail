# py-lolipop-send-mail

- ### iso-2022-jp.py は、ロリポップが 465 SSL でエラーなので試した結果
  - エラーは sslv3 alert handshake failure
  - 587 で starttls() なしにするとで動作した
  - セキュリティはどうなってるか、さすがに不明( たぶんトラブル対応ルートなんだろあとは思うが... )

- ### Yahoo!は 通常 465 仕様で動作した
