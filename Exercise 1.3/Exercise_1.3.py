recipes_list = []

ingredients_list = []

def take_recipe():
    n = int(input("How many recipes would you like to enter?: "))

    for i in range(n):
        name = input(f"Name of recipe {i + 1}: ")
        cooking_time = int(input("Cooking time: "))
        ingredients = input("Enter your ingredients and separate them with commas: ").split(', ')
        
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif cooking_time > 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'

        recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}

        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        

        recipes_list.append(recipe)

        print(f"Recipe {i + 1} added: {recipe}")

def display_recipes():
    print("\nAll recipes:\n")
    for recipe in recipes_list:
        print(f"Recipe: {recipe['name']}")
        print(f"Cooking Time: {recipe['cooking_time']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Difficulty: {recipe['difficulty']}")
        print("-" * 20)

def display_ingredients():
    sorted_ingredients = sorted(ingredients_list)
    print("\nIngredients Available Across All Recipes")
    print("-" * 40)
    for ingredient in sorted_ingredients:
        print(ingredient)

take_recipe()

display_recipes()

display_ingredients()