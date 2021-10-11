import discord
import os
import help
import quizz

my_secret = os.environ['BOT_TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    # As soon as the bot is ready
    print('Logged as {}'.format(client.user))


@client.event
# Each time a message is received
async def on_message(message):
    # Ignoring messages from the bot
    if message.author == client.user:
        return

    if message.content == "!quizz":
        chosen_song = quizz.pick_random_song(quizz.DB)
        await quizz.ask_the_title(message, chosen_song)
        attempted_answer = await client.wait_for('message')
        await quizz.check_answer(attempted_answer, chosen_song, 'title')

    if message.content == "!quizzz":
        chosen_song = quizz.pick_random_song(quizz.DB)
        sentence = quizz.hole_in_sentence(chosen_song['phrase'])
        await quizz.ask_missing_word(message, sentence)
        attempted_answer = await client.wait_for('message')
        await quizz.check_answer(attempted_answer, sentence, 'missing_word')

    if message.content == "!help":
        response = help.message()
        await message.channel.send(response)


client.run(my_secret)
