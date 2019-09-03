from app import app

from classes.bot_reply import BotReply
from classes.institution import Institution
from classes.user_question import UserQuestion


def main():
    """
    This function is the main function executed by the program.
    """
    # say hello to the user
    bot_hello = BotReply()
    bot_hello.welcome_message()
    # initialize the interactive bot
    bot = BotReply()
    # ask for the user question
    entered_question = input("votre question svp ? ")
    user_quest = UserQuestion(entered_question)
    # loop as far as the user does not ask an acceptable question
    while not user_quest.analyze(bot)['acceptable_question']:
        bot = BotReply()
        # tell the user why she/he has to retype her/his question
        print(user_quest.analyze(bot)['ask_for_something'])
        # ask for the user question
        entered_question = input("votre question svp ? ")
        user_quest = UserQuestion(entered_question)
    # initialize the institution
    inst = Institution(user_quest.analyze(bot)['question'])
    # display the results
    print(bot.give_answer_first(inst))
    print(bot.give_answer_second(inst))

if __name__ == '__main__':
    main()