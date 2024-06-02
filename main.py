import re
from Arvore.BinaryTree import NodeTree
from Pilha.Pilha import Pilha


class ExpressionAnalyzer:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/'])
        self.priority = {'+':1, '-':1, '*':2, '/':2}
    
    def _is_operator(self, c):
        return c in self.operators

    def _tokenize(self, expression):
        """ Separando cada caratere de texto """
        return re.findall(r'\d+|[+/*()-]', expression)
