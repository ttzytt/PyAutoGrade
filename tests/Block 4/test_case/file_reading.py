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
    ret = io.StringIO(rand_str)
    ret.seek(0)
    return ret
    

def gen_file_assert_eq(string : str, expected : Any, tested_func_name : str, *extra_args, **extra_kwargs) -> PrewrittenScriptCase:
    peb = ps.EvaluatorBuilder()
    temp_file = io.StringIO()
    temp_file.write(string)
    temp_file.seek(0)
    return ps(peb.assert_eq(expected, temp_file, *extra_args, **extra_kwargs), tested_func_name)

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
    read_file.seek(0)
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
            word = word.lower()
            if len(word) > max_length:
                max_length = len(word)
                longest_words = [word]
            elif len(word) == max_length and word not in longest_words:
                # If the current word has the same length as the longest word, add it to the list
                longest_words.append(word)
    read_file.seek(0)
    return longest_words

def longest_palindrome_sol(read_file):
    longest_palindromes = []
    max_length = 0

    for line in read_file:
        words = line.split()
        
        for word in words:
            # Check if the word is a palindrome
            word = word.lower()
            if word == word[::-1]:
                # If the word is a palindrome and its length is greater than the current maximum length
                if len(word) > max_length:
                    max_length = len(word)
                    longest_palindromes = [word]
                elif len(word) == max_length and word not in longest_palindromes:
                    # If the word is a palindrome and its length is equal to the current maximum length
                    longest_palindromes.append(word)
    read_file.seek(0)
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
    read_file.seek(0)
    return count

def count_long_lines_sol(read_file, min_length):
    num_long_lines = 0

    for line in read_file:
        # Check if the length of the line is at least min_length
        if len(line) >= min_length:
            num_long_lines += 1
    read_file.seek(0)
    return num_long_lines

def specific_word_count_sol(read_file, word):
    count = 0
    word = word.lower()
    for line in read_file:
        # Split the line into words
        words = line.split()
        words = [w.lower() for w in words]
        # Count occurrences of the target word
        count += words.count(word)
    read_file.seek(0)
    return count

def starts_with_counter_sol(read_file, word_beginning):
    count = 0
    for line in read_file:
        # Split the line into words
        words = line.split()
        words = [word.lower() for word in words]
        # Count words that start with the specified prefix
        count += sum(1 for word in words if word.startswith(word_beginning))
    read_file.seek(0)
    return count


def test_case_constructor() -> list[TestCase]:

    test_cases : list[TestCase] = []
    peb = ps.EvaluatorBuilder()
    TESTED_FUNC_NAME = "average_length"
    file_param_assert_eq = lambda string, expected: gen_file_assert_eq(string, expected, TESTED_FUNC_NAME)
    _ps = lambda evaluator, msg = "": ps(evaluator, TESTED_FUNC_NAME, msg)
    # -------- T1 ---------
    randfile = gen_random_file(20)
    correct_ans = average_length_sol(randfile)
    test_cases.extend([
        file_param_assert_eq(
            "Foxes eat rabbits.\nhug a fox.", 4
        ), # #1
        file_param_assert_eq(
            randfile.getvalue(), correct_ans
        ), # #2
        file_param_assert_eq(
            "Foxes eat rabbits. Four. Seven. Thisistest.\nhug a fox.", 5.111111111111111
        ), # #3
        file_param_assert_eq(
            "a a a a a b b b b", 1
        ), # #4
        file_param_assert_eq(
            "ab cd ef gh ij kl", 2
        ), # #5
        file_param_assert_eq(
            "a ab \t a \n ab \n a ab a ab", 1.5
        ), # #6
        file_param_assert_eq(
            "Thisisonewordhoweverlongitmayseem", 33
        ), # #7
        file_param_assert_eq(
            "Hyphen-hyphen another word", 8
        ), # #8
        file_param_assert_eq(
            "Apostraphe's another word", 7.666666666666667
        ), # #9
        file_param_assert_eq(
            "", None
        ), # #10
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(20)
            )
        ), # #11
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(2000)
            )
        ), # #12
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(8000)
            )
        ), # #13
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(8000)
            )
        ), # #14
        _ps(peb.assert_eq_correct_sol(
            average_length_sol, 
            gen_random_file(8000)
            )
        ), # #15
    ])


    # -------- T2 ---------
    TESTED_FUNC_NAME = "longest_word"
    # punctuation
    test_cases.extend([
    file_param_assert_eq(
            "Hi! my names is bob. this is weird!\n I'm writing a test!",
            ['writing']
        ), # #16
        file_param_assert_eq(
            "Hi hi Hi hi hi Hi hi hi",
            ['hi']
        ), # #17
        file_param_assert_eq(
            "Hello! How are you? Great! this is fun.",
            ['hello!', 'great!']
        ), # #18
        _ps(peb.assert_eq_correct_sol(
            longest_word_sol, 
            gen_random_file(1000)
            )
        ), # #19
        _ps(peb.assert_eq_correct_sol(
            longest_word_sol, 
            gen_random_file(2000)
            )
        ), # #20
        _ps(peb.assert_eq_correct_sol(
            longest_word_sol, 
            gen_random_file(8000)
            )
        ), # #21
    ])


    # # -------- T3 ---------
    TESTED_FUNC_NAME = "longest_palindrome"
    test_cases.extend([
        file_param_assert_eq(
            "anna civic kayak level madam mom noon racecar radar " +
            "redder refer rotor solos stats tenet wow", ['racecar']
        ), # #22
        file_param_assert_eq(
            "Anna Civic Kayak Level madam Mom Noon Racecar Radar " +
            "Redder refer Rotor Solos Stats Tenet Wow", ['racecar']
        ), # #23
        file_param_assert_eq(
            "HI, none, of, these, Words, are, Palindromes", []
        ), # #24
        file_param_assert_eq(
            "Anna Civic kayak Level madam Mom Noon Radar " +
            "refer Rotor Solos Stats Tenet Wow",
            ['civic', 'kayak', 'level', 'madam', 'radar', 'refer', 'rotor', 'solos', 'stats', 'tenet']
        ), # #25
        _ps(peb.assert_eq_correct_sol(
            longest_palindrome_sol, 
            gen_random_file(1000)
            )
        ), # #26
        _ps(peb.assert_eq_correct_sol(
            longest_palindrome_sol,
            gen_random_file(2000),
            )
        ), # #27
        _ps(peb.assert_eq_correct_sol(
            longest_palindrome_sol,
            gen_random_file(8000),
            )
        ), # #28
    ])

    # -------- T4 ---------
    TESTED_FUNC_NAME = "all_vowels_counter"

    test_cases.extend([
        file_param_assert_eq(
            "The sequoia tree was not facetiously speaking because\n"
            + "it lived in an utopia.",
            2
        ), # #29
        file_param_assert_eq(
            "The elephant learned the vowels aeiou, and it learned"
            + "aeronautics. Do you know the word acuminose?",
            3
        ), # #30
        file_param_assert_eq(
            "AAEEIIOOU, said the asteroidu",
            2
        ), # #31
        file_param_assert_eq(
            "I live in the ghetto so ratatata",
            0
        ), # #32
        _ps(peb.assert_eq_correct_sol(
            all_vowels_counter_sol, 
            gen_random_file(1000)
            )
        ), # #33
        _ps(peb.assert_eq_correct_sol(
            all_vowels_counter_sol,
            gen_random_file(2000),
            )
        ), # #34
        _ps(peb.assert_eq_correct_sol(
            all_vowels_counter_sol,
            gen_random_file(8000),
            )
        ), # #35
    ])


    # # -------- T5 ---------
    TESTED_FUNC_NAME = "count_long_lines"
    test_cases.extend([
        gen_file_assert_eq("", 0, "count_long_lines", 10), # #36
        gen_file_assert_eq("This isn't a long line.\n"
                        + "This line is a very, very, very, very, very, very, very, "
                        + "very, very, very, very, long line.\n"
                        + "This a medium length line, I guess.", 1, "count_long_lines", 40), # #37
        gen_file_assert_eq("This is a short line.\n"
                        + "This one is, too.\n"
                        + "And this one.\n"
                        + "Short line!!!!!", 0, "count_long_lines", 40), # #38
        gen_file_assert_eq("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
                        + "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                        + "ccccccccccccccccccccccccccccccccccc\n"
                        + "\n"
                        + "ddddddddddddddddddddddddddddddddddd\n"
                        + "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\n", 5, "count_long_lines", 30), # #39
        _ps(peb.assert_eq_correct_sol(
            count_long_lines_sol, 
            gen_random_file(1000),
            random.randint(1, 200)
            )
        ), # #40
        _ps(peb.assert_eq_correct_sol(
            count_long_lines_sol, 
            gen_random_file(2000),
            random.randint(1, 200)
            )
        ), # #41
        _ps(peb.assert_eq_correct_sol(
            count_long_lines_sol, 
            gen_random_file(8000),
            random.randint(1, 200)
            )
        ), # #42
    ])


    # -------- T6 ---------
    TESTED_FUNC_NAME = "random_word"

    rand_file1 = gen_random_file(2000)
    words1 = rand_file1.getvalue().split()
    rand_file2 = gen_random_file(2000)
    words2 = rand_file2.getvalue().split()
    rand_file3 = gen_random_file(2000)
    words3 = rand_file3.getvalue().split()
    rand_file4 = gen_random_file(2000)
    words4 = rand_file4.getvalue().split()
    test_cases.extend([
        _ps(
            peb.assert_content_in_set(set(words1), 
                                    lambda s : set([s]),
                                    rand_file1)
        ), # #43
        _ps(
            peb.assert_content_in_set(set(words2), 
                                      lambda s : set([s]),
                                      rand_file2)
        ), # #44
        _ps(
            peb.assert_content_in_set(set(words3), 
                                      lambda s : set([s]),
                                      rand_file3)
        ), # #45
          _ps(
            peb.assert_content_in_set(set(words4), 
                                      lambda s : set([s]),
                                      rand_file4)
        ) # #46
    ])


    # -------- T7 ---------
    TESTED_FUNC_NAME = "random_words"
    rand_file1 = gen_random_file(1000)
    words1 = rand_file1.getvalue().split()
    rand_file2 = gen_random_file(1000)
    words2 = rand_file2.getvalue().split()
    rand_file3 = gen_random_file(1000)
    words3 = rand_file3.getvalue().split()
    rand_file4 = gen_random_file(1000)
    words4 = rand_file4.getvalue().split()
    test_cases.extend([
        _ps(
            peb.assert_content_in_set(set(words1), 
                                    lambda s : set(s),
                                    rand_file1, random.randint(1, 20)) 
        ), # #47
        _ps(
            peb.assert_content_in_set(set(words2), 
                                      lambda s : set(s),
                                      rand_file2, random.randint(1, 20))
        ), # #48
        _ps(
            peb.assert_content_in_set(set(words3), 
                                      lambda s : set(s),
                                      rand_file3, random.randint(1, 20))
        ), # #49
          _ps(
            peb.assert_content_in_set(set(words4), 
                                      lambda s : set(s),
                                      rand_file4, random.randint(1, 20))
        ) # #50
    ])

    # -------- T8 ---------
    TESTED_FUNC_NAME = "specific_word_count"
    rand_file1 = gen_random_file(3000)
    words1 = rand_file1.getvalue().split()
    rand_file2 = gen_random_file(3000)
    words2 = rand_file2.getvalue().split()
    rand_file3 = gen_random_file(3000)
    words3 = rand_file3.getvalue().split()
    test_cases.extend([
        gen_file_assert_eq(
            "This is the sentence. DO NOT HUG ME ok?\nYou will regret it! :)" +
            "... Seriously LISTEN\n here don't do it. here",
            2,
            "specific_word_count",
            "here"
        ),  # 51
        gen_file_assert_eq(
            "Never ever do this!!!!! You shall regret it! A demon will " +
            "come to haunt you!!",
            0,
            "specific_word_count",
            "the"
        ),  # 52
        gen_file_assert_eq(
            "Do not do whatbubbleever anyone tellbubbles you " +
            "to do! bubbleNEVER bubble Or you will regret it",
            1,
            "specific_word_count",
            "bubble"
        ),  # 53
        _ps(
            peb.assert_eq_correct_sol(
                specific_word_count_sol, 
                rand_file1,
                random.choice(words1)
            )
        ), # #54
        _ps(
            peb.assert_eq_correct_sol(
                specific_word_count_sol, 
                rand_file2,
                random.choice(words2)
            )
        ), # #55
        _ps(
            peb.assert_eq_correct_sol(
                specific_word_count_sol, 
                rand_file3,
                random.choice(words3)
            )
        ), # #56
    ])

    # -------- T9 ---------
    TESTED_FUNC_NAME = "starts_with_counter"
    TESTED_FUNC_NAME = "starts_with_counter"
    randfile1 = gen_random_file(2000)
    word1_pre = randfile1.getvalue().split()
    rand_idx = random.randint(0, len(word1_pre) - 1)
    word1_pre = word1_pre[rand_idx] ; word1 = word1_pre[:random.randint(1, len(word1_pre))]
    randfile2 = gen_random_file(2000)
    word2_pre = randfile2.getvalue().split()
    rand_idx = random.randint(0, len(word2_pre) - 1)
    word2_pre = word2_pre[rand_idx] ; word2 = word2_pre[:random.randint(1, len(word2_pre))]
    randfile3 = gen_random_file(2000)
    word3_pre = randfile3.getvalue().split()
    rand_idx = random.randint(0, len(word3_pre) - 1)
    word3_pre = word3_pre[rand_idx] ; word3 = word3_pre[:random.randint(1, len(word3_pre))]
    test_cases.extend([
        gen_file_assert_eq(
            "queen\nAardvark\nQueotes\nthat\nbeing\nan\naardvark\nqueen\nis\nhard ",
            2,
            "starts_with_counter",
            "aa"
        )  # #57
        , 
        _ps(
            peb.assert_eq_correct_sol(
                starts_with_counter_sol, 
                randfile1,
                word1
            )
        ), # #58
        _ps(
            peb.assert_eq_correct_sol(
                starts_with_counter_sol, 
                randfile2,
                word2
            )
        ), # #59
        _ps(
            peb.assert_eq_correct_sol(
                starts_with_counter_sol, 
                randfile3,
                word3
            )
        ), # #60
    ])


    return test_cases


