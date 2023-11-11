'''

Stack Data Structure 
'''

class Stack(): 
    def __init__(self): 
        self.items = [] 
    
    def push(self, item): 
        """Add an Item to the Stack 

        Args:
            item (str, int , ): Item to add at the Top of the Stack 
        """
        self.items.append(item)
    
    def pop(self): 
        """Removes the Top Element From the items 

        Args:
            items (list): a list of element in the stack 
        """
        return self.items.pop() 
    
    def is_empty(self) :
        """
        Return whether the Stack is empty or not 
        """
        if len(self.items) == 0 : 
            return True 
        return False  
        
    def peek(self): 
        """Returns the Top Element in the Stack 
        """
        if not(self.items): 
            return "No Element in the Stack"
        return self.items[-1]

def main() : 
    print("It is Just a Stack , Why are you running it ?")

if "__name__" == "__main__": 
    main() 
