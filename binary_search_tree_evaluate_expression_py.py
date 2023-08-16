import tkinter as tk
from tkinter import ttk

class BinarySearchTree:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.key = key

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = self.Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left:
                self._insert_recursive(node.left, key)
            else:
                node.left = self.Node(key)
        elif key > node.key:
            if node.right:
                self._insert_recursive(node.right, key)
            else:
                node.right = self.Node(key)

class EvalExpression:
    def evaluate(self, s: str) -> int:
        operators = ['-','+','*','/']
        operator_stack = []
        operand_stack = []
        result = 0
        tracker = 0
        i = 0
        j = 0

        while i < len(s):
            if s[i] in operators:
                if operator_stack:
                    operand_stack.append(int(s[tracker:j]))

                    while operator_stack and operators.index(s[i]) <= operators.index(operator_stack[-1]):
                        num_1 = operand_stack.pop()
                        num_2 = operand_stack.pop()
                        sign = operator_stack.pop()

                        if sign == '/':
                            result = num_2 // num_1
                        elif sign == '*':
                            result = num_2 * num_1
                        elif sign == '-':
                            result = num_2 - num_1
                        elif sign == '+':
                            result = num_2 + num_1

                        operand_stack.append(result)

                    operator_stack.append(s[i])

                else:
                    operand_stack.append(int(s[tracker:j]))
                    operator_stack.append(s[i])

                tracker = j + 1
                j = tracker
            else:
                j += 1
            i += 1

        operand_stack.append(int(s[tracker:j]))

        while operator_stack:
            num_1 = operand_stack.pop()
            num_2 = operand_stack.pop()
            sign = operator_stack.pop()

            if sign == '/':
                result = num_2 // num_1
            elif sign == '*':
                result = num_2 * num_1
            elif sign == '-':
                result = num_2 - num_1
            elif sign == '+':
                result = num_2 + num_1

            operand_stack.append(result)

        return operand_stack[0]

class BinarySearchTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Search Tree & Expression Evaluation")

        self.tree = BinarySearchTree()
        self.expression_evaluator = EvalExpression()

        self.label = ttk.Label(root, text="Enter a value:")
        self.label.pack()

        self.entry = ttk.Entry(root)
        self.entry.pack()

        self.insert_button = ttk.Button(root, text="Insert", command=self.insert_value)
        self.insert_button.pack()

        self.treeview = ttk.Treeview(root, columns=("Value"), show="headings")
        self.treeview.heading("Value", text="Value")
        self.treeview.pack()

        self.expression_label = ttk.Label(root, text="Enter an expression:")
        self.expression_label.pack()

        self.expression_entry = ttk.Entry(root)
        self.expression_entry.pack()

        self.evaluate_button = ttk.Button(root, text="Evaluate Expression", command=self.evaluate_expression)
        self.evaluate_button.pack()

    def insert_value(self):
        value = self.entry.get()
        if value.isdigit():
            value = int(value)
            self.tree.insert(value)
            self.update_treeview()

    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        self._update_treeview_recursive(self.tree.root)

    def _update_treeview_recursive(self, node):
        if node:
            self.treeview.insert("", "end", values=(node.key,))
            self._update_treeview_recursive(node.left)
            self._update_treeview_recursive(node.right)

    def evaluate_expression(self):
        expression = self.expression_entry.get()
        if expression:
            result = self.expression_evaluator.evaluate(expression)
            tk.messagebox.showinfo("Expression Result", f"The result is: {result}")

def main():
    root = tk.Tk()
    app = BinarySearchTreeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()