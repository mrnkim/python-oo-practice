from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,file_path):
        """creates a list of words from a text file"""
        print('i am inside my parent')
        file = open(file_path)
        self.list_of_words = self.read_file(file)
        print(f"{len(self.list_of_words)} words read")

    def read_file(self, file):
        return [line.strip() for line in file]

    def __repr__(self):
        return f"<WordFinder list_of_words contains {len(self.list_of_words)} words"

    def random(self):
        """returns a random word from the saved list of words"""
        return choice(self.list_of_words)


class SpecialWordFinder(WordFinder):

    # def __init__(self, file_path):
    #     # super().__init__(file_path)
    #     # SpecialWordFinder.remove_sharp_and_blank(self)

    def read_file(self, file):
        return [line for line in super().read_file(file) if not line.startswith("#") and line != '']



