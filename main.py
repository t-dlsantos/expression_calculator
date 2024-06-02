import re
from Arvore.BinaryTree import NodeTree
from Pilha.Pilha import Pilha


class ExpressionAnalyzer:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/'])
        self.priority = {'+':1, '-':1, '*':2, '/':2}
    
