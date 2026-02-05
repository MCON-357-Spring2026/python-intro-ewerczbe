"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is  the length of the corresponding food item in the original list.
"""
favorite_foods = ['apples', 'oranges', 'pears', 'grapes']
print(favorite_foods[0])
print(favorite_foods[3])
favorite_foods.append('grapefruit')
favorite_foods.remove('oranges')
for item in favorite_foods:
    print(item)
lengths = [len(food) for food in favorite_foods]
for item in lengths:
    print(item)