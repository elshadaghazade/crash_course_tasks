def open_file():
    ''' Remember the docstring'''
    pass # this is a placeholder that you will replace with Python code


def read_file(fp):  
    ''' Remember the docstring'''
    # Read n and initizlize the network to have n empty lists -- 
    #    one empty list for each member of the network
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])

    # You need to write the code to fill in the network as you read the file
    # Hint: append appropriate values to the appropriate lists.
    # Each iteration of the loop will have two appends -- why?

    return network

def num_in_common_between_lists(list1, list2):
    ''' Remember the docstring'''
    pass # this is a placeholder that you will replace with Python code

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' Remember the docstring'''
    pass # this is a placeholder that you will replace with Python code

def recommend(user_id,network,similarity_matrix):
    ''' Remember the docstring'''
    pass # this is a placeholder that you will replace with Python code
    
def main():
    # by convention "main" doesn't need a docstring
    pass # this is a placeholder that you will replace with Python code
    
if __name__ == "__main__":
    main()
