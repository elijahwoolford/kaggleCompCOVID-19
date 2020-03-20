import os
import json


def reader(json_file_path: str):
    with open(json_file_path) as curr_json:
        return json.load(curr_json)


class ArticleReader:

    def __init__(self, json_file_path):
        data = reader(json_file_path)
        self.file = json_file_path
        self.body = data["body_text"]
        self.metadata = data["metadata"]
        self.id = data["paper_id"]

    def get_text_parts(self):
        data = reader(self.file)
        text_parts = data["body_text"][0]["text"]
        return text_parts


