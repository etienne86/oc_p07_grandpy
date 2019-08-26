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
    # loop as far as the user asks an acceptable question
    cont = True
    while cont:
        # ask for the user question
        entered_question = input("votre question svp ? ")
        user_quest = UserQuestion(entered_question)
        # initialize the interactive bot
        bot = BotReply()
        # initialize the institution
        inst = Institution(user_quest.analyze(bot)['question'])
        # stop or continue?
        cont = not user_quest.analyze(bot)['acceptable_question']
    # display the results
    print(bot.give_answer_first(inst))
    print(bot.give_answer_second(inst))

if __name__ == '__main__':
    main()