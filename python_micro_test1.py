def bit_count(A, B):
    """
    This function will returnt the total count of the 1 bit in a output
    Args: Integer
    Output: Integer
    """
    out = A * B 
    bin_out = bin(out)
    count = bin_out.count("1")
    print(count)


bit_count(3, 7)