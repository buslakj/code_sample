from sample_2.sample import compare_lists, converts_columns_to_lists_helper, gen_similarity_score


def test_small_data_set():
    file = 'sample_2/tests/data1.txt'
    l1, l2 = converts_columns_to_lists_helper(file)

    comparison = compare_lists(l1, l2)
    similarity = gen_similarity_score(l1,l2)

    assert l1 == sorted([3, 4, 2, 1, 3, 3])
    assert l2 == sorted([4, 3, 5, 3, 9, 3])
    assert comparison == 11
    assert similarity == 31
    