from dataclasses import dataclass
from typing import Optional, Callable


@dataclass
class Node:
    val: int
    right: Optional["Node"] = None
    left: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self, root_val: int):
        self.root = Node(val=root_val)

    def search(self, val: int) -> bool:
        '''
        Search operation.
        Search for a value in the BST.
        
        Returns
        =======
        True if value found
        False if not found
        '''
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
        '''
        Insert a new value in BST.
        Returns
        =======
        the new tree with the inserted value.
        '''
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
        '''
        Delete a value from the BST.
        Returns
        =======
        the new tree without that value
        '''
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
    print("(inorder): ")
    bst.print_inorder()
    print("(preorder): ")
    bst.print_preorder()
    print("(postorder): ")
    bst.print_postorder()
    print("")

    print("BST (inorder): ", bst)
    print("Search 20: ", bst.search(20))
    print("Search 25: ", bst.search(25))
    print("Search 30: ", bst.search(30))

    print("Deleting 10...")
    bst.delete(10)
    print("BST: ", bst)
