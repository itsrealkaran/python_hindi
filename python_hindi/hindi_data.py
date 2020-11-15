# functions:
hebrew_builtins = {
    # numbers
    "": "abs",
    "": "all",
    "": "any",  # not sure about this translate: 'אחד' mean '1' in hebrew.

    # list
    "": "len",
    "": "min",
    "": "max",
    "": 'reversed',
    "":"enumerate",
    "":"map",

    # std
    "": "print",
    "": "input",

    # errors
    "": "ImportError",
    "": "NameError",
    "": "PermissionError",
    "":"Exception",
    "":"FileNotFoundError",
    

    # strings
    '': 'repr',
    "": "exec",
    "":"open"
}

# keywords:
hebrew_keywords = {
    "":
    "hebrew_python",  # TODO : I want to create another module for this.

    # if and booleans:
    "": "if",
    "": "True",
    "": "False",
    "": "and",
    "": "not",
    "": "is",
    "": "else",
    "": "elif",  # אחרתאם ?
    "": "or",

    # loops
    "": "for",
    "": "in",
    "": "range",
    "": "break",
    "": "while",
    "": "continue",

    # types:
    "": "list",
    "": "int",
    "": "float",
    "": "None",
    "": "bool",
    "":"str",
    "": "set()",
    '': 'אובייקט',

    # imports
    "": "from",
    "": "import",
    "": "as",

    # classes and functions
    "": "return",
    "": "class",
    "": "global",
    "": "def",
    "": "pass",
    "": "yield",

    # errors
    "": "try",
    "": "assert",
    "": "raise",
    "": "except",
    "": "finally",
    
    # list
    "": "round()",
    "": "slice()",
    "": "sorted()",
    "": "sum()",
    "": "type()",

    #
    '': "with",
    "": "del",
    "": "lambda",
}
