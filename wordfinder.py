from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,file_path):
        """creates a list of words from a text file"""
        self.file = open(file_path)
        self.list_of_words = [line.replace("\n","") for line in self.file]
        self.file.close()
        print(f"{len(self.list_of_words)} words read")

    def __repr__(self):
        return f"<WordFinder list_of_words contains {len(self.list_of_words)} words"

    def random(self):
        """returns a random word from the saved list of words"""
        return choice(self.list_of_words)





#instantiated with path to file of words
# prints out the number of the words?
# saves list of words behind the scenes

#random method
# grab random word from saved list and return it