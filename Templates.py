class Node:
    def __init__ (self, key, value, name=""):
        self.left=None
        self.right=None
        self.key=key
        self.value=value
        self.name=name
        
        def __str__ (self):
            return str(self.key)
        
class BinaryTree:
    root=None
    
    def insert(self, root, n):
        if root is None:
            self.root=n
            return
        
        if n.key<root.key:
            if root.left is None:
                root.left=n
            else:
                self.insert(root.left, n)
        elif n.key>root.key:
            if root.right is None:
                root.right=n
            else:
                self.insert(root.right, n)
    
    
    def search(self, root, key):
        if root is None:
            return False
        if root.key==key:
            return  True
        else:
            if key< root.key:
                return self.search(root.left, key)
            else:
                return self.search(root.right, key)

    def delete(self, root, key):
        global time
        time+=1
        if root is None:
            return None
            
        if key<root.key:
            root.left=self.delete(root.left, key)
        elif key>root.key:
            root.right=self.delete(root.right, key)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.right
                root=None
                return temp
            
            temp=self.min_val(root.right)
            root.key=temp.key
            root.right=self.delete(root.right,temp.key)
        return root

    def print_post(self, root):
        if root is not None:
            self.print_post(root.left)
            self.print_post(root.right) 
            print(root.key)
            

            