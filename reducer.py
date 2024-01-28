#!/usr/bin/env python 

import sys
import threading
from queue import Queue

def reducer(input_queue):
    current_word = None
    current_count = 0

    while not input_queue.empty():
        word, count = input_queue.get()
        
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(f"{current_word},{current_count}")
            current_word = word
            current_count = count

    if current_word:
        print(f"{current_word},{current_count}")

def main():
    input_queue = Queue()

    # Assuming the input is coming from the standard input
    for line in sys.stdin:
        word, count_str = line.strip().split(',')
        count = int(count_str)
        input_queue.put((word, count))

    # Creating two reducer threads
    reducer_thread1 = threading.Thread(target=reducer, args=(input_queue,))
    reducer_thread2 = threading.Thread(target=reducer, args=(input_queue,))

    reducer_thread1.start()
    reducer_thread2.start()
    reducer_thread1.join()
    reducer_thread2.join()

if __name__ == "__main__":
    main()