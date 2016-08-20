Unspeakably Evil Hacks in Service of Marginally Improved Syntax
---------------------------------------------------------------

Delivered at 3:15 PM on Sat Aug 20 2016 at PyBay.

Running the Slides
~~~~~~~~~~~~~~~~~~

To run the slides, check out the repo and run::

    $ pip install --user virtualenv virtualenvwrapper   # Skip if you already have these.
    $ git submodule init && gitsubmodule update         # Clone vendored pyxl3 submodule.
    $ mkvirtualenv -p $(which python3) pybay2016
    $ source run.sh  # It's important that you source here rather than just invoking ./run.sh!

This should start install all the necessary dependencies into a Python 3
virtualenv named `pytenn2016` and start a Jupyter Notebook server with the
LiveReveal extension installed and running.
