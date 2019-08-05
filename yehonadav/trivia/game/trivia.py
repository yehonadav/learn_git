"""
A simple python api wrapper for https://opentdb.com/
"""

from aiohttp import ClientSession
from requests import get

from game.__helpers import decode_dict, make_request
from game.enums import *


class Trivia:
    def request(self, num_questions: int, category: Category = None,
                difficulty: Difficulty = None) -> dict:
        """
        Send an api request to https://opentdb.com/
        Limitations:
        Only 1 Category can be requested per API Call.
        To get questions from any category, don't specify a category.
        A Maximum of 50 Questions can be retrieved per call.

        :param num_questions: the number of questions,
        must be between 1 and 50 (inclusive)

        :param category: the category of the question. None for any category

        :param difficulty: the Difficulty of the question. None for any Difficulty

        :param type_: the type of the question. None for any type

        :return: the api call response

        :rtype: dict

        :raises: ValueError when the num_questions parameter is less than 1
        or greater than 50
        """
        result = get(
            self.__url(num_questions, category, difficulty)).json()
        if result['response_code'] in (3, 4):
            raise Exception("failed to load questions")
        else:
            return decode_dict(result)

    async def request_async(self, session: ClientSession, close_session: bool,
                            num_questions: int, category: Category = None,
                            difficulty: Difficulty = None) -> dict:
        """
        Send an api request to https://opentdb.com/
        Limitations:
        Only 1 Category can be requested per API Call.
        To get questions from any category, don't specify a category.
        A Maximum of 50 Questions can be retrieved per call.

        :param session: an Aiohttp client session.

        :param close_session: True to close the session after the request.

        :param num_questions: the number of questions,
        must be between 1 and 50 (inclusive)

        :param category: the category of the question. None for any category

        :param difficulty: the Difficulty of the question. None for any Difficulty

        :return: the api call response

        :rtype: dict

        :raises: ValueError when the num_questions parameter is less than 1
        or greater than 50

        :raises ClientResponseError if the HTTP response code isn't 200
        """
        try:
            return await self.__request(
                session, num_questions, category, difficulty)
        finally:
            if close_session:
                session.close()

    async def __request(self, session: ClientSession, num_questions: int,
                        category: Category = None, difficulty: Difficulty = None) -> dict:
        """
        Helper method for the async request.
        """
        resp = await make_request(
            session, self.__url(num_questions, category, difficulty))
        result = await resp.json()
        if result['response_code'] != 0:
            return await self.__request(
                session, num_questions, category, difficulty)
        else:
            return decode_dict(result)

    def __url(self, num_questions, category, difficulty):
        """
        Helper method to generate request url.
        """
        if num_questions < 1 or num_questions > 50:
            raise ValueError
        url = 'https://opentdb.com/api.php?amount={}&encode=base64'.format(
            num_questions)
        if category is not None:
            url += '&category={}'.format(category.value)
        if difficulty is not None:
            url += '&difficulty={}'.format(difficulty.value)
        return url
