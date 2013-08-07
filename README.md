Pythonic Perambulations
-----------------------
This is a port of my blog to the [Pelican](http://blog.getpelican.com/)
blogging platform.  Experimental for now, but I hope to move everything
over soon.

Requirements
------------
- Recent version of
  [pelican-plugins](http://github.com/getpelican/pelican-plugins):
  Make sure the path is specified correctly in ``pelicanconf.py``.
  This must include the ``liquid_tags`` plugin from this PR:
  https://github.com/getpelican/pelican-plugins/pull/21

- Recent version of [IPython](http://github.com/ipython/ipython).  The
  liquid_tags plugin above requires IPython 1.0.  Note that previously
  this could be built with the stand-alone nbconvert package.  That
  no longer works with the recent liquid_tags plugin.

- Recent version of [Pelican](http://github.com/getpelican/pelican).  For
  the static paths (downloads, images, figures, etc.) to appear in the right
  place, Pelican 3.3+ must be used.

- Recent version of
  [pelican-octopress-theme](https://github.com/duilio/pelican-octopress-theme),
  with an additional few lines in the header (see ``pelicanconf.py`` for
  a description of what is needed).
  For a few of the options, this requires several additions:
  
  - https://github.com/duilio/pelican-octopress-theme/pull/11: social media
  - https://github.com/duilio/pelican-octopress-theme/pull/12: disqus specification
  - https://github.com/duilio/pelican-octopress-theme/pull/13: extra header args