import pickle

def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']}")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")
    print("-" * 20)

def search_ingredient(data):
    ingredients = data.get('all_ingredients', [])

    print("Ingredients")
    for index, ingredient in enumerate(ingredients, start=1):
        print(f"{index}: {ingredient}")

    try:
        choice = int(input("Pick an ingredient by number: "))
        ingredient_searched = ingredients[choice - 1]

        print(f"\nRecipes containing '{ingredient_searched}':\n")
        recipes = data.get('recipes_list', [])
        for recipe in recipes:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)

    except (ValueError, IndexError):
        print("Please enter one of the numbers that correspond to an ingredient")
    else:
        if not recipes:
            print(f"No recipes found with ingredient '{ingredient_searched}'.")

def recipe_search():
    filename = input("Enter the filename where you keep your recipes: ")

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            print(f"File '{filename}' loaded successfully.")
    except FileNotFoundError:
        print(f"'{filename}' not found")
    else:
        search_ingredient(data)

recipe_search()

    


