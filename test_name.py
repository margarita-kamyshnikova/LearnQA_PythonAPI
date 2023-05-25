class TestPhrase:
    def test_phrase_checker(self):
        phrase = input("Set a phrase: ")
        assert (len(phrase) < 15), f"The phrase's length is more than 15 characters"