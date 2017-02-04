#-*- coding: utf-8 -*-

import poplib

def rcvmail(svr,usr,pwd):
    m = poplib.POP3(svr)
    m.user(usr)
    m.pass_(pwd)

    numMessages = len(m.list()[1])

    msg = '\n'.join(m.retr(49)[1])
    parse_message(msg)

    return msg

    m.quit()


if __name__ == '__main__':

    srv = 'mailsrv'  # あなたのPOPサーバ
    user_name = 'usr' #あなたのメールアカウント
    password = raw_input('input password')  #あなたのメールパスワード
    rcvmail(srv,user_name,password)