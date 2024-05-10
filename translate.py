import argparse 
import json
from typing import List, Tuple
from utils import parse_query

def get_from_index(index, term_list):
    found = set(term_list)
    for term in term_list:
        res = index.get(term)
        if not res:
            res = set()
            for i in index:
                entry = index.get(i)
                if term in entry:
                    res.update([i] + entry)
        found.update(res)
    return list(found)
    

def translate_query(query: str, index_location: str) -> Tuple[List[str], List[str], List[str], List[str]]:
    include, exclude, optional = parse_query(query)
    print("include", include)
    print("exclude", exclude)
    print("optional", optional)
    print("...")

    index = None
    with open(index_location, "r") as file:
        index = json.load(file)
        print(index)
    if not index:
        print("error loading index")
        return

    include_results = get_from_index(index, include)
    exclude_results = get_from_index(index, exclude)
    optional_results = get_from_index(index, optional)

    # Remove the exclude results from the include+optional results
    all_positive_results = include_results + optional_results
    results = list(set(all_positive_results) - set(exclude_results))

    print("include", include_results)
    print("exclude", exclude_results)
    print("optional", optional_results)
    print("...")
    print("all_positives", all_positive_results)
    print("results", results)
    print("...")


    return include_results, exclude_results, optional_results, results



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", help="search query")
    args = parser.parse_args()
    query = args.query if args.query else ""
    print("query", query)

    index_location = "./search_terms.json"    
    print(translate_query(query, index_location))
