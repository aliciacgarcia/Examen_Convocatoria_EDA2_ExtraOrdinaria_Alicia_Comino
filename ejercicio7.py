class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def build_tree(symbols_and_frequencies):
    nodes = [Node(symbol, frequency) for symbol, frequency in symbols_and_frequencies]
    
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        new_node = Node(None, left.frequency + right.frequency)
        new_node.left = left
        new_node.right = right
        
        nodes.append(new_node)
    
    return nodes[0]

def build_code_table(root, code=''):
    if root.symbol:
        return {root.symbol: code}
    else:
        return {**build_code_table(root.left, code + '0'), **build_code_table(root.right, code + '1')}

def compress(message, code_table):
    return ''.join([code_table[c] for c in message])

def decompress(compressed_message, root):
    message = ''
    current_node = root