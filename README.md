# python勉強会用資料置き場

## pythonって何がいいの？

1. 普通に書いてるだけで、綺麗にかける。可読性が高い。
2. 全てのデータがオブジェクトなので、扱いやすい。
3. ライブラリが豊富（特にデータ分析系）、歯車の開発が不要。

→以下で実際に体験していきましょう。

## 環境

|ソフト|説明|
|:-------------|:---------|
|python3.6|pythonの本体|
|anaconda4.3|パッケージ管理ソフト|
|pycharm|python用の統合開発ソフト|

## インストール方法

1. [python](https://www.python.org/downloads/)  から自分の環境にあったものをダウンロードし、インストールします。3系の最新バージョンをインストールしましょう。

2. [pycharm community edition](https://www.jetbrains.com/pycharm/download/)をインストールしてください。

参考
http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c  
http://qiita.com/t2y/items/2a3eb58103e85d8064b6

## 基本的な勉強の進め方
1. 基本的にpycharm上でコードを実行していってもらいたいので、[pycharm_guide.md](https://github.com/safari029/learn_python/blob/master/pycharm_guide.md)をみてください。
2. learnフォルダのnotebookに記載のコードを手元の環境で実行してみましょう。
3. 各章末に実践編としてプログラムを作る課題がありますので試してみてください。
4. learnの100以降は便利なパッケージ類の紹介を行う予定です。実際に開発に役立てていきましょう。
5. 他に必要そうな項目は以下に随時まとめていきます。

### コミュニティ活動系
オンサイトのイベントに参加してみましょう。

* [PyData.Tokyo](https://pydatatokyo.connpass.com/)
* [PyCon JP](https://pyconjp.connpass.com/)
* [Start Python Club](https://startpython.connpass.com/)

### セキュリティ
* [Pythonに咬まれるな : 注意すべきセキュリティリスクのリスト](http://postd.cc/a-bite-of-python/)

### pythonのよくつまづくポイントまとめ
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
