''' 
Program to Check if the Brackets are Balanced or Not? 
'''
from basic_stack import Stack 


def is_match(p1, p2 ): 
    """Returns whether two bracket are a match 

    Args:
        p1 (str): a bracket
        p2 (str): another pracket
    """
    if p1 == "(" and p2 == ")": 
        return True 
    elif p1 == "{" and p2 == "}":
        return True 
    elif p1 == "[" and p2 == "]":
        return True 
    else : 
        return False 
    
def is_balanced(text: str):
    """Returns if the Bracket is balanced or not 

    Args:
        text (str): a collection of bracket 

    Returns:
        bool: True if its balanced and False Otherwise 
    """
    s = Stack()
    balanced = True
    index = 0

    while index < len(text) and balanced:
        paren = text[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    balanced = False
                    break
        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_balanced("[][]"))


