import os
from typing import List
from ArticleReader import ArticleReader


def gather_docs_by_keyword(data_path: str, keywords: List[str]) -> (List[str], dict):
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


def contains_keywords(text_parts: str, keywords: List[str]) -> bool:
    for keyword in keywords:
        status = keyword in text_parts
        if status:
            return True
        else:
            continue

    return False


def get_keyword_count(text_parts: str, keywords: List[str]) -> int:
    keyword_count = 0
    for keyword in keywords:
        keyword_count += text_parts.count(keyword)

    return keyword_count


def get_top_docs_by_keyword(keyword_counts: dict, num_top_aricles: int) -> List[str]:
    top_doc_counts = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:num_top_aricles]
    return [x[0] for x in top_doc_counts]

def get_sentences_with_keywords(docs: List[str], keywords: List[str], n = 30) -> List[str]:
    for doc in docs:
        if n > 0:
            article = ArticleReader(doc)
            text = article.get_text_parts()
            text = text.split('. ')
            for sentence in text:
                if any(keyword in sentence for keyword in keywords):
                    print(article.metadata['title'])
                    print()
                    print(sentence)
                    print()
                    print()
                    print()
                    n = n - 1

if __name__ == '__main__':
    # TODO:
    docs, keyword_counts = gather_docs_by_keyword("2020-03-13", ["Korea", "China", "Italy"])
    print(docs)
    print(keyword_counts)
    print(get_top_docs_by_keyword(keyword_counts, 10))
