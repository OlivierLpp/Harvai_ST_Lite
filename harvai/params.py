import os


def get_path_data(path):
    if os.path.basename(path) == 'harvai-lite':
        return "raw_data/LEGITEXT000006074228.pdf"
    else:
        return "raw_data/LEGITEXT000006074228.pdf"

def get_path_json(path):
    if os.path.basename(path) == 'harvai-lite':
        return "raw_data/data_preproc.json"
    else:
        return "raw_data/data_preproc.json"

def get_path_json_digits(path):
    if os.path.basename(path) == 'harvai-lite':
        return "raw_data/data_preproc_digits.json"
    else:
        return "raw_data/data_preproc_digits.json"
