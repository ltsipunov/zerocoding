import pytest
from vowels import count_vowels

@pytest.mark.parametrize("s, expected",[
    ('The quick brown fox jumps over the lazy dog',12),
    ('Cwm fjord bank glyphs vext quiz',6),
    ('Shh, hmm, gn, br',0),
    ('Brr, mmm, tsk', 0),
    ('Ia no au', 5 ),
    ('aauiiaa',7),
    ('The quick brOwn fOx jUmps ovEr thE lazy dOg',12),
])

def test_check_with_param(s, expected):
    assert count_vowels(s) == expected