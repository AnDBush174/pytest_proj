from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(["a", "b", "c"], 5, None) is None
    assert arrs.get(["x", "y", "z"], -1, "default") == "z"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert arrs.my_slice([], 0, 2) == []
    assert arrs.my_slice(["a", "b", "c", "d"], 0, -1) == ["a", "b", "c"]
    assert arrs.my_slice([1, 2, 3, 4, 5], -1) == [5]

def test_empty_slice():
    assert arrs.my_slice([], 0, 2) == []

