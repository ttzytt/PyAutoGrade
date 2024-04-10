from test_case import *
import sys 
sys.path.append('./../../src/')
from test_case import  PrewrittenFileCase as pf, PrewrittenScriptCase as ps
import random
import io
import string

def gen_random_file(
                    file_len : int,
                    use_punctuation : bool = True, 
                    use_digits : bool = True, 
                    use_whitespace : bool = True, 
                    ) -> io.StringIO: 
    rand_str = ""
    charset = string.ascii_letters
    if use_punctuation: charset += string.punctuation
    if use_digits: charset += string.digits
    if use_whitespace: charset += string.whitespace
    for _ in range(file_len):
        rand_str += random.choice(charset)
    return io.StringIO(rand_str)


def gen_file_assert_eq(string : str, expected : Any, tested_func_name : str, *extra_args, **extra_kwargs) -> PrewrittenScriptCase:
    peb = ps.EvaluatorBuilder()
    f = io.StringIO()
    f.write(string)
    f.seek(0)
    return ps(peb.assert_eq(expected, f, *extra_args, **extra_kwargs), tested_func_name)

def average_length_sol(read_file):
    total_length = 0
    total_words = 0
    # Iterate over each line in the file
    for line in read_file:
        # Split the line into words
        words = line.split()
        # Update total words count
        total_words += len(words)
        # Update total length count by summing the lengths of each word
        total_length += sum(len(word) for word in words)

    # Calculate the average length
    if total_words > 0:
        average_length = total_length / total_words
    else:
        average_length = None  # Handle the case when there are no words in the file
    return average_length

def longest_word_sol(read_file):
    longest_words = []
    max_length = 0
    # Iterate over each line in the file
    for line in read_file:
        # Split the line into words
        words = line.split()
        # Iterate over each word in the line
        for word in words:
            # Remove any punctuation from the word
            word = ''.join(char for char in word if char.isalnum())
            # Check if the current word is longer than the current longest word
            if len(word) > max_length:
                max_length = len(word)
                longest_words = [word]
            elif len(word) == max_length:
                # If the current word has the same length as the longest word, add it to the list
                longest_words.append(word)
    return longest_words
    
def longest_palindrome_sol(read_file):
    longest_palindromes = []
    max_length = 0

    for line in read_file:
        words = line.split()
        
        for word in words:
            # Remove any punctuation from the word and convert to lowercase
            word = ''.join(char for char in word if char.isalnum()).lower()
            
            # Check if the word is a palindrome
            if word == word[::-1]:
                # If the word is a palindrome and its length is greater than the current maximum length
                if len(word) > max_length:
                    max_length = len(word)
                    longest_palindromes = [word]
                elif len(word) == max_length:
                    # If the word is a palindrome and its length is equal to the current maximum length
                    longest_palindromes.append(word)

    return longest_palindromes

def all_vowels_counter_sol(read_file):
    count = 0
    
    for line in read_file:
        words = line.split()
        
        for word in words:
            # Convert the word to lowercase for case-insensitive comparison
            word_lower = word.lower()
            # Check if all vowels are present in the word
            if 'a' in word_lower and 'e' in word_lower and 'i' in word_lower and 'o' in word_lower and 'u' in word_lower:
                count += 1
    
    return count

def count_long_lines_sol(read_file, min_length):
    num_long_lines = 0

    for line in read_file:
        # Check if the length of the line is at least min_length
        if len(line) >= min_length:
            num_long_lines += 1

    return num_long_lines



def test_case_constructor() -> list[TestCase]:

    test_cases : list[TestCase] = []
    peb = ps.EvaluatorBuilder()
    TESTED_FUNC_NAME = "average_length"
    file_param_assert_eq = lambda string, expected: gen_file_assert_eq(string, expected, TESTED_FUNC_NAME)
    _ps = lambda evaluator, msg = "": ps(evaluator, TESTED_FUNC_NAME, msg)
    # -------- T1 ---------
    test_cases.extend([
       file_param_assert_eq(
            "Foxes eat rabbits.\nhug a fox.", 4
        ),
        file_param_assert_eq(
            "Foxes eat rabbits. Four. Seven. Thisistest.\nhug a fox.", 5.111111111111111
        ),
        file_param_assert_eq(
            "a a a a a b b b b", 1
        ),
        file_param_assert_eq(
            "ab cd ef gh ij kl", 2
        ),
        file_param_assert_eq(
            "a ab \t a \n ab \n a ab a ab", 1.5
        ),
        file_param_assert_eq(
            "Thisisonewordhoweverlongitmayseem", 33
        ),
        file_param_assert_eq(
            "Hyphen-hyphen another word", 8
        ),
        file_param_assert_eq(
            "Apostraphe's another word", 7.666666666666667
        ),
        file_param_assert_eq(
            "", None
        ),
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(1000)
            )
        ),
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(2000)
            )
        ),
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(8000)
            )
        )
    ])

    # -------- T2 ---------
    # TESTED_FUNC_NAME = "longest_word"
    # test_cases.extend([
    #      file_param_assert_eq(
    #         "Hi! my names is bob. this is weird!\n I'm writing a test!",
    #         ['writing']
    #     ),
    #     file_param_assert_eq(
    #         "Hi hi Hi hi hi Hi hi hi",
    #         ['hi']
    #     ),
    #     file_param_assert_eq(
    #         "Hello! How are you? Great! this is fun.",
    #         ['hello!', 'great!']
    #     ), 
    #     _ps(peb.assert_eq_correct_sol(
    #         longest_word_sol, 
    #         gen_random_file(1000)
    #         )
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         longest_word_sol, 
    #         gen_random_file(2000)
    #         )
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         longest_word_sol, 
    #         gen_random_file(8000)
    #         )
    #     )
    # ])

    # # -------- T3 ---------
    # TESTED_FUNC_NAME = "longest_palindrome"
    # test_cases.extend([
    #     file_param_assert_eq(
    #         "anna civic kayak level madam mom noon racecar radar " +
    #         "redder refer rotor solos stats tenet wow", ['racecar']
    #     ),
    #     file_param_assert_eq(
    #         "Anna Civic Kayak Level madam Mom Noon Racecar Radar " +
    #         "Redder refer Rotor Solos Stats Tenet Wow", ['racecar']
    #     ),
    #     file_param_assert_eq(
    #         "HI, none, of, these, Words, are, Palindromes", []
    #     ),
    #     file_param_assert_eq(
    #         "Anna Civic kayak Level madam Mom Noon Radar " +
    #         "refer Rotor Solos Stats Tenet Wow",
    #         ['civic', 'kayak', 'level', 'madam', 'radar', 'refer', 'rotor', 'solos', 'stats', 'tenet']
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         longest_palindrome_sol, 
    #         gen_random_file(1000)
    #         )
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         longest_palindrome_sol,
    #         gen_random_file(2000),
    #         )
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         longest_palindrome_sol,
    #         gen_random_file(8000),
    #         )
    #     )
    # ])

    # # -------- T4 ---------
    # TESTED_FUNC_NAME = "all_vowels_counter"

    # test_cases.extend([
    #     file_param_assert_eq(
    #         "The sequoia tree was not facetiously speaking because\n"
    #         + "it lived in an utopia.",
    #         2
    #     ),
    #     file_param_assert_eq(
    #         "The elephant learned the vowels aeiou, and it learned"
    #         + "aeronautics. Do you know the word acuminose?",
    #         3
    #     ),
    #     file_param_assert_eq(
    #         "AAEEIIOOU, said the asteroidu",
    #         2
    #     ),
    #     file_param_assert_eq(
    #         "I live in the ghetto so ratatata",
    #         0
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         all_vowels_counter_sol, 
    #         gen_random_file(1000)
    #         )
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         all_vowels_counter_sol,
    #         gen_random_file(2000),
    #         )
    #     ),
    #     _ps(peb.assert_eq_correct_sol(
    #         all_vowels_counter_sol,
    #         gen_random_file(8000),
    #         )
    #     )
    # ])

    # # -------- T5 ---------
    # test_cases.extend([
    #     gen_file_assert_eq("", 0, "count_long_lines"),
    #     gen_file_assert_eq("This isn't a long line.\n"
    #                     + "This line is a very, very, very, very, very, very, very, "
    #                     + "very, very, very, very, long line.\n"
    #                     + "This a medium length line, I guess.", 1, "count_long_lines", 40),
    #     gen_file_assert_eq("This is a short line.\n"
    #                     + "This one is, too.\n"
    #                     + "And this one.\n"
    #                     + "Short line!!!!!", 0, "count_long_lines", 40),
    #     gen_file_assert_eq("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    #                     + "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
    #                     + "ccccccccccccccccccccccccccccccccccc\n"
    #                     + "\n"
    #                     + "ddddddddddddddddddddddddddddddddddd\n"
    #                     + "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\n", 5, "count_long_lines", 30), 
    #     # _ps(peb.assert_eq_correct_sol(
    #     #     count_long_lines_sol, 
    #     #     gen_random_file(1000)
    #     #     )
    #     # ),
    #     # _ps(peb.assert_eq_correct_sol(
    #     #     count_long_lines_sol, 
    #     #     all_vowels_counter_sol(2000)
    #     #     )
    #     # ),
    #     # _ps(peb.assert_eq_correct_sol(
    #     #     count_long_lines_sol, 
    #     #     all_vowels_counter_sol(8000)
    #     #     )
    #     # )
    # ])


    return test_cases

