# Apex Lexer
This module creates a Pygments lexer for the Apex language. Since Apex is largely based on Java,
this lexer is a modified form of the Java lexer.

# Hand-Testing
```bash

$ pygmentize -x -l ./pygments_lexer_apex.py:ApexLexer -f html -O full -o test.html test/apex/FundController.apxc
```

# Note
This was cooked up in about 15 minutes, so it almost certainly does not cover all the lexigraphical
complexities, edge cases, and obscure portions of the Apex language. Contributions to beef it up are welcome.
