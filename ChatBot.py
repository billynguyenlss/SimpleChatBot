import streamlit as st
import numpy as np
import nltk
from nltk.chat.util import Chat


class ChatBot(Chat):
    def __init__(self, pairs, reflections):
        super().__init__(pairs, reflections)
        self._welcome = "Xin chào! Chúc anh chị một ngày tốt lành ạ! Em có thể giúp gì cho anh chị được ạ?"
        self._bot_responses = []
        self._user_requests = []

    def get_bot_responses(self):
        return self._bot_responses

    def get_user_requests(self):
        return self._user_requests

    # Hold a conversation with a chatbot
    def response(self, user_input, quit="quit"):
        self._user_requests.append(user_input)
        if user_input != quit:
            # while user_input[-1] in "!.":
            #     user_input = user_input[:-1]
            print("Bot >> ", self.respond(user_input))
            self._bot_responses.append(self.respond(user_input))
            return self.respond(user_input)
        else:
            return

    def run(self, user_input):

        self.response(user_input)
