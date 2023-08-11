import json
import random

from config import queue_filename, source_filename, chunk_size


def file_read(filename):
    fh = open(filename, 'r')
    content: list = json.loads(fh.read())
    fh.close()
    return content


def extract() -> str:
    try:
        data = file_read(queue_filename)
        if len(data) < 1:
            raise Exception('Empty file')
    except Exception as e:
        data = file_read(source_filename)

    random.shuffle(data)
    output = "\n".join([' - '.join(item) for item in data[0:chunk_size]])
    queue = data[chunk_size:]

    file_handler = open(queue_filename, 'w+')
    json.dump(queue, file_handler)
    file_handler.close()

    return output
