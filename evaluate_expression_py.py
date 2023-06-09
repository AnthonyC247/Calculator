class EvalExpression():
  
  def evaluate(self, s: str) -> int:
    
    '''Two stacks used. One for the operands to be stored as integers.
    The second one is for the operators as a stack of characters.'''

    operators = ['/','*','+','-'] #A list of strings of all of the mathematical operations 
    operator_stack = [] #To append the operator strings into the stack 
    operand_stack = [] # #To append the operands strings into the stack 
    result = 0 ##Result of the operation being added to the stack 
    tracker = 0 # Tracker starts off to look at the beginning of the string 
    i = 0 #keep track of each character in string
    j = 0 #keep track of each character in string 

    '''Start by iterating through the input string and examining each character'''

    while i < len(s): #Iterating through input string and keeping tracking of length
      if s[i] in operators: #Check if a operator is located inside the opss list 
        if operator_stack: #If so...
          operand_stack.append(int(s[tracker:j]))

          '''With the input string, start to iterate through each character
          if a character where any number will be converted to an integer.
          Then pop a operand from the operand stack and another one and performing mathematical operations.
          '''

          if s[i] == '*' or s[i] == '/': #If the character within the string is a multiplication or division sign 
                      num_1 = operand_stack.pop() #Take out the first number located in the string 
                      num_2 = operand_stack.pop() #Take out the second number located in the string
                      sign = operator_stack.pop() #Take out the first sign located in the string

                      if sign == '*': #If the sign is division
                        result = num_2 * num_1 #divide both the second and first number popped from before
                        operand_stack.append(result) #Push or add that result to the operand_stack

                      elif sign == '/': #If the sign is multiplication 
                        result = num_2 // num_1 #multiply both the second and first number popped from before
                        operand_stack.append(result) #Push or add that result to the operand_stack

                      else:
                        #operator_stack.append(sign)
                        operand_stack.append(num_2) #Put away the second number in the operand_stack
                        operand_stack.append(num_1) #Put away the first number in the operand_stack 
                        operator_stack.append(sign) #Put away the sign in the operator_stack 
                      operator_stack.append(s[i]) #Put the string character from the input away in the operator_stack

          if s[i] == '+' or s[i] == '-': #If any addition or subtraction signs are located in the string 
                      num_1 = operand_stack.pop() #Take out the first number from the operand_stack
                      num_2 = operand_stack.pop() #Take out the second number from the operand_stack
                      sign = operator_stack.pop() #Take either sign first encountered from the operator_stack

                      if sign == '+': #If addition sign is encountered
                        result = num_2 + num_1 # perform addition 
                        operand_stack.append(result) #Add the new result to the operand_stack list 

                      elif sign == '-':
                        operand_stack.append(result)

                      else:
                        operator_stack.append(sign) #Any of the signs will be pushed to the operator_stack
                        operand_stack.append(num_2) #Put away the second number in the operand_stack
                        operand_stack.append(num_1) #Put away the second number in the operand_stack 
                      operator_stack.append(s[i]) # Put the sign used into operator_stack taken as a string character

        else:
          operand_stack.append(int(s[tracker:j]))
          operator_stack.append(s[i])
        tracker = j + 1
        j = tracker
      else:
        j += 1
      i += 1

    operand_stack.append(int(s[tracker:j]))
    num_1 = operand_stack.pop()
    num_2 = operand_stack.pop()
    sign = operator_stack.pop()



    if sign == '*':
      result = num_2 * num_1
      operand_stack.append(result)
    elif sign == '/':
      result = num_2 // num_1
      operand_stack.append(result)

    elif sign == '+':
      result = num_2 + num_1
      operand_stack.append(result)

    elif sign == '-':
      result = num_2 - num_1
      operand_stack.append(result)

    res = 0

    while len(operand_stack) > 1:
      num_1 = operand_stack.pop()
      num_2 = operand_stack.pop()
      operator = operator_stack.pop()

      #if operator == '-':
          #res = num_2 - num_1
      #elif operator == '+':
        #res = num_2 + num_1
      #operand_stack.append(res)

      '''In the code above, with size of Operator stack greater than 0 and operator on top 
      of the stack has precedence greater than or equal 
      to current character'''
      '''Now, when the operator stack is empty, you have the result at the top of the operand stack. Return that result'''
    return operand_stack[0]
