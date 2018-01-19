#-*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for
import pickle
from cosine_similarity import cos_sim
from codecs import open as codecopen

#Initialize
app = Flask(__name__)

#Define a route for url
@app.route('/')
def form():
	return render_template('test.html')

#form action
@app.route('/test2', methods=['POST'] )
def action():
    ingredient = request.form['ingredient']
    category = request.form['category']
    tmp = list(ingredient)
    tmplist = []
    tmptext = ""
    for i in tmp:
        if i in [","]:
            tmplist.append(tmptext)
            tmptext = ""
        elif i in [" "]:
            pass
        else:
            tmptext = tmptext + i
    tmplist.append(tmptext)

    tmptext = ""
    with open('C:/Users/younh/Desktop/recipe_data/testData.txt', 'wb') as f:
        pickle.dump(tmplist, f)
    with open('C:/Users/younh/Desktop/recipe_data/category.txt', 'wb') as f:
        pickle.dump(category, f)

    recipe_list = cos_sim()

    tmprecipe = []
    for i in recipe_list:
        f = codecopen('C:/Users/younh/Desktop/recipe_data/recipe/' + str(i) + '.txt', 'r', 'utf-8')
        tmprecipe.append(f.read())

    return render_template('test2.html', ingredient=ingredient, tmprecipe=tmprecipe)

#Run the app
if __name__ == '__main__':
	app.run(debug='True')