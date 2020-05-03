from flask import Flask, render_template, request
import requests
from recipes import recipes_from_ingredients, find_food

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route('/why')
def why():
    return render_template('why.html')

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route("/recipe_search/", methods=["GET", "POST"])
def recipe_search():
    if request.method == "POST":
        ingredient1 = str(request.form["ingredient 1"])
        ingredient2 = str(request.form["ingredient 2"])
        recipes = recipes_from_ingredients(ingredient1, ingredient2)
        recipe_title = recipes[0]
        ingredientsList = recipes[1]
        recipe_nutrients = recipes[2]
        recipe_link = recipes[3]
        image_url = recipes[4]
        
        if recipes:
            return render_template(
                "recipe_results.html", ingredient1=ingredient1, ingredient2=ingredient2, recipe_title=recipe_title, ingredientsList=ingredientsList, recipe_link=recipe_link, recipe_nutrients=recipe_nutrients, image_url=image_url
            )
        else:
            return render_template("search.html", error=True)
    return render_template("search.html", error=None)

@app.route("/food_search/", methods=["GET", "POST"])
def food_search():
    if request.method == "POST":
        food = str(request.form["food"])
        results = find_food(food)
        nutrients = results[0]
        image = results[1]
        
        if results:
            return render_template(
                "food_results.html", food=food, nutrients=nutrients, image=image
            )
        else:
            return render_template("food_search.html", error=True)
    return render_template("food_search.html", error=None)