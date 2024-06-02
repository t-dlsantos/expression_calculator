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
    
    def _infix_to_postfix(self, tokens):
        stack = Pilha()
        output = []
        for token in tokens:
            if token.isdigit():
                output.append(token)
                print(f'output = {output}')
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())

                stack.pop()  # Remove '('
            else:  # Operator
                while (not stack.is_empty() and stack.peek() != '(' and
                       self.priority[token] <= self.priority[stack.peek()]):
                    output.append(stack.pop())
                stack.push(token)
        while not stack.is_empty():
            output.append(stack.pop())
        print(f'output = {output}')
        """
        Separa os numeros e operadores da expressão
        """
        return output
