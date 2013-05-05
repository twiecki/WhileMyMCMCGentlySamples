Pythonic Perambulations
-----------------------
This is a port of my blog to the [Pelican](http://blog.getpelican.com/)
blogging platform.  Experimental for now, but I hope to move everything
over soon.

Requirements
------------
- Recent version of
  [pelican-plugins](https://github.com/getpelican/pelican-plugins):
  Make sure the path is specified correctly in ``pelicanconf.py``.

- Recent version of
  [nbconvert](https://github.com/ipython/nbconvert):
  Make sure that your ``PYTHONPATH`` system variable points to this directory.
  This may need to be updated in the future when IPython 1.0 is released.

- Recent version of
  [pelican-octopress-theme](https://github.com/duilio/pelican-octopress-theme),
  with an additional few lines in the header (see ``pelicanconf.py`` for
  a description of what is needed).