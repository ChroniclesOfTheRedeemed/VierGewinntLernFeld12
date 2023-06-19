import json
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


class Storer:
    @staticmethod
    def create_if_not_exist(file_name, dict):
        file_path = "jsons/" + str(file_name) + ".json"
        if not Path(file_path).is_file():
            if not os.path.exists('../../jsons'):
                os.makedirs('../../jsons')
            open(file_path, "x")
            with open(file_path, "w") as outfile:
                outfile.write(json.dumps(dict, indent=4))

    @staticmethod
    def load(file_name) -> dict:
        file_path = "jsons/" + str(file_name) + ".json"
        # self.logger.info("UserData for " + user_name)
        if Path(file_path).is_file():
            logger.info("Open Json File from " + file_path)
            with open(file=file_path, encoding='utf-8') as json_file:
                data = json.load(json_file)
            logger.debug("Containing: ")
            logger.debug(data)
            return data
        else:
            logger.info("Couldn't find JSON, by path " + file_path)

    @staticmethod
    def store(file_name, dict):
        file_path = "jsons/" + str(file_name) + ".json"
        if Path(file_path).is_file():
            with open(file_path, "w") as outfile:
                outfile.write(json.dumps(dict, indent=4))
        else:
            if not os.path.exists('../../jsons'):
                os.makedirs('../../jsons')
            open(file_path, "x")
            with open(file_path, "w") as outfile:
                outfile.write(json.dumps(dict, indent=4))

    @staticmethod
    def exist(file_name: str) -> bool:
        my_file = Path("jsons/" + file_name + ".json")
        return my_file.is_file()
