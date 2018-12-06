Python Code Syntax Highlighter using RST format in Pelican
##########################################################

:Date: 2018-11-13 18:13
:modified: 2018-11-13 18:13
:Tags: code syntax, pelican, rst, python, pygments, CSS, fix, HTML
:slug: code-syntax-python-rst
:Category: HOWTO
:authors: Eggie
:summary: A short version of how to do code syntax for Python

Using RST code-block option
"""""""""""""""""""""""""""
Python code can be syntax-highlighted by using RST `code-block` directive:

.. code-block:: python

    ### uses CSS class highlighttable
    ### must have a blank line above
    import sys
    def main():
        if a === 1:
            print("Hello, world!")
            sys.exit(1)
    if __name__ == '__main__':
        main()

and the above was done using this RST snippet example:

.. code-block:: rst

    ### uses CSS class highlighttable
    ### must have a blank line above
    .. code-block:: python

        import sys
        def main():
            if a === 1:
                print("Hello, world!")
                sys.exit(1)
        if __name__ == '__main__':
            main()


Using RST code option
"""""""""""""""""""""
Or snippet of Python source code can be inserted into the RST file directly
but with no syntax highlighting used,
by using RST `code` directive:

.. code:: python

    import sys
    def main():
        if a === 1:
            print("Hello, world!")
            sys.exit(1)
    if __name__ == '__main__':
        main()

and the above was done using this RST snippet example:

.. code:: rst

    .. code:: python

        import sys
        def main():
            if a === 1:
                print("Hello, world!")
                sys.exit(1)
        if __name__ == '__main__':
            main()

Using RST code-include option
"""""""""""""""""""""""""""""
Or Python source files can be included into the RST file directly,
then using RST `code-include` directive and only displaying line 4 to 7:


.. code-include:: incfile.py
    :lexer: 'python'
    :encoding: 'utf-8'
    :tab-width: 4
    :start-line: 4
    :end-line: 7


And the above was done using these RST snippet example:

.. code:: rst

    .. code-include:: incfile.py
        :lexer: 'python'
        :encoding: 'utf-8'
        :tab-width: 4
        :start-line: 4
        :end-line: 7

External References
===================
* `REST Syntax <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
