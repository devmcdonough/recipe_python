class Recipe(object):

    all_ingredients = []

    def __init__(self, name, ingredients=None, cooking_time=0):
        self.name = name
        self.ingredients = ingredients if ingredients is not None else []
        self.cooking_time = cooking_time
        self. difficulty = self.calculate_difficulty()

    def get_name(self):
        return self.name
    
    def set_name(self, name=""):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            return "Easy"
        if self.cooking_time < 20 and len(self.ingredients) < 6:
            return "Medium"
        if self.cooking_time < 30 and len(self.ingredients) < 6:
            return "Intermediate"
        else:
            return "Hard"
        
    def get_difficulty(self):
        if self.difficulty is None:
            self.difficulty = self.calculate_difficulty()
        return self.difficulty
        
    def add_ingredients(self, *args):
        for ingredient in args:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
        print("Ingredients have been updated")

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
    def __str__(self):
        return f"Recipe: {self.name}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty}n/Ingredients: {', '.join(self.ingredients)}"
    
    def recipe_search(data, search_term):
        print(f"Recipes containing {search_term}: ")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
        print("-" * 28)

class Tea(Recipe):
    def __init__(self):
        Recipe.__init__(self, name="Tea", ingredients=["Tea packet", "Sugar", "Water"], cooking_time=10)

class Coffee(Recipe):
    def __init__(self):
        Recipe.__init__(self, name="Coffee", ingredients=["Coffee Powder", "Sugar", "Water"], cooking_time=5)

class Cake(Recipe):
    def __init__(self):
        Recipe.__init__(self, name="Cake", ingredients=["Butter", "Sugar", "Eggs", "Vanilla", "Flour", "Baking Powder", "Milk"], cooking_time=50)

class BananaSmoothie(Recipe):
    def __init__(self):
        Recipe.__init__(self, name="Banana Smoothie", ingredients=["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], cooking_time=5)

tea = Tea()
coffee = Coffee()
cake = Cake()
banana_smoothie = BananaSmoothie()

recipes_list = [
    tea,
    coffee,
    cake,
    banana_smoothie
]

ingredients_to_search = ["Water", "Sugar", "Bananas"]

for ingredient in ingredients_to_search:
    Recipe.recipe_search(recipes_list, ingredient)