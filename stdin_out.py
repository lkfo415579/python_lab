# -*- coding: utf-8 -*-
# !/usr/bin/env python
import sys
import codecs

if __name__ == '__main__':
    sys.stdin = codecs.getreader('utf-8')(sys.stdin)
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

    for line in sys.stdin:
        sys.stdout.write("FUCKER:"+line)
