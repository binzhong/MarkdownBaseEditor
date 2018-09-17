#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QTextBrowser

from globalvalue import *

import houdini
from misaka import Markdown, HtmlRenderer
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name

class HighlighterRenderer(HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter(linenos=True)
            return highlight(text, lexer, formatter)
        # default
        return '\n<pre><code>{}</code></pre>\n'.format(houdini.escape_html(text.strip()))


class TextBrowser(QTextBrowser):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        pass
        #with open('./resource/default.css', 'r') as file:
        #    self.defaultCSS = file.read()
    
    def setText(self, text):
        htmlrd = HighlighterRenderer()
        mdToHtml = Markdown(htmlrd, extensions=('fenced-code', 'tables', 'footnotes', 'autolink', 'highlight',))
        html = mdToHtml(text)
        #css head
        cssStyle = '<style type = "text/css">\n'
        #css body
        cssStyle = cssStyle + HtmlFormatter().get_style_defs('.highlight')
        #css end
        cssStyle = cssStyle + '</style>\n'

        super().setHtml(cssStyle + html)

        