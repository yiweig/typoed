KEYS_ADJACENCY_LIST_FILE_NAME = 'keys.adj'
KEY_MAPPING = {}

with open(KEYS_ADJACENCY_LIST_FILE_NAME) as keys_adjacency_list:
    for line in keys_adjacency_list:
        if len(line) > 1:
            keys = line.split()
            KEY_MAPPING[keys[0]] = keys[1:]

