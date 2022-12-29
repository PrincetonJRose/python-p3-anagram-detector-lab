# your code goes here!
class Anagram:
    pass
    def __init__( self, word ):
        self.word = word

    def match( self, words ):
        pass
        anagrams = []
        split_word = list( self.word )
        split_word.sort()
        for word in words:
            w = list( word )
            w.sort()
            if w == split_word:
                anagrams.append( word )
        if anagrams:
            return anagrams
        else: return []
