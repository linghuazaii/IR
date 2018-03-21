#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is auto-generated.Edit it at your own peril.

def BKDRHash(key, itype):
    seed = 1313131313
    hash_val = 0
    for c in key:
        hash_val = (hash_val * seed) + ord(c)

    return ((hash_val & 0x7FFFFFFFFFFFFFF) | itype << 60)

'''
if __name__ == '__main__':
    print BKDRHash('the vampire never exists!', 0)
'''
