from main import negative_number


def test_negative_number():
    result = negative_number(-5)
    assert result, "Test failed for the ne number"


if __name__ == "__main__":
    test_negative_number()