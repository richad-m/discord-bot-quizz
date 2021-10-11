import gspread
import random
import trim
import re

# Retrieve credentials to access GSheet
from client_secret import CREDENTIALS

# Passing credentials via gspread
gc = gspread.service_account_from_dict(CREDENTIALS)
# Selecting the spreadsheet to open
sh = gc.open_by_key("1Ws91wWUhnpCXnV8Wpdwrr5vnd5Coio5kw1cQ8FOVDHc")
booba_database = sh.sheet1

# Retrieving data from the spreadsheet in one variable, ONE TIME
DB = booba_database.get_all_values()


def pick_random_song(db):
    # Picks random song out of a DB
    random_punchline_row = random.sample(db, 1)[0]
    chosen_song = {
        'artist': random_punchline_row[1],
        'title': random_punchline_row[3],
        'phrase': random_punchline_row[2],
        'album': random_punchline_row[4],
        'year': random_punchline_row[5]
    }
    return chosen_song


def hole_in_sentence(string):
    # Returns an with a random word replaced by ******, and the missing word
    string_list = re.findall("\w*", string)
    words = []
    for word in string_list:
        if len(word) > 4:
            words.append(word)
    word_to_replace = random.sample(words, 1)[0]
    holed_sentence = string.replace(word_to_replace, '______')
    result = {'sentence': holed_sentence, 'missing_word': word_to_replace}
    return result


async def ask_missing_word(message, sentence):
    # Game function asks to guess the missing word in a phrase
    await message.channel.send(":pirate_flag: Welcome to Booba Quizz :pirate_flag: !\n\n")
    await message.channel.send("What's the missing word in this sentence ? :musical_note:\n **>>> {} **\n\n Please answer below :point_down:".format(sentence['sentence']))


async def ask_the_title(message, chosen_song):
    # Game function to guess title of the song retrieved from spreadsheet
    await message.channel.send(":pirate_flag: Welcome to Booba Quizz :pirate_flag: !\n\n")
    await message.channel.send("In which song can we find this phrase? :musical_note:\n **>>> {} **\n\n Please answer below :point_down:".format(chosen_song['phrase']))


async def check_answer(message, chosen_song, mode):
  # Checks if the message matches the right answer (depend on the chosen mode)
    right_answer = chosen_song[mode]
    if trim.format_string(message.content) == trim.format_string(right_answer):
        # await message.add_reaction(":clap:")
        await message.channel.send(":white_check_mark: That's right *{}*, the answer was *{}* ! You are a real Ratpis :pirate_flag:".format(message.author.display_name, right_answer))
    else:
        # await message.add_reaction(':x:')
        await message.channel.send(":x: Wrong. The correct answer was *{}*".format(right_answer))
