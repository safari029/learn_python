# -*- coding:utf-8 -*-

import ipaddress as ip

class IPSet():

    def __init__(self):
        self.net_set=set() #self.net_set={} とするとdict型になってしまう、空集合は set() で宣言する

    def add(self,net):
        self.net_set.add(ip.IPv4Network(net,strict=False))

    def search(self,address):
        for n in self.net_set:
            if ip.IPv4Address(address) in n:
                return True

        #どれもヒットしなかった場合
        return False


if __name__ == '__main__':

    ipset=IPSet()

    ipset.add('192.168.100.0/24')
    ipset.add('192.168.101.0/24')
    ipset.add('192.168.102.0/24')

    print(ipset.search('192.168.100.1'))
    print(ipset.search('192.168.200.1'))