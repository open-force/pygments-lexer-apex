# -*- coding: utf-8 -*-
"""Pygments lexer for the Salesforce Apex language. This is largely a modified version of the Java Lexer."""

import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
    this, combined, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation
from pygments.util import shebang_matches
from pygments import unistring as uni

__all__ = ['ApexLexer']


class ApexLexer(RegexLexer):
    """For Salesforce Apex source code."""

    name = 'Apex'
    aliases = ['apex']
    filenames = ['*.apxc', '*.apxt', '*.cls']

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = {
        'root': [
            # General text
            (r'[^\S\n]+', Text),
            # Comments
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            # Keywords: go before method names to avoid lexing "throw new XYZ" as a method signature
            (r'(?i)(break|case|catch|continue|do|else|finally|for|if|instanceof|new|return|switch|this|throw|try|'
             r'while)\b',
             Keyword),
            # DML keywords
            (r'(?i)(delete|insert|merge|undelete|update|upsert)\b', Keyword),
            # Method names
            (r'((?:(?:[^\W\d]|\$)[\w.\[\]$<>]*\s+)+?)'  # return arguments
             r'((?:[^\W\d]|\$)[\w$]*)'                  # method name
             r'(\s*)(\()',                              # signature start
             bygroups(using(this), Name.Function, Text, Operator)),
            # Annotations
            (r'@[^\W\d][\w.]*', Name.Decorator),
            # Apex class modifiers
            (r'(?i)(abstract|const|enum|extends|final|global|implements|on|override|private|protected|public|static|'
             r'super|throws|with sharing|without sharing)\b', Keyword.Declaration),
            (r'(?i)(blob|boolean|date|datetime|decimal|double|float|id|integer|long|object|time)\b',
             Keyword.Type),
            # Constants
            (r'(?i)(true|false|null)\b', Keyword.Constant),
            (r'(?i)(class|interface|trigger)(\s+)', bygroups(Keyword.Declaration, Text),
             'class'),
            (r"'(\\\\|\\'|[^'])*'", String),
            (r"'\\.'|'[^\\]'|'\\u[0-9a-fA-F]{4}'", String.Char),
            (r'(\.)((?:[^\W\d]|\$)[\w$]*)',
             bygroups(Operator, Name.Attribute)),
            (r'^\s*([^\W\d]|\$)[\w$]*:', Name.Label),
            (r'([^\W\d]|\$)[\w$]*', Name),
            (r'([0-9][0-9_]*\.([0-9][0-9_]*)?|'
             r'\.[0-9][0-9_]*)'
             r'([eE][+\-]?[0-9][0-9_]*)?[fFdD]?|'
             r'[0-9][eE][+\-]?[0-9][0-9_]*[fFdD]?|'
             r'[0-9]([eE][+\-]?[0-9][0-9_]*)?[fFdD]|'
             r'0[xX]([0-9a-fA-F][0-9a-fA-F_]*\.?|'
             r'([0-9a-fA-F][0-9a-fA-F_]*)?\.[0-9a-fA-F][0-9a-fA-F_]*)'
             r'[pP][+\-]?[0-9][0-9_]*[fFdD]?', Number.Float),
            (r'0[xX][0-9a-fA-F][0-9a-fA-F_]*[lL]?', Number.Hex),
            (r'0[bB][01][01_]*[lL]?', Number.Bin),
            (r'0[0-7_]+[lL]?', Number.Oct),
            (r'0|[1-9][0-9_]*[lL]?', Number.Integer),
            (r'[~^*!%&\[\](){}<>|+=:;,./?-]', Operator),
            (r'\n', Text)
        ],
        'class': [
            (r'([^\W\d]|\$)[\w$]*', Name.Class, '#pop')
        ],
    }
