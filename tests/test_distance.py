from mlproject.distance import haversine

def test_distance_type():
    assert type(haversine(1, 2, 3, 4)) == float
