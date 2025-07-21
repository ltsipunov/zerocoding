import pytest
import bubble, selection, insertion, quick, merge, heap, gnome, shell, radix, bucket, counting

from random import sample

def standard(a):
    return sorted(a)

a10k = [ i for i in range(10_000)]
s10k = sample(a10k,10_000)

@pytest.mark.parametrize("a, expected",[
    ([1,6,2,5,3,4], [1,2,3,4,5,6]),
    ([-1,6,2,-5,-3, 4], [-5,-3,-1,2,4,6]),
    ([1], [1]),
    ([1,0], [0,1]),
    ([0,1], [0,1]),
    # (s10k,a10k),
])
def test_small(a, expected):
    assert standard(a) == expected
    assert bubble.sort(a) == expected
    assert insertion.sort(a) == expected
    assert selection.sort(a) == expected
    assert quick.sort(a) == expected
    assert merge.sort(a) == expected
    assert heap.sort(a) == expected
    assert gnome.sort(a) == expected
    assert shell.sort(a) == expected
    assert radix.sort(a) == expected
    assert bucket.sort(a) == expected
    assert counting.sort(a) == expected

@pytest.mark.parametrize("a, expected",[
    (s10k,a10k),
])
def test_medium(a, expected):
    assert quick.sort(a) == expected
    assert heap.sort(a) == expected
    assert gnome.sort(a) == expected
    assert shell.sort(a) == expected
    assert radix.sort(a) == expected
    assert bucket.sort(a) == expected