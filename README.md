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
  This must include the ``liquid_tags`` plugin from this PR:
  https://github.com/getpelican/pelican-plugins/pull/21

- Recent version of
  [nbconvert](https://github.com/ipython/nbconvert):
  Make sure that your ``PYTHONPATH`` system variable points to this directory.
  This will need to be updated in the future: the nbconvert package is	
  currently undergoing an extensive refactoring for IPython 1.0.

- Recent version of
  [pelican-octopress-theme](https://github.com/duilio/pelican-octopress-theme),
  with an additional few lines in the header (see ``pelicanconf.py`` for
  a description of what is needed).
  For a few of the options, this requires several additions:
  
  - https://github.com/duilio/pelican-octopress-theme/pull/11: social media
  - https://github.com/duilio/pelican-octopress-theme/pull/12: disqus specification
  - https://github.com/duilio/pelican-octopress-theme/pull/13: extra header args