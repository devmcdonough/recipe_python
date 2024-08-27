class ShoppingList():
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []
    
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
    
    def remove_item(self, item):
        try:
            self.shopping_list.remove(item)
        except: 
            print("Item not found")

    def view_list(self):
        print("\nItems in " + str(self.list_name) + '\n' + 30*'-')
        for item in self.shopping_list:
            print(' - ' + str(item))

    def merge_lists(self, obj):
        # Creates a name for merged list
        merged_lists_name = 'Merged list ' + str(self.list_name) + " + " + str(obj.list_name)
        # Creates empty object
        merged_lists_obj = ShoppingList(merged_lists_name)
        # Adds the first lists name to a new list
        merged_lists_obj.shopping_list = self.shopping_list.copy()
        # Adds the second shopping list to the new list
        for item in obj.shopping_list:
            if not item in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)

        return merged_lists_obj

pet_store_list = ShoppingList('Pet Store Shopping List')
grocery_store_list = ShoppingList('Grocery Store List')

for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)

for item in ['fruits', 'vegetable', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item)

merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

merged_list.view_list()
