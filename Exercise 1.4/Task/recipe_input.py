import pickle

recipes_list = []
all_ingredients = []

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
            return 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
            return 'Medium'
    elif cooking_time > 10 and len(ingredients) < 4:
            return 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
            return 'Hard'

def take_recipe(i):
    name = input(f"Name of recipe {i + 1}: ")
    cooking_time = int(input("Cooking time: "))
    ingredients = input("Enter your ingredients and separate them with commas: ").split(', ')
    difficulty = calc_difficulty(cooking_time, ingredients)
       
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}

    recipes_list.append(recipe)

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
        
    print(f"Recipe added: {recipe}")

def collect_recipes():
    n = int(input("How many recipes would you like to enter? "))
    for i in range(n):
        take_recipe(i)

def save_data(filename):

    data = {
        'recipes_list': recipes_list,
        'all_ingredients': all_ingredients
    }

    choice = input(f"Do you want to save '{filename}'? (y/n): ").strip().lower()

    if choice == 'y':
        save_filename = filename 
    else:
        save_filename = input("Enter a new filename: ")

    with open(filename, 'wb') as my_file:
          pickle.dump(data, my_file)
          print(f"Data saved to {filename}")

def load_data():
    filename = input("Filename: ")
    data = None

    try:
        with open(filename, 'rb') as my_file:
               data = pickle.load(my_file)
               print("File loaded successfully")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Let's add some new recipes.")
        data = {
             'recipes_list': [],
             'all_ingredients': []
        }
    except Exception as e:
        print("Something happened! I don't know what: {e}")
        data = {
             'recipes_list': [],
             'all_ingredients': []
        }

    finally:
        global recipes_list, all_ingredients
        recipes_list = data.get('recipes_list', [])
        all_ingredients = data.get('all_ingredients', [])
        if recipes_list or all_ingredients:
            print("We got your data!")
        else:
             print("No data loaded: starting fresh.")

    return filename

def display_recipes():
    print("\nAll recipes:\n")
    for recipe in recipes_list:
        print(f"Recipe: {recipe['name']}")
        print(f"Cooking Time: {recipe['cooking_time']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Difficulty: {recipe['difficulty']}")
        print("-" * 20)

def display_ingredients():
    sorted_ingredients = sorted(all_ingredients)
    print("\nIngredients Available Across All Recipes")
    print("-" * 40)
    for ingredient in sorted_ingredients:
        print(ingredient)

filename = load_data()

display_recipes()
display_ingredients()

collect_recipes()

display_recipes()
display_ingredients()

save_data(filename)