#-*- coding: utf-8 -*-
import os
import pickle
import re
from codecs import open as codecopen

featurelist = []

for i in os.listdir('C:/Users/younh/Desktop/recipe_data/ingredient'):
    f = codecopen('C:/Users/younh/Desktop/recipe_data/ingredient/' + str(i), 'r', 'utf-8')
    print i
    tmp = f.read()

    tmp1 = []

    regex = re.compile('tip.*')

    tmp = re.sub(regex, '', tmp)

    regex = re.compile('(\(.+?\),)')

    tmp1 = re.sub(regex, ',', tmp)

    regex = re.compile('\(.*\)')

    tmp1 = re.sub(regex, '', tmp1)

    regex = re.compile('\, ')

    tmp1 = re.sub(regex, ',', tmp1)

    regex = re.compile('tip.*')
    tmp1 = re.sub(regex, '', tmp1)

    tmp1 = tmp1.replace(', ',',')
    tmp1 = tmp1.split(',')
    tmp2 = []
    for j in tmp1:
        k = j.split('\n')
        for t in k:
            tmp2.append(t)
    del tmp2[0]
    del tmp2[0]

    tmp4 = []
    for j in tmp2:
        if j is u'':
            pass
        else :
            tmp4.append(j)

    for j in tmp4:
        if j in featurelist:
            pass
        elif j in ' ':
            pass
        else:
            featurelist.append(j)
    f.close()



for i in featurelist:
    print i
    #print '\n'


g = codecopen('C:/Users/younh/Desktop/recipe_data/featurelist.txt', 'wb')
pickle.dump(featurelist, g)

g.close()
