#collections: Counter, namedtuple,defaultdict, deque
#itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
