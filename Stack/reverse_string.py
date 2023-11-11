from basic_stack import Stack


def rev_string(text:str): 
    """Reverses a String 

    Args:
        text (str): string to reverse 

    Returns:
        result(str): reversed string 
    """
    mystack = Stack() 
    result = "" 
    for char in text: 
        mystack.push(char) 
    while not(mystack.is_empty()): 
        result += mystack.pop() 
    return result  

print(rev_string("Hello"))