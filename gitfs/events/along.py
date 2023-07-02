"""
>>> AtomicLong
<class 'along.AtomicLong'>
"""
from cffi import FFI
from functools import total_ordering


ffi = FFI()
ffi.cdef("""
long long_add_and_fetch(long *, long);
long long_sub_and_fetch(long *, long);
long long_bool_compare_and_swap(long *, long, long);
""")
lib = ffi.verify("""
long long_add_and_fetch(long *v, long l) {
    return __sync_add_and_fetch(v, l);
};

long long_sub_and_fetch(long *v, long l) {
    return __sync_sub_and_fetch(v, l);
};

long long_bool_compare_and_swap(long *v, long o, long n) {
    return __sync_bool_compare_and_swap(v, o, n);
};
""")


@total_ordering
class AtomicLong(object):
    """
    >>> along = AtomicLong(0)
    >>> along.value
    0
    >>> along == 0
    True
    >>> along >= 1
    False
    >>> along <= 1
    True
    >>> along += 1
    >>> along == 1
    True
    >>> along -= 2
    >>> along == 1
    False
    >>> along == -1
    True
    """
    def __init__(self, initial_value):
        """
        >>> AtomicLong(0) # doctest: +ELLIPSIS
        <along.AtomicLong object at 0x...>
        """
        #print("__init__")
        self._storage = ffi.new('long *', initial_value)

    @property
    def value(self):
        """
        >>> along = AtomicLong(0)
        >>> along.value
        0
        """
        #print("value")
        return self._storage[0]

    def __iadd__(self, inc):
        """
        >>> along = AtomicLong(0)
        >>> along.__iadd__(5) # doctest: +ELLIPSIS
        <along.AtomicLong object at 0x...>
        >>> along.value
        5
        """
        lib.long_add_and_fetch(self._storage, inc)
        #print("iadd")
        return self

    def __isub__(self, dec):
        """
        >>> along = AtomicLong(0)
        >>> along.__isub__(5) # doctest: +ELLIPSIS
        <along.AtomicLong object at 0x...>
        >>> along.value
        -5
        """
        lib.long_sub_and_fetch(self._storage, dec)
        #print("isub")
        return self

    def __eq__(self, other):
        """
        >>> along = AtomicLong(0)
        >>> along.__eq__(5)
        False
        """
        #print("__eq__")
        return self.value == other

    def __le__(self, other):
        """
        >>> along = AtomicLong(0)
        >>> along.__le__(5)
        True
        """
        #print("__le__")
        return self.value <= other

    def __ge__(self, other):
        """
        >>> along = AtomicLong(0)
        >>> along.__ge__(5)
        False
        """
        #print("__ge__")
        return self.value >= other
