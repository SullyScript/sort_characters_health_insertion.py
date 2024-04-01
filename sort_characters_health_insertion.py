# ECOR 1042 Lab 5 - Individual submission for sort_characters_health_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101236902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T055"

#==========================================#
# Place your sort_characters_health_insertion function after this line

def sort_characters_health_insertion(health: list[dict], order: str) -> list:
    """ Return providing dictionaries in acending or descending health orders, based on user defined input.
    order must be a string of value "A" or "D", health must be a dictionary
    
    >>> sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]
    
    >>> sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "D")
    [{'Occupation': 'H', 'Health': 62.71}, {'Occupation': 'EB', 'Health': 62.37}]
    
    >>> sort_characters_health_insertion([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    """
    
    n = len(health)
    
    for i in range(1,n):
        key = health[i]
        health_found = False
        
        for k,v in health[i].items():

            if k == "Health":
                health_found = True
        
        if health_found == False:
            print("'Health' key is not present")
            return health            
               
        health_value  = health[i]['Health']                  
                
        j = i - 1    
       
        if order == "A":
            while j >= 0 and health[j]['Health'] > health_value:
                health[j+1] = health[j]
                j -= 1
       
        else:
            while j >= 0 and health[j]['Health'] < health_value:
                health[j+1] = health[j]
                j -= 1            
            
        health[j+1] = key
             
    return health    
              
    
# Do NOT include a main script in your submission
