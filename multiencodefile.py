#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import codecs
import chardet

class McFile():
    def __init__(self, file = None, encoding = 'utf-8'):
        self.file = file
        self.encoding = encoding
    
    #for with ... as ...
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        return False

def mcOpen(fileName, flags, encoding = ''):
    #Open with bynary, there is no need to detecting the charset
    assert(flags.find('b') < 0)

    result = McFile()

    #encoding is valid
    if encoding != '':
        result.file = codecs.open(fileName, flags, encoding)
        result.encoding = encoding
        return result

    file = open(fileName, 'rb')
    #The format of the result should be like:
    # {'confidence': 0.98999999999999999, 'encoding': 'GB2312'}
    detResult = chardet.detect(file.read())
    file.close()

    result.encoding = detResult['encoding']
    #If encoding is like GB* and the confidence is lower than 60 percent,use the GB18030
    if result.encoding.find('GB') >= 0 and result['confidence'] < 0.6:
        result.encoding = 'GB18030'
        result.file = codecs.open(filename, flags, result.encoding)
    else:
        result.file = codecs.open(fileName, flags, result.encoding) 
    
    return result

def openWithEncoding(fileName, flags, encoding):
    return codecs.open(fileName, flags, encoding)