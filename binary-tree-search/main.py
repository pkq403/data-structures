from dataclasses import dataclass
from typing import Optional, Callable
import sys
'''
Binary Search Tree (BST) Python3 implementation
(test it in test.py file)
Author: pkq403
'''

@dataclass
class Node:
    val: int
    right: Optional["Node"] = None
    left: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self, root_val: int):
        self.root = Node(val=root_val)

    def search(self, val: int) -> bool:
        """
        Search operation.
        Search for a value in the BST.

        Returns
        =======
        bool
            True if value found else False
        """

        def rsearch(node: Node) -> bool:
            if node is None:
                return False
            if node.val == val:
                return True
            if node.val < val:
                return rsearch(node.right)
            return rsearch(node.left)

        return rsearch(self.root)

    def insert(self, val: int) -> Node:
        """
        Insert a new value in BST.

        Returns
        =======
        int
            the new tree with the inserted value.
        """

        def ins(node: Node):
            if node is None:
                return Node(val)
            if node.val < val:
                node.right = ins(node.right)
            else:
                node.left = ins(node.left)
            return node

        return ins(self.root)

    def delete(self, val: int) -> Node:
        """
        Delete a value from the BST.

        Returns
        =======
        Node
            the new tree without that value
        """

        def get_successor(node: Node):
            cur = node.right
            while (next := cur.left) is not None:
                cur = next
                print(next)
            # swap root with nearest key
            nearest = cur.val
            self.delete(cur.val)
            node.val = nearest
            return node

        def dele(node: Node):
            if node is None:
                return None
            if node.val == val:
                if node.left and node.right:
                    return get_successor(node)
                if (uniq_child := node.left or node.right) is not None:
                    return uniq_child
                return None
            if node.val < val:
                node.right = dele(node.right)
            else:
                node.left = dele(node.left)
            return node

        return dele(self.root)

    def max(self) -> int:
        """
        Gets the maximum value in BST.

        Returns
        =======
        int
            maximum value
        """

        def find_max(node: Node):
            if node.right is None:
                return node
            return find_max(node.right)

        return find_max(self.root).val

    def min(self) -> int:
        """
        Gets the minimum value in BST.

        Returns
        =======
        int
            minimum value
        """

        def find_min(node: Node):
            if node.left is None:
                return node
            return find_min(node.left)

        return find_min(self.root).val

    def floor(self, val: int) -> int:
        """
        Given a number x find the floor of x in the BST.

        floor means the greatest value of BST which is smaller
        than or equal to x.

        Returns
        =======
        int
            the floor of x (-1 if not found any value smaller or eq to x)
        """
        def find_floor(node: Node):
            if node is None:
                return None
            if node.val == val: 
                return node.val
            if node.val > val: 
                return find_floor(node.left)
            return find_floor(node.right) or node.val

        return find_floor(self.root) or -1

    def ceil(self, val: int) -> int:
        """
        Given a number x find the ceil of x in the BST.

        ceil means the smaller value of BST which is greater
        than or equal to x.

        Returns
        =======
        int
            the ceil of x (-1 if not found any value greater or eq to x)
        """
        def find_ceil(node: Node):
            if node is None:
                return None
            if node.val == val:
                return node.val
            if node.val < val: 
                return find_ceil(node.right)
            return find_ceil(node.left) or node.val

        return find_ceil(self.root) or -1

    def _leftMost(node: Node) -> Node:
        if curr.left is None:
            return curr
        return leftMost(curr.left)

    # Succesors
    def inorder_succesor(self, val: int) -> int:
        def inord_succ(node: Node):
            pass
        return inord_succ(self.root)

    # Binary Tree Traversals (inorder, preorder and postorder)
    def inorder(self, callback: Callable[[Node], None]):
        def inord(node: Node):
            if node is None:
                return None
            inord(node.left)
            callback(node)
            inord(node.right)

        return inord(self.root)

    def preorder(self, callback: Callable[[Node], None]):
        def preord(node: Node):
            if node is None:
                return None
            callback(node)
            preord(node.left)
            preord(node.right)

        return preord(self.root)

    def postorder(self, callback: Callable[[Node], None]):
        def postord(node: Node):
            if node is None:
                return None
            postord(node.left)
            postord(node.right)
            callback(node)

        return postord(self.root)

    @staticmethod
    def _print_node(node: Node):
        print(f"{node.val}, ", end="")

    def print_inorder(self):
        self.inorder(self._print_node)

    def print_preorder(self):
        self.preorder(self._print_node)

    def print_postorder(self):
        self.postorder(self._print_node)

    def __str__(self):
        bst_str = ""

        def save(node: Node):
            nonlocal bst_str
            bst_str += str(node.val) + ", "

        self.inorder(save)
        return bst_str


if __name__ == "__main__":
    bst = BinarySearchTree(100)
    bst.insert(20)
    bst.insert(200)
    bst.insert(10)
    bst.insert(30)
    bst.insert(150)
    bst.insert(300)
    # inorder: 10 20 30 100 150 200 300
    # preorder: 100 20 10 30 200 150 300
    # postorder: 10 30 20 150 300 200 100
    print("[*] Binary Search Tree (report)")
    print("\n[*] Traversals")
    print("(inorder): ", end="")
    bst.print_inorder()
    print("\n(preorder): ", end="")
    bst.print_preorder()
    print("\n(postorder): ", end="")
    bst.print_postorder()
    print("\n\n[*] BST Extremum")
    print("[!] Max: ", bst.max())
    print("[!] Min: ", bst.min())
    print("")
    print("[*] Search Test")
    print("Search 20: ", bst.search(20))
    print("Search 25: ", bst.search(25))
    print("Search 30: ", bst.search(30))
    print("[*] Floor Test")
    print("Floor 210", bst.floor(210))
    print("Floor 150", bst.floor(150))
    print("Floor 25", bst.floor(25))
    print("Floor 5", bst.floor(5))
    print("[*] Ceil Test")
    print("Ceil 210", bst.ceil(210))
    print("Ceil 150", bst.ceil(150))
    print("Ceil 25", bst.ceil(25))
    print("Ceil 5", bst.ceil(5))
    print("Ceil 400", bst.ceil(400))
    print("\n[*] Delete Test")
    print("Deleting 10...")
    bst.delete(10)
    print("BST: ", bst)
    print("Deleting 10...")
    bst.delete(200)
    print("BST: ", bst)
