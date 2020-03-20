import os

from ArticleReader import ArticleReader


def gather_docs_by_keyword(data_path: str, keywords: list):
    docs = []
    keyword_counts = {}
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".json"):
                curr_file_path = os.path.join(root, file)
                article = ArticleReader(curr_file_path)
                text_parts = article.get_text_parts()
                status = contains_keywords(text_parts, keywords)
                if status:
                    docs.append(file)
                    keyword_count = get_keyword_count(text_parts, keywords)
                    keyword_counts[file] = keyword_count

    return docs, keyword_counts


def contains_keywords(text_parts: str, keywords: list):
    statuses = []
    for keyword in keywords:
        status = keyword in text_parts
        statuses.append(status)

    return True in statuses


def get_keyword_count(text_parts: str, keywords: list):
    keyword_count = {}
    for keyword in keywords:
        count = text_parts.count(keyword)
        keyword_count[keyword] = count

    return keyword_count


def get_top_docs_by_keyword(keyword_counts: dict, keyword: str):
    return sorted(keyword_counts.keys(), key=lambda x: (keyword_counts[x][keyword]), reverse=True)


if __name__ == '__main__':
    # TODO:
    docs, keyword_counts = gather_docs_by_keyword("", [])
    # get_top_docs_by_keyword(keyword_counts, "")
