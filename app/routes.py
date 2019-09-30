#! /usr/bin/env python3
# coding: utf8

import os

from flask import render_template, request, jsonify, url_for

from app import app
from classes.bot_reply import BotReply
from classes.institution import Institution
from classes.user_question import UserQuestion
from ..config import Config


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    bot = BotReply()
    return render_template('index.html',
                           title='Chez GrandPy',
                           bot=bot,
                           googlemaps_api_key=Config.GOOGLE_MAPS_API_KEY)


@app.route('/postmethod', methods = ['POST'])
def post_javascript_data():
    jsdata = request.form['entered_data']
    user_quest = UserQuestion(jsdata)
    bot = BotReply()
    # initialize a dict with the bot replies
    bot_rep = {"phrases": []}
    # check if this is an acceptable question
    if not user_quest.analyze(bot)['acceptable_question']:
        bot = BotReply()
        # tell the user why she/he has to retype her/his question
        bot_rep["phrases"] +=  [user_quest.analyze(bot)['ask_for_something']]
    else:
        # initialize the institution
        inst = Institution(user_quest.analyze(bot)['question'])
        # fill the phrases
        bot_rep["phrases"] += [bot.give_answer_first(inst)]
        bot_rep["phrases"] += [bot.give_answer_second(inst)]
        # provide the map variables
        app_map = bot.return_map(inst, zoom=15)
        bot_rep["map"] = {
            "lat": app_map.lat,
            "lng": app_map.lng,
            "title": app_map.title,
            "zoom": app_map.zoom
        }
    return jsonify(bot_rep)
