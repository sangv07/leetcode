#!/usr/bin/env python
# coding: utf-8

# # Problem

# The problem is set up as follows:
# You are given a list of airports and you have to ensure a passenger can reach each of those airports,
# starting at 'lga', with as many interconnecting flights as you like. All connecting one-way flights
# that you already have available are also given in the list called routes, none of these depart from 'lga'.
# It is your job to fill in the necessary flights exlusively departing from 'lga' to any other airport in order to be able to reach all airports.
# The challenge is to use the minimal amount of flights departing from 'lga'.
# First we import the only library necessary, the airports and the routes.

# In[1]:

airports = ['bgi','cdg','del','doh','dsm','ewr','eyw','hnd','icn','jfk','lga','lhr','ord','san','sfo','sin','tlv','bud']

routes = [['dsm','ord'], ['bgi','lga'], ['sin','cdg'], ['cdg','sin'], ['del','doh'], ['del','cdg'], ['tlv','del'],
          ['ewr','hnd'], ['hnd','icn'], ['hnd','jfk'], ['icn','jfk'], ['jfk','lga'], ['eyw','lhr'], ['lhr','sfo'],
          ['sfo','san'], ['sfo','dsm'], ['san','eyw'], ['cdg','bud']]
a = ['dsm','ord']
b = ['ord','bgi']
c = ['bgi','lga']
d = ['sin','cdg']
e = ['cdg','sin']
f = ['del','doh']
g = ['del','cdg']
h = ['tlv','del']
i = ['ewr','hnd']
j = ['hnd','icn']
k = ['hnd','jfk']
l = ['icn','jfk']
m = ['jfk','lga']
n = ['eyw','lhr']
o = ['lhr','sfo']
p = ['sfo','san']
q = ['sfo','dsm']
r = ['san','eyw']
s = ['cdg','bud']

#routes = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s]

for i in