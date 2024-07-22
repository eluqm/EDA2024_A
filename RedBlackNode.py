class RedBlackNode:
    def __init__(self, cancion):
        self.cancion = cancion
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'

class RedBlackTree:
    def __init__(self):
        self.TNULL = RedBlackNode(None)
        self.TNULL.color = 'black'
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
    
    def insert(self, cancion, clave):
        node = RedBlackNode(cancion)
        node.parent = None
        node.cancion = cancion
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if clave == 'popularidad':
                if node.cancion.popularidad < x.cancion.popularidad:
                    x = x.left
                else:
                    x = x.right
            elif clave == 'año':
                if node.cancion.año < x.cancion.año:
                    x = x.left
                else:
                    x = x.right
            elif clave == 'duracion':
                if node.cancion.duracion < x.cancion.duracion:
                    x = x.left
                else:
                    x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif clave == 'popularidad':
            if node.cancion.popularidad < y.cancion.popularidad:
                y.left = node
            else:
                y.right = node
        elif clave == 'año':
            if node.cancion.año < y.cancion.año:
                y.left = node
            else:
                y.right = node
        elif clave == 'duracion':
            if node.cancion.duracion < y.cancion.duracion:
                y.left = node
            else:
                y.right = node

        if node.parent == None:
            node.color = 'black'
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black' 

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y   
    
    def in_order_traversal(self, ascendente):
        res = []
        self._in_order_helper(self.root, res, ascendente)
        return res

    def _in_order_helper(self, node, res, ascendente):
        if node != self.TNULL:
            self._in_order_helper(node.left if ascendente else node.right, res, ascendente)
            if node.cancion:
                res.append(node.cancion)
            self._in_order_helper(node.right if ascendente else node.left, res, ascendente)
