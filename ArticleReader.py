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
        self.abstract = data["abstract"]
        self.bib = data["bib_entries"]

    def get_text_parts(self):
    	return "".join([x['text'] for x in self.body])


if __name__ == '__main__':
    a = ArticleReader("2020-03-13/biorxiv_medrxiv/biorxiv_medrxiv/0a32446730827ad8152c6a61e4738e4e0b231412.json")
    print(a.body)
