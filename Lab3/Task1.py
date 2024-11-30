def singlets (t: str, k: int) -> List:
    """ Generate a multiset of k-shingles from a list of tokens.

    Args:
        t (str): _description_
        k (int): _description_

    Returns:
        List: _description_
    """
    # the check for the errors
    if (any([isinstance(t,str)])):
        return TypeError("Wrong  type of the data")
    if (k > len(t)):
        return ValueError(" Check the value of the k" )
    
    
    return 