def mean(vals):
    """Computes the mean from a list of values."""
    try:
        total = float(sum(vals))
        length = len(vals)
    except TypeError:
        raise TypeError("The list was not numbers.")
    except:
        print "Something unknown happened with the list."
    return float(total)/length

def median(numlist):
    numlist.sort()
    length = len(numlist)
    index = length/2
    if length % 2 == 0:
       return mean([numlist[index], numlist[index - 1]])
    else:
       return numlist[index]

def mode(vals):
    """Computes the mode from a list of values."""
    pass

def std(vals):
    """Computes the standard deviation from a list of values."""
    n = len(vals)
    if n == 0:
        return 0.0
    mu = sum(vals) / n
    if mu == 1e500:
        return NotImplemented
    var = 0.0
    for val in vals:
        var = var + (val - mu)**2
    return (var / n)**0.5

def var(vals):
    """Computes the variance from a list of values."""
    pass
