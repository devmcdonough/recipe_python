import pickle

tea = {
    'name': 'Tea',
    'ingredients': 'Tea leaves, Water, Sugar',
    'cooking_time': 5,
    'difficulty': 'Easy'
}

with open('recipe_binary.bin', 'wb') as my_file:
    pickle.dump(tea, my_file)

with open('recipe_binary.bin', 'rb') as my_file:
    loaded_tea = pickle.load(my_file)

print("Recipe:")
print(f"Name: {loaded_tea['name']}")
print(f"Ingredients: {loaded_tea['ingredients']}")
print(f"Cooking Time: {loaded_tea['cooking_time']} minutes")
print(f"Difficulty: {loaded_tea['difficulty']}")
