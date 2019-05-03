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
                
    String Manipulations
        i) Strings are immutable meaning, once created, it cannot be modified. If you need to change a string, what you can do is make a derived/derivated string:
            > signal_peptide = 'MASKATLLLAFTLLFATCIA' # the string signal_peptide holds the amino acid sequence capitalized
            > to get a lower case version of the string, we use the method lower():
                >>>signal_peptide.lower():
                    'maskatlllaftllfatcia'
                    
              - the original string is still not modified and returns the initial aa sequence when called:
               >>>signal_peptide:
                   'MASKATLLLAFTLLFATCIA'
                   
              - we can make this new string to have the same name as the previous one, by simply renaming it:
              
                  signal_peptide = signal_peptide.lower() 
                  
                  >>>signal_peptide
                      'maskatlllaftllfatcia'
                      
                     the net effect is like we had modified the original string
        
        ii) Replace old portion of a string with new: 
            replace(old, new)
                >>>DNAseq = "TTGCTAG"
                >>>mRNAseq = DNAseq.replace('T', 'U')
                >>> mRNAseq
                    'UUGCUAG'
                    .
             If the optional argument 'count' is used, only the first count occurences/instnances of old will be replaced:
                    >>>nascent_mRNAseq = DNAseq.replace('T', 'U', 1)
                    >>>nascent_mRNAseq
                    '"TTGCTAG"
                    
                    >>> nascent_mRNAseq2 = DNAseq.replace('T', 'U', 2)
                    >>> nascent_mRNAseq2
                        'UUGCTAG'
                    >>>
        iii) Count how many times a substring appears between start and end position (if specified): the count() function
            The count() function has one compulsory and two optional parameters:
                > Mandatory paramater: 1)substring – string whose count is to be found.
                >Optional Parameters:
                    1)start (Optional) – starting index within the string where search starts.
                    2)end (Optional) – ending index within the string where search ends.
                   
                   >>> t = DNAseq.count('T')
                   >>> t
                        3
                        
                   >>> t1 = DNAseq.count('T', 1,3)
                    >>> t1
                        1

                   >>> t4 = DNAseq.count('T', 0,4)
                   >>> t4
                        2
       
               >>> c = DNAseq.count('C')
               >>> g = DNAseq.count('G')
                >>> float(c+g)/len(DNAseq)*100 # the float function is used to force a floating point result (%CG content), but this is not required in Python 3
                    42.857142857142854
                    
                    
        iv)
