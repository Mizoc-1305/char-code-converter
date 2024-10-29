# 文字コード変換器
大学の課題で作成した、文字コードを相互に変換するプログラムです。  
## 使い方  
コマンドラインで次のコードを実行します。  
```bash
python main.py
```
  
変換前の文字コードと変換後の文字コードをそれぞれ選択します。  
```bash
変換前の文字コードを選択してください:
1: Shift_JIS
2: ISO-2022-JP
3: EUC-JP
4: Unicode (UTF-8)
番号を入力:

変換後の文字コードを選択してください:
1: Shift_JIS
2: ISO-2022-JP
3: EUC-JP
4: Unicode (UTF-8)
番号を入力:
```  

変換したい文字コードを入力します。  
ただし、スペースは削除して16進数のバイト列として入力してください。  
また、Unicodeの場合は「U+」や「u+」は削除してください。  
```bash
変換したい16進数のバイト列を入力してください。空白は入れず、Unicodeの場合「U+」は削除してください。:
```

入力したバイト列をデコードして日本語の文字列にしたものと、指定した文字コードで再エンコードした結果が表示されます。   
以下は入出力の例です。


```bash:
変換前の文字コードを選択してください:
1: Shift_JIS
2: ISO-2022-JP
3: EUC-JP
4: Unicode (UTF-8)
番号を入力: 1

変換後の文字コードを選択してください:
1: Shift_JIS
2: ISO-2022-JP
3: EUC-JP
4: Unicode (UTF-8)
番号を入力: 3
shift_jis から euc_jp に変換します。

変換したい16進数のバイト列を入力してください。空白は入れず、Unicodeの場合「U+」は削除してください。: 82b182f182c982bf82cd

デコード結果: こんにちは
euc_jp形式の16進数出力: A4B3A4F3A4CBA4C1A4CF
```
