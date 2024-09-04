import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients VARCHAR(250),
               cooking_time INT,
               difficulty ENUM('Easy', 'Medium', 'Intermediate', 'Hard') 
               )''')

def calculate_difficulty(num_ingredients, cooking_time):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients > 4:
        return "Intermediate"
    else:
        return "Hard"

def create_recipe(conn, cursor, name, ingredients, cooking_time):
    ingredients_str = ', '.join(ingredients.split(", "))
    num_ingredients = len(ingredients.split(", "))
    difficulty = calculate_difficulty(cooking_time, num_ingredients)
    
    query ='''INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
            VALUES (%s, %s, %s, %s)'''
    values = (name, ingredients, cooking_time, difficulty)

    cursor.execute(query, values)

    conn.commit()

def search_recipe(conn, cursor):
    # Fetch all ingredients
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    # Create list of unique ingredients
    all_ingredients = set()
    for row in results:
        ingredients = row[0].split(",")
        all_ingredients.update(ingredients)

    # Converts set to list
    all_ingredients = list(all_ingredients)

    # Display ingredients
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}, {ingredient}")

    # User chooses ingredient
    choice = int(input("Choose an ingredient by number: "))
    if 1 <= choice <= len(all_ingredients):
        search_ingredient = all_ingredients[choice -1]
        print(f"Searching for recipes with '{search_ingredient}'...\n")

        # Search for recipes with chosen ingredient
        query = '''SELECT name, ingredients, cooking_time, difficulty
                    FROM Recipes WHERE ingredients LIKE %s'''
        cursor.execute(query, ('%' + search_ingredient + '%',))
        recipes = cursor.fetchall()

        if recipes:
            for recipe in recipes:
                print(f"Recipe: {recipe[0]}, Ingredients: {recipe[1]}, Cooking Time: recipe[2], Difficulty: {recipe[3]}")
        else:
            print(f"We don't have any recipes with {search_ingredient}")
    else:
        print("Uh oh")

def  update_recipe(conn, cursor):
    # Select all recipes and display them
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    print("\nAvailable recipes")
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")

    # Let the user choose recipe by ID
    recipe_id = int(input("ID Number: "))

    # Fetch current recipe
    cursor.execute("SELECT name, ingredients, cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
    current_recipe = cursor.fetchone()

    # Prompt user for new values
    new_name = input("Enter new name: ")
    new_ingredients = input("New ingredients (separated by comma): ")
    new_cooking_time = int(input("New cooking time (in minutes!): "))

    # Convert cooking time to int
    if isinstance(new_cooking_time, str):
        new_cooking_time = int(new_cooking_time)

    # Recalculate difficulty
    num_ingredients = len(new_ingredients.split(", "))
    new_difficulty = calculate_difficulty(num_ingredients, new_cooking_time)

    # Update recipe with new values
    query = '''UPDATE Recipes SET name = %s, ingredients = %s, cooking_time = %s, difficulty = %s WHERE id = %s'''
    cursor.execute(query, (new_name, new_ingredients, new_cooking_time, new_difficulty, recipe_id))
    conn.commit()

def delete_recipes(conn, cursor):
    # Select all recipes and display them
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    print("\nAvailable recipes")
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")

     # Let the user choose recipe by ID
    recipe_id = int(input("ID Number of recipe you want to delete: "))

    query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(query, (recipe_id,))

    conn.commit()
    
    print(f"Recipe {recipe_id} deleted.")

def main_menu():
    choice = ""
    while(choice != 'quit'):
        print("What would you like to do?")
        print("1. Create a new recipe")
        print('2. Search for a recipe by ingredient')
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit")
        choice = input("Yout choice: ")

        if choice == '1':
            name = input("Recipe name: ")
            ingredients = input("Ingredients (separate with commas): ")
            cooking_time = int(input("Cooking time (in minutes): "))
            create_recipe(conn, cursor, name, ingredients, cooking_time)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
            
        elif choice == '4':
            delete_recipes(conn, cursor)
    
    conn.close()

main_menu()