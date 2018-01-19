import pickle
import os
import re
from codecs import open as codecopen

ingredient_vector = []

with open('C:/Users/younh/Desktop/recipe_data/featurelist.txt', 'rb') as f:
    main_feature = pickle.load(f)

for i in os.listdir('C:/Users/younh/Desktop/recipe_data/recipe'):
    tmp_vector = []
    ingredient_list = []
    f = codecopen('C:/Users/younh/Desktop/recipe_data/recipe/' + str(i), 'r', 'utf-8')

    tmp = f.read().split('\n')

    tmp_split = []
    for j in tmp[7:9]:
        print j

        regex = re.compile('tip.*')

        j = re.sub(regex, '', j)

        regex = re.compile('(\(.+?\),)')

        j = re.sub(regex, ',', j)


        regex = re.compile('\(.*\)')

        j = re.sub(regex, '', j)

        regex = re.compile('\, ')

        j = re.sub(regex, ',', j)

        split_tmp = j.split(',')

        for k in split_tmp:
            tmp_split.append(k)

    if u'' in tmp_split:
        integer = tmp_split.index(u'')
        del tmp_split[integer]

    for j in main_feature:
        if j in tmp_split:
            tmp_vector.append(1)
        else:
            tmp_vector.append(0)
    print i
    print tmp_vector
    print '==========================================================='


    ingredient_vector.append(tmp_vector)

    f.close()

with open('C:/Users/younh/Desktop/recipe_data/vector.txt','wb') as f:
    pickle.dump(ingredient_vector,f)
