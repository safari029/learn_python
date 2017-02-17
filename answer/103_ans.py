# -*- coding:utf-8 -*-

import requests

#設定値
url='https://slack.com/api/chat.postMessage'
token = 'your token' #https://api.slack.com/web からtokenを作成します。
channel = 'your chanel name #hogehoge'
text = 'Hello API!!'

#辞書型でパラメータを指定
d={
    'token':token,
    'channel':channel,
    'text':text
}

#リクエスト本体
res=requests.post(url,data=d) #postした結果をresに格納

#結果を出力
print(res) #ステータスコードを表示
print(res.json) #json形式でレスポンスが帰ってくるとき、そのままデコードすることも可能