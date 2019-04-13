import csv
import ast


def id_splits_iterator():
    with open('splits.txt', 'r') as f:
        r = csv.reader(f, delimiter=',', quotechar='"')
        headers = next(r)
        for row in r:
            if len(row) == 0:
                break
            if row[0].startswith('#'):
                continue

            yield {headers[i].strip(): ast.literal_eval(row[i]) for i in range(len(headers))}

if __name__ == "__main__":
        for splid, split_dict in enumerate(id_splits_iterator()): print(splid, split_dict)