from time import sleep


class RBTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def insert(self, key):                                          # insert new node
        node = Node(key)
        node.parent = None
        node.value = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                              # 1 is red, 0 is black and new node is always red

        y = None
        x = self.root

        while x != self.NULL:                                       # loop to find position of new node
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y                                             # y is parent of new node
        if y is None:                                               # new node has no parent, then its the root
            self.root = node
        elif node.value < y.value:                                  # check if it goes to left/right subtree
            y.left = node
        else:
            y.right = node
        if node.parent is None:                                     # root node is black always
            node.color = 0
            return
        if node.parent.parent is None:                              # if parent of new node is root
            return
        self.fixInsert(node)                                        # check and fix for RB properties

    def fixInsert(self, k):
        while k.parent.color == 1:                                  # while parent is red
            if k.parent == k.parent.parent.right:                   # if parent is right child of its parent aka GRANDPARENT
                u = k.parent.parent.left                            # takes the left child of GRANDPARENT
                if u.color == 1:                                    # if its color is red, UNCLE node is red
                    u.color = 0                                     # set children of GRANDPARENT black
                    k.parent.color = 0
                    k.parent.parent.color = 1                       # set GRANDPARENT as red
                    k = k.parent.parent                             # check again
                else:
                    if k == k.parent.left:                          # if node is left child of parent
                        k = k.parent
                        self.RightRotate(k)                         # do RR
                    k.parent.color = 0                              # sets parent color to black
                    k.parent.parent.color = 1                       # sets GRANDPARENT color to red
                    self.LeftRotate(k.parent.parent)                # do LR
            else:                                                   # same process but for parent if left child of its parent but LR is first then RR
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.LeftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0                                         # root color is always black from properties

    def LeftRotate(self, x):
        y = x.right                                                 # Y = Right child of x
        x.right = y.left                                            # Change right child of x to left child of y
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent                                         # Change parent of y as parent of x
        if x.parent is None:                                        # If parent of x == None ie. root node
            self.root = y                                           # Set y as root
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RightRotate(self, x):
        y = x.left                                                  # Y = Left child of x
        x.left = y.right                                            # Change left child of x to right child of y
        if y.right != self.NULL:
            y.right.parent = x
        y.parent = x.parent                                         # Change parent of y as parent of x
        if x.parent is None:                                        # If x is root node
            self.root = y                                           # Set y as root
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, value):
        self.delete_node(self.root, value)

    def delete_node(self, node, key):
        z = self.NULL
        while node != self.NULL:                                    # loop to find the node and store it in z
            if node.value == key:
                z = node

            if node.value <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:                                          # if node is not found throw this error
            print("Value not found")
            return

        y = z
        y_original_color = y.color                                  # get color of the node and store it
        if z.left == self.NULL:                                     # if left child of z is NULL
            x = z.right                                             # x is the right child of node
            self.transplant(z, x)                                   # delete and replace z with x
        elif z.right == self.NULL:                                  # same but for right child
            x = z.left
            self.transplant(z, x)
        else:                                                       # if z has both children
            y = self.minimum(z.right)                               # get min of right subtree
            y_original_color = y.color                              # get color of node and store it
            x = y.right
            if y.parent == z:                                       # if y is direct child of z
                x.parent = y                                        # set y as x's parent
            else:                                                   # if y is not direct child of z, do modifications to get it to the top
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:                                   # if color is black after all the modifications, check and fix
            self.fixDelete(x)

    def fixDelete(self, x):
        while x != self.root and x.color == 0:                      # loop until we get to root and the root is black
            if x == x.parent.left:                                  # if x is left child of parent
                s = x.parent.right                                  # get SIBLING of x
                if s.color == 1:                                    # if SIBLING is red
                    s.color = 0                                     # set SIBLING color to black
                    x.parent.color = 1                              # set parent of x to red
                    self.LeftRotate(x.parent)                       # do LR
                    s = x.parent.right                              # get new value of SIBLING
                if s.left.color == 0 and s.right.color == 0:        # if both SIBLING are black
                    s.color = 1                                     # set SIBLING color to red
                    x = x.parent
                else:
                    if s.right.color == 0:                          # if only right SIBLING is black
                        s.left.color = 0                            # set left child of SIBLING as black
                        s.color = 1                                 # set SIBLING color as red
                        self.RightRotate(s)                         # do RR
                        s = x.parent.right
                    s.color = x.parent.color                        # if only left SIBLING is black
                    x.parent.color = 0                              # set parent of x as black
                    s.right.color = 0                               # set right SIBLING as black
                    self.LeftRotate(x.parent)                       # do LR
                    x = self.root
            else:                                                   # if x is right child of parent
                s = x.parent.left                                   # same process but for x as right child of parent
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.RightRotate(x.parent)                      # do RR instead of LR
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.LeftRotate(s)                          # do LR instead of RR
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RightRotate(x.parent)                      # do RR instead of LR
                    x = self.root
        x.color = 0                                                 # since all cases were reached now x will be root and set color as black

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def print(self):
        print("-------- Current RB-Tree --------\n")
        self.printTree(self.root, "", True)
        print("---------------------------------")

    def printTree(self, node, indent, direction):
        if node != self.NULL:
            print(indent, end="")
            if direction:
                if node is self.root:
                    print("Root >>>>>", end=" ")
                    indent += "\t"
                else:
                    print("R >>>>>", end=" ")
                    indent += "|\t"
            else:
                print("L >>>>>", end=" ")
                indent += "|\t"

            color = "r" if node.color == 1 else "b"
            print(str(node.value) + " [ " + color + " ] \n")
            self.printTree(node.left, indent, False)
            self.printTree(node.right, indent, True)

    def RB_BHeight(self):
        aux = self.root
        bh = 0
        while aux != self.NULL:
            aux = aux.left
            if aux.color == 0:
                bh += 1
        print("\tBlack-Height of", bh, "was found\n")

    @staticmethod
    def RB_Height():
        print("\tNormal-Height of", newTree.RB_NHeight(newTree.root), "was found\n")

    def RB_NHeight(self, aux):
        if aux == self.NULL:
            return -1
        else:
            lDepth = newTree.RB_NHeight(aux.left)
            rDepth = newTree.RB_NHeight(aux.right)
            if lDepth < rDepth:
                return rDepth + 1
            else:
                return lDepth + 1


# Define Node
class Node:
    def __init__(self, value):
        self.value = value                                          # initialize node as itself
        self.parent = None                                          # parent as empty
        self.left = None                                            # left child as empty
        self.right = None                                           # right child as empty
        self.color = 1                                              # color of node is always red when inserted


if __name__ == "__main__":
    answer = True
    while answer:
        print("1)\tCreate RB-Tree\n"
              "2)\tShow the Tree\n"
              "3)\tInsert value into Tree\n"
              "4)\tRemove value from Tree\n"
              "5)\tGet Black Height\n"
              "6)\tGet Normal Height\n"
              "7)\tGet min value\n"
              "8)\tGet max value\n"
              "9)\tExit program\n")
        choice = int(input("Choose an option: "))
        if choice == 1:
            newTree = RBTree()
            print("\tTree created successfully")
            print("\n")
        elif choice == 2:
            newTree.print()
            print("\n")
        elif choice == 3:
            try:
                nr = int(input("\tValue to insert: "))
                newTree.insert(nr)
                sleep(2)
                print("Successful operation\n")
            except:
                print("\nError, no Tree was found\n")
        elif choice == 4:
            try:
                nr = int(input("\tValue to delete: "))
                newTree.delete(nr)
                sleep(2)
                print("Successful operation\n")
            except:
                print("\nError, no Tree was found\n")
        elif choice == 5:
            newTree.RB_BHeight()
        elif choice == 6:
            newTree.RB_Height()
        elif choice == 7:
            mini = newTree.minimum(newTree.root)
            print("I've found as min value", str(mini.value))
            print("")
        elif choice == 8:
            maxi = newTree.maximum(newTree.root)
            print("I've found as max value", str(maxi.value))
            print("")
        elif choice == 9:
            print("\tGo to sleep")
            sleep(2)
            print("1 Sheep")
            sleep(2)
            print("2 Sheep")
            sleep(2)
            print("3 Sheep")
            sleep(2)
            print("4 She.. *yawn*")
            sleep(3)
            print("\tGood night, sweet prince")
            answer = False
        else:
            print("\tINVALID choice, try again\n\n")
            sleep(2)
