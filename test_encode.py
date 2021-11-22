from hypothesis import given
from hypothesis.strategies import text    
from encode import *

@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
