from flask import Flask, render_template, request
import requests
from recipes import recipes_from_ingredients, find_food

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/recipe_search/", methods=["GET", "POST"])
def recipe_search():
    if request.method == "POST":
        ingredient1 = str(request.form["ingredient 1"])
        ingredient2 = str(request.form["ingredient 2"])
        recipes = recipes_from_ingredients(ingredient1, ingredient2)
        recipe_title = recipes[0]
        ingredientsList = recipes[1]
        recipe_link = recipes[2]
        
        if recipes:
            return render_template(
                "recipe_results.html", ingredient1=ingredient1, ingredient2=ingredient2, recipe_title=recipe_title, ingredientsList=ingredientsList, recipe_link=recipe_link
            )
        else:
            return render_template("search.html", error=True)
    return render_template("search.html", error=None)

@app.route("/food_search/", methods=["GET", "POST"])
def food_search():
    if request.method == "POST":
        food = str(request.form["food"])
        results = find_food(food)
        
        if results:
            return render_template(
                "food_results.html", food=food, results=results
            )
        else:
            return render_template("food_search.html", error=True)
    return render_template("food_search.html", error=None)