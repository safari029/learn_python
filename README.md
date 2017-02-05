# python勉強会用資料置き場

## 環境

|ソフト|説明|
|:-------------|:---------|
|python3.6|pythonの本体|
|anaconda4.3|パッケージ管理ソフト|
|pycharm|python用の統合開発ソフト|

## インストール方法

1. [anaconda(4.3)](https://www.continuum.io/downloads)  から自分の環境にあったものを落とし、インストールします。こちらにpython3.6本体も同梱されています。　　　　　　　　　　　　　　　　　　　

2. [pycharm community edition](https://www.jetbrains.com/pycharm/download/)をインストールしてください。

参考
http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c  
http://qiita.com/t2y/items/2a3eb58103e85d8064b6

## 勉強の進め方
1. notebookに記載のコードを手元の環境で実行してみましょう。
2. 各章末に実践編としてプログラムを作る課題がありますので試してみてください。


## pythonのよくつまづくポイントまとめ

1. 文字コードについて  
python3系は文字をunicodeとして処理する。（2系は）
出力する際には基本的に最初に宣言した符号化処理で実施する。
windows系のpythonだとデフォのエンコードがcp932、macだとutf-8  
[参考]  
[Unicode HOWTO](https://docs.python.jp/3/howto/unicode.html)
[文字コードの考え方から理解するUnicodeとUTF-8の違い](http://equj65.net/tech/charcode/)

```python
#defaultエンコーディングの確認方法
import sys
sys.getdefaultencoding()
```
