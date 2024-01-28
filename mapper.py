#!/usr/bin/env python   
# import sys because we need to read and write data to STDIN and STDOUT 

import re
import sys
import threading
from queue import Queue

def clean_text(file):
    words = []
    reg = re.compile("[a-z]+")
    for line in file:
        if len(line) > 0:
            words.append(reg.findall(line.lower()))
    words = [i for i in words if i != []]
    return words

def unlist(input):
    result_list = []
    for i in input:
        for word in i:
            result_list.append(word)
    return result_list

def mapper(words, output_queue):
    flattened_words = unlist(words)
    for word in flattened_words:
        output_queue.put((word, 1))

def main():
    words = clean_text(sys.stdin)
    output_queue = Queue()

    # Creating two mapper threads
    mapper_thread1 = threading.Thread(target=mapper, args=(words[:len(words)//2], output_queue))
    mapper_thread2 = threading.Thread(target=mapper, args=(words[len(words)//2:], output_queue))

    mapper_thread1.start()
    mapper_thread2.start()
    mapper_thread1.join()
    mapper_thread2.join()

    while not output_queue.empty():
        print(','.join(map(str, output_queue.get())))

if __name__ == "__main__":
    main()