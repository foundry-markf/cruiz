#!/usr/bin/env python3

"""
Search recipes parameters
"""

import typing

from .commonparameters import CommonParameters


class SearchRecipesParameters(CommonParameters):
    """
    Representation of all the arguments to search for a recipe

    Attributes are dynamically added from the keyword-args passed in.
    """

    def __init__(self, **args: typing.Any) -> None:
        import cruiz.workers.remotesearch

        super().__init__(cruiz.workers.remotesearch.invoke)
        for k, v in args.items():
            self.__setattr__(k, v)
