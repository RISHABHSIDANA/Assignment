list_a = ["car", "place", "tree", "under", "grass", "price"]

remove_items_containing_a_or_A = lambda x: 'a' not in x.lower()
filtered_list = list(filter(remove_items_containing_a_or_A, list_a))

print(filtered_list)
