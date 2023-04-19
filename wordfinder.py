from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,file_path):
        """creates a list of words from a text file"""
        WordFinder.open_and_make_read_list(file_path)
        print(f"{len(self.list_of_words)} words read")

    @classmethod
    def open_and_make_read_list(self, file_path):
        self.file = open(file_path)
        self.list_of_words = [line.replace("\n","") for line in self.file]
        self.file.close()
        return self.list_of_words

    def __repr__(self):
        return f"<WordFinder list_of_words contains {len(self.list_of_words)} words"

    def random(self):
        """returns a random word from the saved list of words"""
        return choice(self.list_of_words)


class SpecialWordFinder(WordFinder):

    def __init__(self, file_path):
        super().__init__(file_path)
        SpecialWordFinder.remove_sharp_and_blank(self)

    def remove_sharp_and_blank(self):
        self.new_list_of_words = [line for line in self.list_of_words if line.startswith("#")==False or line.isspace()==False]
        return self.new_list_of_words



