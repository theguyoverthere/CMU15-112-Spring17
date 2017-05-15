#******************************************************************************#
# Author: Tarique Anwer
# Date:   14/5/2017
# Description: Background: In a Scrabble-like game, players each have a hand,
#              which is a list of lowercase letters. There is also a dictionary,
#              which is a list of legal words (all in lowercase letters). And
#              there is a list of letterScores, which is length 26, where
#              letterScores[i] contains the point value for the ith character in
#              the alphabet (so letterScores[0] contains the point value for
#              'a'). Players can use some or all of the tiles in their hand and
#              arrange them in any order to form words. The point value for a
#              word is 0 if it is not in the dictionary, otherwise it is the sum
#              of the point values of each letter in the word, according to the
#              letterScores list (pretty much as it works in actual Scrabble).
#              In case you are interested, here is a list of the actual
#              letterScores for Scrabble:
#              letterScores = [
#              #  a, b, c, d, e, f, g, h, i, j, k, l, m
#                 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
#              #  n, o, p, q, r, s, t, u, v, w, x, y, z
#                 1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10
#              ]
#              Note that your function must work for any list of letterScores as
#              is provided by the caller. With this in mind, write the function
#              bestScrabbleScore(dictionary, letterScores, hand) that takes 3
#              lists -- dictionary (a list of lowercase words), letterScores (a
#              list of 26 integers), and hand (a list of lowercase characters)
#              -- and returns a tuple of the highest-scoring word in the
#              dictionary that can be formed by some arrangement of some subset
#              of letters in the hand, followed by its score.
#              In the case of a tie, the first element of the tuple should
#              instead be a list of all such words in the order they appear in
#              the dictionary. If no such words exist, return None.
#              Note: there is no fixed dictionary here. Each time we call the
#              function, we may provide a different dictionary! It may contain
#              100 words or perhaps 100,00 words.
#******************************************************************************#
import string

# The Second Edition of the 20-volume Oxford English Dictionary contains full
# entries for 171,476 words in current use, and 47,156 obsolete words. To this
# may be added around 9,500 derivative words included as subentries.
# That's roughly, 2,28,000 words. A 9 letter word would produce 9! = 3,62,880
# combinations. If we go down the permutation route, we're looking at a
# nightmare!

def letterCounts(s):
    """
    Form a list with the count of letters present in the string s. The list is
    26 characters long, and represents the count of each of the letter present
    in the English alphabet.

    :param s: A string of characters.
    :return: A list with the count of letters in the string.

    """
    counts = [0] * 26

    for ch in s.upper():
        if (ch >= "A") and (ch <= "Z"):
            counts[ord(ch) - ord("A")] += 1

    return counts

def possibleToFormWord(word, hand):
    """
    Check to see if it is possible to form the word, with the characters
    available in the string "hand"

    :param word: A string, which is supposedly a valid word.
    :param hand: A string of lower-case characters
    :return: True if it is possible to form the word given with all or some of
           the letters available in the string "hand".
    """

    letterCountWord = letterCounts(word)
    letterCountHand = letterCounts(hand)

    for i in range(len(letterCountWord)):
        if letterCountWord[i] > letterCountHand[i]:
            return False

    return True

def computeWordScore(word, letterScores):
    """ Compute the word score.

    :param word: A string whose score needs to be computed.
    :param letterScores: A list of scores for each lowercase letter of the
           English alphabet.
    :return: Score as a positive integer.
    """
    score = 0

    for c in word:
        score += letterScores[ord(c) - ord('a')]

    return score

def bestScrabbleScore(dictionary, letterScores, hand):
    """
    bestScrabbleScore(dictionary, letterScores, hand) takes 3 lists --
    dictionary (a list of lowercase words), letterScores(a list of 26 integers),
    and hand (a list of lowercase characters) and returns a tuple of the
    highest-scoring word in the dictionary that can be formed by some
    arrangement of some subset of letters in the hand, followed by its score. In
    the case of a tie, the first element of the tuple is instead a list
    of all such words in the order they appear in the dictionary. If no such
    words exist, the function returns None.

    :param dictionary: A list of string elements, considered to be valid words.
    :param letterScores: A list of positive integers, representing scores of
           each lowercase letter of the English alphabet.
    :param hand: A list of characters available to form a valid word.
    :return: List of word(s) with the highest score, or None. If more than
           two words in the dictionary result in the same score, the words are
           returned as a list themselves.

           For example, the following returns are valid:
           a) ["Hello", "lloeH", 16]
           b) ["good", 10]
           c None
    """
    result = []
    possibleWords = []
    highestScore = 0

    for word in dictionary:
        if possibleToFormWord(word, "".join(hand)):
            score = computeWordScore(word, letterScores)

            if score >= highestScore:
                if score > highestScore:
                    possibleWords.clear()

                possibleWords.append(word)
                highestScore = score

    if not possibleWords:
        return None
    else:
        if len(possibleWords) > 1:
            result.append(possibleWords)
        else:
            result.append("".join(possibleWords))

        result.append(highestScore)
        return tuple(result)
