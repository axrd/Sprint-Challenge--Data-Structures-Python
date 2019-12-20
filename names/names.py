# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?


import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# OG solution with a WEAK t complexity of O(n^2):

#duplicates = []
#for name_1 in names_1:
 #   for name_2 in names_2:
  #      if name_1 == name_2:
   #         duplicates.append(name_1)


# Implementing a Binary Search Tree:
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def append(self, value):
        # Doing it recursively:
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.append(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.append(value)

    # Checking if specific value is in the tree
    def is_in(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                self.left.is_in(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.is_in(target)




duplicates = []

bst = BinarySearchTree(names_1[0])
for name_1 in names_1:
    bst.append(name_1)
for name_2 in names_2:
    if bst.is_in(name_2):
        duplicates.append(name_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# We're down to < 0.23 seconds :)


