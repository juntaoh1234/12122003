
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

temp_key = ''
temp_reason = ''

def udhgetApiUsign(dic, secret):
    if 'usign' in dic.keys():
        dic.pop('usign')
    if 'secret' in dic.keys():
        dic.pop('secret')
    sortedkeys = sorted(dic.keys(), key=str.lower)
    digest = ''
    for k in sortedkeys:
        digest += k + str(dic[k])
    newdigest = secret+digest+secret
    m = hashlib.md5()
    m.update(newdigest.encode())
    return m.hexdigest().upper()

def uscgetApiUsign(dic, secret):
    if 'usign' in dic.keys():
        dic.pop('usign')
    if 'token' in dic.keys():
        dic.pop('token')
    sortedkeys = sorted(dic.keys(), key=str.lower)
    digest = ''
    for k in sortedkeys:
        digest += k + str(dic[k])
    digest += 'secret' + secret
    m = hashlib.md5()
    m.update(digest.encode())
    return m.hexdigest().upper()
