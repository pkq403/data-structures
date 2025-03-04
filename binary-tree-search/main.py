from dataclasses import dataclass
from typing import Optional, Type


@dataclass
class Node:
    val: int
    right: Optional["Node"] = None
    left: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self, root_val: int):
        self.root = Node(val=root_val)

    def search(self, val: int) -> bool:
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

    def __str__(self):
        bst_str = ""

        def save(new_str: str):
            nonlocal bst_str
            bst_str += new_str

        def inorder(node: Node):
            if node is None:
                return None
            inorder(node.left)
            save(str(node.val) + ", ")
            inorder(node.right)

        inorder(self.root)
        return bst_str


if __name__ == "__main__":
    bst = BinarySearchTree(8)
    bst.insert(4)
    bst.insert(5)
    bst.insert(10)
    bst.insert(12)
    bst.insert(14)
    bst.insert(9)
    # 4, 5, 8, 9, 10, 12

    print("BST: ", bst)
    print("Search 5: ", bst.search(5))
    print("Search 7: ", bst.search(7))
    print("Search 12: ", bst.search(12))

    print("Deleting 10...")
    bst.delete(10)
    print("BST: ", bst)
