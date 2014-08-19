#!/usr/bin/env python
import _scs_direct
import _scs_indirect
from warnings import warn
from numpy import transpose 
from scipy import sparse

def solve(probdata, cone, **kwargs):
    """
    solves convex cone problems
     
    @return dictionary with solution with keys:
         'x' - primal solution
         's' - primal slack solution
         'y' - dual solution
         'info' - information dictionary
    """
    if not probdata or not cone:
        raise TypeError("Missing data or cone information")

    if not 'A' in probdata or not 'b' in probdata or not 'c' in probdata:
        raise TypeError("Missing one or more of A, b, c from data dictionary")
    A = probdata['A']
    b = probdata['b']
    c = probdata['c']

    warm = {}
    if 'x' in probdata:
        warm['x'] = probdata['x']
    if 'y' in probdata:
        warm['y'] = probdata['y']
    if 's' in probdata:
        warm['s'] = probdata['s']

    if A is None or b is None or c is None:
        raise TypeError("Incomplete data specification")
    if sparse.issparse(A):
        warn("Converting A to a dense matrix")
        A = A.todense()

    if sparse.issparse(b):
        b = b.todense()

    if sparse.issparse(c):
        c = c.todense()

    m, n = A.shape

    # A is stored in ROW MAJOR order, so we need to transpose:
    if kwargs.get('use_indirect', False):
        return _scs_indirect.csolve((m, n), A.T, b, c, cone, warm, **kwargs)
    else:
        return _scs_direct.csolve((m, n), A.T, b, c, cone, warm, **kwargs)
