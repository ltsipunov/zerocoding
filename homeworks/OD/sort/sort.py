import pytest
import bubble, heap, gnome, shell, radix

from random import sample


def standard(a):
    return sorted(a)


a10k = [ i for i in range(10_000)]
s10k = sample(a10k,10_000)
print(a10k[10:20],s10k[10:20],)

@pytest.mark.parametrize("a, expected",[
    ([1,6,2,5,3,4], [1,2,3,4,5,6]),
    ([-1,6,2,-5,-3, 4], [-5,-3,-1,2,4,6]),
    ([1], [1]),
    ([1,0], [0,1]),
    ([0,1], [0,1]),
    (s10k,a10k),
])

def test_check_with_param(a, expected):
    assert standard(a) == expected
    assert bubble.sort(a) == expected
    assert heap.sort(a) == expected
    assert gnome.sort(a) == expected
    assert shell.sort(a) == expected
    assert radix.sort(a) == expected
