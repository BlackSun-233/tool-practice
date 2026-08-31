from merge_sort import merge_sort

def test_normal():
    assert merge_sort([3,1,4,1,5,9,2,6]) == [1,1,2,3,4,5,6,9]

def test_dup():
    assert merge_sort([5,2,2,8,2]) == [2,2,2,5,8]
