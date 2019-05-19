from euler import problem_004


class TestIsIntPalindrome:

    def test_2_digits(self):
        input = 99

        result = problem_004.is_int_palindrome(input)

        assert isinstance(result, bool)
        assert result is True

    def test_not_palindrome(self):
        input = 98

        result = problem_004.is_int_palindrome(input)

        assert isinstance(result, bool)
        assert result is False

    def test_1_digits(self):
        input = 0

        result = problem_004.is_int_palindrome(input)

        assert isinstance(result, bool)
        assert result is True

    def test_3_digits(self):
        input = 999

        result = problem_004.is_int_palindrome(input)

        assert isinstance(result, bool)
        assert result is True
