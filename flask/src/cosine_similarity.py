#*--coding:utf-8--*
import pickle
from codecs import open as codecopen
from scipy import linalg, mat, dot


def cos_sim():
    cos_sim_vector = []
    tmp_vector = []
    recipe_index = []
    rtmp = []
    tmp_index = []
    last_list_index = []
    complit_list = []

    with open('C:/Users/younh/Desktop/recipe_data/featurelist.txt', 'rb') as f:
        main_feature = pickle.load(f)

    with open('C:/Users/younh/Desktop/recipe_data/vector.txt', 'rb') as f:
        vector = pickle.load(f)

    with open('C:/Users/younh/Desktop/recipe_data/testData.txt', 'rb') as f:
        data = pickle.load(f)

    with open('C:/Users/younh/Desktop/recipe_data/category.txt', 'rb') as f:
        category = pickle.load(f)

    for j in main_feature:
        if j in data:
            tmp_vector.append(1)
        else:
            tmp_vector.append(0)

    for i in vector:
        mA = mat(i)
        mB = mat(tmp_vector)
        cossim_AB = dot(mA, mB.T) / (linalg.norm(mA) * linalg.norm(mB))
        cos_sim_vector.append(cossim_AB)

    for i in range(1,101):
        max_index = cos_sim_vector.index(max(cos_sim_vector))
        max_recipe = cos_sim_vector.index(max(cos_sim_vector)) + 1
        recipe_index.append(max_recipe)
        cos_sim_vector[max_index] = 0.0

    for i in recipe_index:
        if len(str(i)) == 4:
            k = i
        else:
            for j in range(1,5):
                i = '0' + str(i)
                if len(str(i)) == 4:
                    k = i
        tmp_index.append(k)

#    with open('C:/Users/younh/Desktop/recipe_data/recipe_index.txt', 'wb') as f:
#        pickle.dump(recipe_index, f)

    for i in tmp_index:
        rtmp.append('recipe_'+ str(i))

    for i in rtmp:
        f = codecopen('C:/Users/younh/Desktop/recipe_data/recipe/' + i + '.txt', 'r', 'utf-8')
        tmp = f.read().split('\n')

        if category in '':
            last_list_index = rtmp[0:3]
        elif category in tmp[2:3]:
            last_list_index.append(i)
        else:
            pass

    complit_list = last_list_index[0:3]

    return complit_list

cos_sim()