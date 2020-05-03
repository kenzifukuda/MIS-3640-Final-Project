import json
import urllib.request
import urllib.parse
from pprint import pprint
import string

base_url = 'https://api.edamam.com'
rid_num = '76c66c05'
r_key = '9de7a31a7d8269c0d0b62d55324a5646'
fid_num = 'b248fb3a'
f_key = '25332f58957a326060980b9b0842352c'

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

def recipes_from_ingredients(ingredient1, ingredient2):
    ingredient1 = ingredient1.replace(' ', '%20')
    ingredient2 = ingredient2.replace(' ', '%20')
    url = f'{base_url}/search?q={ingredient1}%2C{ingredient2}&app_id={rid_num}&app_key={r_key}&from=0&to=1'
    json_data = get_json(url)
    recipe_title = json_data['hits'][0]['recipe']['label']
    ingredients_list = json_data['hits'][0]['recipe']['ingredientLines']
    recipe_nutrients = json_data['hits'][0]['recipe']['totalNutrients']
    recipe_url = json_data['hits'][0]['recipe']['url']
    image_url = json_data['hits'][0]['recipe']['image']
    return recipe_title, ingredients_list, recipe_nutrients, recipe_url, image_url
# pprint(recipes_from_ingredients('chicken','lemon'))

# def recipe_nutrition(ingredient1, ingredient2):
#     recipe_info = tuple(recipes_from_ingredients(ingredient1, ingredient2))
#     recipe_id = recipe_info[3]
#     recipe_id = recipe_id.replace(':', '%3A')
#     recipe_id = recipe_id.replace('/', '%2F')
#     recipe_id = recipe_id.replace('#', '%23')
#     url = f'{base_url}/search?r={recipe_id}&app_id={rid_num}&app_key={r_key}'
#     json_data = get_json(url)
#     recipe_calories = json_data[0]['calories']
#     return recipe_nutrition
# # pprint(recipe_nutrition('chicken', 'lemon'))

def find_food(food_name):
    food_name = food_name.replace(' ', '%20')
    url = f'{base_url}/api/food-database/parser?app_id={fid_num}&app_key={f_key}&ingr={food_name}&nutrition-type=logging'
    json_data = get_json(url)
    nutrients = json_data['hints'][0]['food']['nutrients']
    image_url = json_data['hints'][0]['food']['image']
    return nutrients, image_url

# pprint(find_food('red apple'))






























# def remove_punctuation(a_list):
#     punctuation = string.punctuation
#     for i in a_list:
#         for letter in i:
#             if letter in punctuation:
#                 i = i.replace(letter, '')
#     return a_list

# def remove_spaces(a_list):
#     a_list = [i.replace(' ', '%20') for i in a_list]
#     return a_list

# def build_url(*a_list):
#     ings = '&ingr='.join(a_list)
#     for i in a_list:
#         url = f'{base_url}/nutrition-data?app_id={id_num}&app_key={key}'

# def get_recipe_nutrition(ingredient1, ingredient2):
#     recipe_tuple = tuple(recipes_from_ingredients(ingredient1, ingredient2))
#     ingredient_list = recipe_tuple[1]
#     ingredient_list = remove_punctuation(ingredient_list)
#     ingredient_list = remove_spaces(ingredient_list)
    
#     url = f'{base_url}/nutrition-data?app_id={id_num}&app_key={key}&ingr={ingredient_list}'
#     json_data = get_json(url)
#     return json_data

# pprint(get_recipe_nutrition('chicken', 'lemon'))