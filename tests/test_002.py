from euler import problem_002


class TestGetFibonacciList:

    def test_get_first_5(self):
        limit = 10
        expected = [1, 2, 3, 5, 8]

        result = problem_002.get_fibonacci_list(limit)

        assert isinstance(result, list)
        assert result == expected
        assert all(item < limit for item in result)


class TestRmOddNumbers:

    def test_odd_removal(self):
        input = [1, 2, 3]
        expected = [2]

        result = problem_002.rm_odd_numbers(input)

        assert isinstance(result, list)
        assert result == expected

    def test_no_odds(self):
        input = [2, 4]

        result = problem_002.rm_odd_numbers(input)

        assert result == input
