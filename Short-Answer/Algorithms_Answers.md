#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) while and for loops are runtime complexity of O(n).

b) nested for loops (while is a type of for loop) have a runtime complexity of O(n^2).

c) runtime complexity of O(1) since it will take the same amount of time despite the input size.

## Exercise II

### prompt

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

### end of prompt

### Answer

First option: Binary search tree: tree are a type of linked list but without constraint that each node only points to another node.
A tree node can point to multiple other nodes in the tree (linked lists count as trees). Rule for BST: For any given node, all values in the right subtree are greater than or equal to the value at the given node.

(contains, insert, --> in contains, how many items do you have to check? Compare if using linked list or array
BST Pros: optimized for searches, but not for inserting (compared to array or linked list)
BST Cons: if BST not balanced, may not be as efficient.)

I would create a binary search tree using n floors. If the eggs breaks, the value could be n/2 so that those values stay on the left side of the tree. If the egg breaks it would be on the left isde, and if the egg does not break, it would be contained on the right side.
Finally, since values < f are those floors where the egg breaks, >f values will be returned when the egg does not break.

Second option: if I was going to be hacky about this problem, I know the building is n stories. I would set the f = len(n) which would be one above the top floor, so that all floors below would be floors where eggs are not broken.
