from setuptools import setup

setup(
    name='pygments-lexer-apex',
    version='0.2.0',
    url='https://github.com/shawalli/pygments-lexer-apex',
    license='MIT',
    author='Shawn Wallis',
    author_email='shawn.p.wallis@gmail.com',
    description='Pygments Salesforce Apex lexer',
    keywords = 'syntax highlighting',
    platforms = 'any',
    py_modules=['pygments_lexer_apex'],
    entry_points='[pygments.lexers]\napexlexer = pygments_lexer_apex:ApexLexer',
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Intended Audience :: Developers',
      'Development Status :: 5 - Alpha',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Operating System :: OS Independent',
      'Topic :: Text Processing :: Filters',
      'Topic :: Utilities'
    ]
)
