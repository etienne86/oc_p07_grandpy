#! /usr/bin/env python3
# coding: utf8

from flask import Flask
from various.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
