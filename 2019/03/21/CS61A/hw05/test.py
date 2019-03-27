from hw05 import generate_paths, tree, print_tree

t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
print_tree(t1)

next(generate_paths(t1, 6))

# path_to_5 = generate_paths(t1, 5)
# sorted(list(path_to_5))
#
# t2 = tree(0, [tree(2, [t1])])
# print_tree(t2)
#
# path_to_2 = generate_paths(t2, 2)
# z = sorted(list(path_to_2))
# print(z)
