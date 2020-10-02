#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:4.2 for-loop.py
@TIME		:2020/10/02 17:54:46
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

users = {
    '1':'active',
    '2':'inactive',
    '3':'active'
}

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)


for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

