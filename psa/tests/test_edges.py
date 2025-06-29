from psa.strength import grade

def test_empty():        assert grade("")          == "D"
def test_spaces():       assert grade("   ")       == "D"
def test_digits_only():  assert grade("123456")    == "C"
def test_symbols_only(): assert grade("@#$%^&*")   == "C"
