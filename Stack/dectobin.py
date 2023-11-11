

from basic_stack import Stack 

def convert_int_to_bin(dec_num : int ): 
    """dec to bin converted 

    Args:
        dec_num (int): decimal number 

    Returns:
        result(str): binary number 
    """
    if dec_num == 0 : 
        return "0" 
    my_stack = Stack() 
    while dec_num >0: 
        remainder = dec_num % 2 
        my_stack.push(remainder)
        dec_num //=2 

    result = ""
    while not(my_stack.is_empty()): 
        result += str(my_stack.pop())

    return result 

print(convert_int_to_bin(56))