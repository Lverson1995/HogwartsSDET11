import json
import logging

import yaml
from requests import Request


class BaseApi:
    @classmethod
    def format(cls, r):
        print(json.dumps(r.json(), indent=2))
