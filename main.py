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
    
    def _construct_tree(self, postfix_tokens):

        stack = Pilha()
        for token in postfix_tokens:
            if token.isdigit():
                node = NodeTree(token)
                stack.push(node)
            else:
                node = NodeTree(token)
                node1 = stack.pop()
                node2 = stack.pop()
                node.right = node1
                node.left = node2
                stack.push(node)
                print(f'Created node with operator {token}: left={node.left.key}, right={node.right.key}')
        return stack.pop()
    
    def _evaluate_tree(self, root):
        if root.left is None and root.right is None:
            return int(root.key)
        left_val = self._evaluate_tree(root.left)
        right_val = self._evaluate_tree(root.right)
        if root.key == '+':
            return left_val + right_val
        elif root.key == '-':
            return left_val - right_val
        elif root.key == '*':
            return left_val * right_val
        elif root.key == '/':
            return left_val / right_val

    def evaluate_expression(self, expression):
        tokens = self._tokenize(expression)
        postfix_tokens = self._infix_to_postfix(tokens)
        ast_root = self._construct_tree(postfix_tokens)
        return self._evaluate_tree(ast_root)

# Exemplo de uso:
# expression = "3 + 5 * ( 2 - 8 )"  # 3 + 5 * -6 = 3 - 30 = -27
expression = "2 + 3 * ( 2 - 900 )"
analyzer = ExpressionAnalyzer()
result = analyzer.evaluate_expression(expression)
print(f"O resultado da expressão '{expression}' é {result}")