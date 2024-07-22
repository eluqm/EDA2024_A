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
