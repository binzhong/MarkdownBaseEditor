#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

from globalvalue import *

import houdini
from misaka import Markdown, HtmlRenderer
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name

class HighlighterRenderer(HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=False)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter(linenos=True)
            return highlight(text, lexer, formatter)
        # default
        return '\n<pre><code>{}</code></pre>\n'.format(houdini.escape_html(text.strip()))


class TextBrowser(QTextEdit):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, parent = None):
        self.setReadOnly(True)
        pass
        #self.setZoomFactor(1.25)
    
    def setText(self, text):
        htmlrd = HighlighterRenderer()
        mdToHtml = Markdown(htmlrd, extensions=('fenced-code', 'tables', 'footnotes',
        'autolink', 'highlight','strikethrough', 'underline', 'quote', 'superscript', 
        'math', 'no-intra-emphasis', 'space-headers', 'math-explicit'))
        html = mdToHtml(text)
        html = html.replace('<table>', '<table border="1">')
        #css head
        cssStyle = '<style type = "text/css">\n'
        #css body
        with open('./resource/typora.style', 'r') as file:
            typoraStyle = file.read()
        cssStyle = cssStyle + typoraStyle
        cssStyle = cssStyle + HtmlFormatter().get_style_defs('.highlight')
        #css end
        cssStyle = cssStyle + '</style>\n'

        self.setHtml(cssStyle + html)

        