from euler import problem_001


class TestGetModuleList:

    def test_get_modulo_list(self):
        start = 1
        end = 2
        divisble = 1

        result = problem_001.get_modulo_list(start, end, divisble)

        assert isinstance(result, list)
        assert len(result) == 1


class TestMergeLists:

    def test_remove_dups(self):
        a = [1, 2]
        b = [2, 3]

        expected = [1, 2, 3]

        result = problem_001.merge_lists(a, b)

        assert isinstance(result, list)
        assert len(result) == 3
        assert result == expected

