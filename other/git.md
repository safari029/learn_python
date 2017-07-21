gitのお勉強
======

# 参考サイト
サルでもわかるgit<http://www.backlog.jp/git-guide/>


# なぜバージョン管理が必要なのか？

1. どこかのファイルサーバでよくある事象

```
manual.txt
manual(修正中).txt
manual_20170721.txt
manual_最新版.txt
manual_最新版2.txt
manual_田中_修正中.txt
```

2. 共同で作業するときによくある事象

A　「俺はこのバグ直したよ」
B　「私は別のとこ直した」
A　「え・・・」
B　「え・・・」


こんなことにならないように作られたのがgitのバージョン管理システム

# 準備編

## まずはgitインストール

技術者ならコンソールで覚えましょう。
※CUI→GUI移行は簡単だけど、GUI→CLIはコストがかかる。環境が変わっても柔軟に対応できるはず。

```
git --version
```
でバージョンが確認できればOK


## gitサーバのアカウント作成

githubのアカウント作成、もしくは社内gitlabのアカウントを払い出してもらう。

他にもgithubのようなgitホスティングサービスは色々あります。

## git 初期設定

後ほど説明しますが、commitする際の表記を設定。

```
git config --global user.name "your username"
git config --global user.email "your email"
```

オレオレ証明書のgitサーバを使うときは以下を設定。

```
git config --global http.sslVerify false
```

ここでの設定はユーザディレクト直下の ".gitconfig" ファイルに保管されてます。

# 入門編

## command

|command|説明|
|:--|:--|
|git init |初期化|
|git status|ステージング状態確認|
|git add|ステージング環境への追加|
|git commit -m "comment"|コミット|
|git log|履歴の確認|
|git remote add origin URL|リモートリポジトリの追加|
|git push origin master|プッシュ|
|git clone|クローン作成|
|git pull|ローカルリポジトリの更新|


## 

* .gitignore
管理対象としないファイルの定義
