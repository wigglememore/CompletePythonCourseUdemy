# generally don't have different data types in one list
list = ['index1', 'index2', 'index3']
# arrays start at one
print(list[1])
print(len(list))
# add to the end of a list
list.append('index4')
print(list)
list.remove('index1')
print(list)

# convention to split long lists by lines
names_ages = [
    ["Cheddar", 2],
    ["Brie", 5],
    ["Stilton", 9]
]
print(names_ages[1][0])

# generally tuples are defined with brackets but they are not awlways necessary
tuple1 = ('val1', 'val2')
# brackets are necessart when putting a tuple inside a list
tuple_in_list = [('val1', 'val2'), ('val2_1', 'val2_2')]
print(tuple_in_list[1])

# tuples don't have .append etc but you can add to them
tuple1 = tuple1 + ('val3',)
print(tuple1)

# sets don't hold order and sets don't contain dubplicate elements
set1 = {'item1', 'item2'}
print(f'set1 is {set1}')
set1.add('item3')
print(f'set1 with an added item is {set1}')
# not duplicates
set1.add('item3')
print(f'set1 with the same item added again is {set1}')
set1.remove('item3')
print(f'set1 with the last item removed is {set1}')

# sets are useful for comparing lists
set_compare_1 = {'a', 'b', 'c'}
set_compare_2 = {'a', 'r', 'h'}
set_1_but_not_2 = set_compare_1.difference(set_compare_2)
print(set_1_but_not_2)
not_in_both = set_compare_1.symmetric_difference(set_compare_2)
print(not_in_both)
both = set_compare_1.intersection(set_compare_2)
print(both)
all_no_duplicates = set_compare_1.union(set_compare_2)
print(all_no_duplicates)
