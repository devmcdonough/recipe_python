from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Connects Python script to sql
Base = declarative_base()

# Creates engine object
engine = create_engine(
    "mysql+mysqlconnector://cf-python:password@localhost/my_database"
)

# Creates session for database
Session = sessionmaker(bind=engine)
session = Session()


class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return (
            "Recipe ID: "
            + str(self.id)
            + "Name: "
            + self.name
            + "Difficulty: "
            + str(self.difficulty)
        )

    def __str__(self):
        return (
           "Recipe ID: " + str(self.id) + "\n"
            "Name: " + self.name + "\n"
            "Ingredients: " + self.ingredients + "\n"
            "Cooking Time: " + str(self.cooking_time) + " minutes\n"
            "Difficulty: " + (self.difficulty if self.difficulty else "Not set") + "\n"
            + "-" * 25
        )
    
    def return_ingredients_as_list(self):
        ingredients_list = self.ingredients.split(", ")
        if ingredients_list == "":
            return []
        else:
            return ingredients_list


    def calculate_difficulty(self):
        ingredients_list = self.ingredients.split(", ")
        num_ingredients = len(ingredients_list)
        print(f"Calculating difficulty: {num_ingredients} ingredients, {self.cooking_time} minutes")

        if num_ingredients < 4 and self.cooking_time < 10:
            self.difficulty = "Easy"
        elif num_ingredients > 4 and self.cooking_time < 10:
            self.difficulty = "Medium"
        elif num_ingredients < 4 and self.cooking_time > 10:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"
        print(f"Difficulty set to: {self.difficulty}")

        
def create_recipe(session, name, ingredients, cooking_time):

    #Validate name
    if len(name) > 50:
        raise ValueError("Name is too long")
    if not name.replace(' ', '').isalnum():
        raise ValueError("Only letters and numbers here")
    
    # Validate cooking time
    if not str(cooking_time).isnumeric():
        raise ValueError("Cooking time should be a number")
    

    num_ingredients = int(input("How many ingredients would you like to enter?: "))
    if num_ingredients == 0:
        raise ValueError("You need at least one ingredient.")

    # Collect ingredients
    ingredients = []

     # Validate ingredients
    if num_ingredients == 0:
        raise ValueError("Add some ingredients")
    
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        #Validate ingredients
        if not ingredient.replace(' ', '').isalpha():
            raise ValueError("'{ingredient}' should only contain letters")
        ingredients.append(ingredient)

    # Converts ingredients into a single string
    ingredients_str = ', '.join(ingredients)

    # Creates new instance
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
        )

    # Calculates and sets difficulty
    recipe_entry.calculate_difficulty()

    # adds new recipe to sessions
    session.add(recipe_entry)
 
    # Saves to the database
    session.commit()

    session.refresh(recipe_entry)
    return recipe_entry

def view_all_recipes(session):
    # Retrieves all recipes
    recipes = session.query(Recipe).all()

    # Check if the database is empty
    if not recipes:
        print("There are no recipes")
        return None
    
    # Loop to display all available recipes
    for recipe in recipes:
        print(recipe)

def search_by_ingredients(session):
    num_recipes = session.query(Recipe).count()
    if num_recipes == 0:
        print("We don't have any recipes, yet.")
        return None  # Exit function if no recipes exist

    # Retrieve all ingredients from the database
    results = session.query(Recipe.ingredients).all()

    all_ingredients = []

    # Create list of unique ingredients
    for result in results:
        ingredients_list = result[0].split(', ')
        all_ingredients.extend(ingredients_list)

    all_ingredients = list(set(all_ingredients))  # Make ingredients unique

    # Display available ingredients
    print("\nAvailable Ingredients: ")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")

    # User selects ingredients by number
    search_ingredients = []
    try:
        while True:
            choice = input("Choose an ingredient by number (or press Enter to finish): ")
            if choice == '':
                break  # Exit the loop if the user presses Enter
            choice = int(choice)
            if 1 <= choice <= len(all_ingredients):
                selected_ingredient = all_ingredients[choice - 1]
                search_ingredients.append(selected_ingredient)
                print(f"Added '{selected_ingredient}' to search.")
            else:
                print("Invalid choice. Choose a number from the list.")
    except ValueError:
        print("Please enter a valid number.")
        return None  # Exit on invalid input

    # If no ingredients were selected, exit
    if not search_ingredients:
        print("No ingredients selected for search.")
        return None

    # Initialize list for search conditions
    conditions = []

    # Create like() conditions for each selected ingredient
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"  # Create a search string like '%ingredient%'
        condition = Recipe.ingredients.like(like_term)  # SQLAlchemy like condition
        conditions.append(condition)

    # Retrieve all recipes that match the search conditions
    matching_recipes = session.query(Recipe).filter(*conditions).all()

    # Display the matching recipes
    if matching_recipes:
        print("\nRecipes matching the selected ingredients:")
        for recipe in matching_recipes:
            print(recipe)  # Calls __str__ method of Recipe to display details
    else:
        print("No recipes found with the selected ingredients.")


def edit_recipe(session):

    num_recipes = session.query(Recipe).count()
    if num_recipes == 0:
        print("We don't have any recipes, yet.")
        return None  # Exit function if no recipes exist

    # Retrieve all ingredients from the database
    results = session.query(Recipe.id, Recipe.name).all()

    print("\nAvailable recipes")
    for result in results:
        print(f"ID: {result[0]}, Name: {result[1]}")

    # Let the user choose recipe by ID
    try: 
        recipe_id = int(input("Enter ID Number: "))
    except ValueError:
        print("That didn't work. Try another ID number")
        return None
    
    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_edit:
        print("We can't find that ID")
        return None
    
    #Display details
    print(f"Editing: ")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking time: {recipe_to_edit.cooking_time} minutes")

    # User chooses which attribute to edit
    try:
        choice = int(input("Choose a number to edit: "))
    except ValueError:
        print("Please enter a number from 1-3")
        return None
    
    if choice == 1:
        new_name = input("Enter new name: ")
        if len(new_name) > 50:
            print("That name is too long")
            return None
        recipe_to_edit.name = new_name

    elif choice == 2:
        new_ingredients = input("Enter new ingredients and separate by comma")
        recipe_to_edit.ingredients = new_ingredients
        recipe_to_edit.calculate_difficulty()

    elif choice == 3:
        try:
            new_cooking_time = int(input("Enter a new cooking time in minutes: "))
        except ValueError:
            print("Please enter a number")
            return None
        recipe_to_edit.cooking_time = new_cooking_time
        recipe_to_edit.calculate_difficulty()

    else:
        print("Please choose a number between 1 and 3.")
        return None
    
    session.commit()
    print("Recipe updated")

    session.refresh(recipe_to_edit)

    print("\nUpdated Recipe: ")
    print(f"Name: {recipe_to_edit.name}")
    print(f"Ingredients: {recipe_to_edit.ingredients}")
    print(f"Cooking time: {recipe_to_edit.cooking_time}")
    print(f"Difficulty: {recipe_to_edit.difficulty}")

def delete_recipe(session):
    # Checks if there are any recipes in the database
    num_recipes = session.query(Recipe).count()
    if num_recipes == 0:
        return None  # Exit function if no recipes exist
    
    # Retrieve all ingredients from the database
    results = session.query(Recipe.id, Recipe.name).all()

    print("\nAvailable recipes")
    for result in results:
        print(f"ID: {result[0]}, Name: {result[1]}")

     # Let the user choose recipe by ID
    try: 
        recipe_id = int(input("Enter ID Number: "))
    except ValueError:
        print("That didn't work. Try another ID number")
        return None

    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_delete:
        print("We can't find that ID")
        return None
    
    confirmation = input(f"Are you sure you want to delete '{recipe_to_delete.name}? (y/n)").lower()
    
    if confirmation == 'y':
        session.delete(recipe_to_delete)
        session.commit()
        print(f"'{recipe_to_delete.name}' deleted")
    else:
        print("Deletion canceled")

def main_menu(session):
    choice = ""
    while(choice != 'quit'):
        print("What would you like to do?")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print('3. Search for a recipe by ingredient')
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit")
        choice = input("Your choice: ")

        if choice == '1':
            name = input("Recipe name: ")
            try:
                cooking_time = int(input("Cooking time (in minutes): "))
                create_recipe(session, name, '', cooking_time)
            except ValueError:
                print("Cooking time should be a number")
        elif choice == '2':
            view_all_recipes(session)
        elif choice == '3':
            search_by_ingredients(session)
        elif choice == '4':
            edit_recipe(session)           
        elif choice == '5':
            delete_recipe(session)

        elif choice == 'quit':
            print("Goodbye")

        else:
            print("Please enter one of the options listed.")
    

Base.metadata.create_all(engine)

if __name__ == "__main__":
    try:
        main_menu(session)
    finally:
        session.close()
        engine.dispose()