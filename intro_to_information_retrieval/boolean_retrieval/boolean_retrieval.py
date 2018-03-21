#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is auto-generated.Edit it at your own peril.

news_dir = '../news'
max_content_length = 64 * 1024 # 64k
delimiters = [' ', ',', '.', '\n']

test = '../news/1.news'

def tokenize(data, delimeter):


def read_news(file_name):
    title = None
    content = None

    with open(file_name) as f:
        title = f.readline()
        content = f.read(max_content_length)
    f.close()

    return title[:-1], content[:-1]


if __name__ == '__main__':
    title, content = read_news(test)
    print title
    print content
