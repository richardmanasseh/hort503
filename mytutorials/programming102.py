# Basic Programming: Data Types/Structures
    Type I: Sequence
        > inside sequence, elements have a sequential order
        > because sequence elements have a sequential order, they can be:
            -indexed
            -sliced
            -iterated
        > well-known exampes are strings, lists, and tuples
        
    Type II: Unordered data
        > Common types are dictionaries and sets:
            -a dictionary stores relationships between a key and value
            -a set is just an unordered collection of values
         
        Boolean
        NumPy arrays
        Dataframes
        Integers
        Floats
        
Type I: SEQUENCE
    A: Strings:
            >is a type of sequence of symbols or characters delimited by '', "", or """ (double triple quotes)
            >so the following strings are equivalent:
                'this is a string'
                "this is a string"
                """this is a string"""
                
            > we can insert another a string delimited by one type of quote into another delimited by a different quote:
                """this is a 'python' string"""
                
                -the important thing is if we begin a string with a type of quote, we must end it with the same:
                
                    """this is a 'python' string" would return an end-of-line (EOL) error
            
            > we can use the """ (double triple quotes) to indicate multi-line strings (aka block string):
                """this 'python' code
                   is not complete yet,
                   but good work, nonetheless"""
                 
            > the character '\l' represents an EOL character. Therefore, the code above could have been written
                in one line as:
                
                  """this 'python' code \l is not complete yet,\l but good work, nonetheless"""
                
    
            
            
