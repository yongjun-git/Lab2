import Lab2

def test_calc_average():
    result = Lab2.calc_average([10.0, 20.0, 30.0])
    assert result == 20.0

def test_find_min_max():
    result = Lab2.find_min_max([30.0, 25.0, 28.0])
    assert result == [25.0, 30.0]

def test_median_odd():
    result = Lab2.calc_median_temperature([30.0, 25.0, 28.0])
    assert result == 28.0

def test_median_even():
    result = Lab2.calc_median_temperature([30.0, 25.0, 28.0, 26.0])
    assert result == 27.0