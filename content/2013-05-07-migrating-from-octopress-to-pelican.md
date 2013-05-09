Title: Migrating from Octopress to Pelican
date: 2013-05-07 17:00
comments: true
slug: migrating-from-octopress-to-pelican

<!-- PELICAN_BEGIN_SUMMARY -->
After nine months on Octopress, I've decided to move on.

I should start by saying that Octopress is a great platform for static
blogging: it's powerful, flexible, well-supported, well-integrated with
GitHub pages, and has tools and plugins to do just about anything you might
imagine.  There's only one problem:

It's written in Ruby.

Now I don't have anything against Ruby per se.  However, it was starting to
seem a bit awkward that a blog called *Pythonic Perambulations*
was built with Ruby, especially given the availability of so many
excellent Python-based static site generators
([Hyde](http://hyde.github.io/),
[Nikola](http://nikola.ralsina.com.ar/),
and [Pelican](http://getpelican.com) in particular).

Additionally, a few things with Octopress were starting to become difficult:
<!-- PELICAN_END_SUMMARY -->
first, I wanted a way to easily insert IPython notebooks into posts.
Sure, I developed a [hackish solution](/blog/2012/10/04/blogging-with-ipython/)
to notebooks in Octopress which had worked
well enough for a while, but a cleaner method would have involved
digging into the Ruby source code and writing a full-fledged Octopress
extension, based on nbconvert.  This would have involved a fair bit of effort
to learn Ruby and figure out how to best interface it with the Python nbconvert
code. Second, Ruby has so many strange and difficult pieces:
GemFiles, RVM, rake... and I never took the time to really understand
the real purpose of all of them (self-reflection:
what parts of Python would seem strange and difficult if I hadn't
been using them for so many years?).  The black-box nature of the process,
at least in my own case, was starting to bother me.

But the kicker was this: In January I got a new computer, and after a reasonable
amount of effort was unable to successfully build my blog.  I've been writing
my posts exclusively on my old laptop which I somehow managed to successfully
set up last August.  But that laptop now has a sorely outdated Ubuntu distro
that I couldn't upgrade for fear of losing the ability to update my blog.
Needless to say, this was not the most effective setup.

It was time to switch my blog engine to Python.

## Choosing a Python Static Generator ##
I started asking around, and found that there were three solid contenders for
a Python-based platform to replace Octopress: [Hyde](http://hyde.github.io/),
[Nikola](http://nikola.ralsina.com.ar/),
and [Pelican](http://getpelican.com).  I gave Hyde a test-run a few weeks ago
in re-making my [website](http://www.astro.washington.edu/users/vanderplas),
and I really like it: it's clean, straightforward, powerful, and easy to use.
The documentation is a bit lacking, though, and I think it would take a fair
bit more effort at this point to build a more complicated site with Hyde.

Nikola and Pelican both seem to be well-loved by their users, but I had to
choose one.  I went with Pelican for one simple reason:
it has more GitHub forks.  I'm sure this is entirely
unfair to Nikola and all the contributors who have poured
their energy into the project, but I had to choose one way or another.
I'm pleased to say that Pelican has not been a disappointment:
I've found it to be flexible and powerful.  It has an active developer-base,
and makes available a wide array of themes and plugins.
For the few extra pieces I needed, I found the plugin and theming
API to be well-documented and straightforward to use.

## Migrating to Pelican from Octopress
I won't attempt to write a one-size-fits-all guide to migrating to Pelican
from Octopress: there are too many possibile combinations of formats, plugins,
themes, etc.  But I will walk through my own process in some detail, in hopes
that it might help others who find themselves in a similar predicament.

I had several goals when doing this migration:

- I wanted, as much as possible, to maintain the look and feel of the blog.
  I like the default Octopress theme: it's simple, clean, compact, and
  includes all the aspects I need for a good blog.
- I wanted, as much as possible, to leave the source of my posts unmodified:
  luckily Pelican supports writing posts in markdown and allows easy insertion
  of custom plugins, so this was relatively easy to accommodate.
- I wanted to maintain the history of Disqus comments for each page, as well
  as the Twitter and Google Pages tools.
- I wanted, as much as possible, to maintain the same URLs for all content,
  including posts, notebooks, images, and videos.
- I wanted a clean way to insert html-formatted IPython notebooks into blog
  posts. Nearly half my posts are written as notebooks, and the
  [old way](/blog/2012/10/04/blogging-with-ipython/) of including them
  was becoming much too cumbersome.
  
I was able to suitably address all these goals with Pelican
in a few evenings' effort.  Some of it was already
built-in to the Pelican settings architecture, some required
customization of themes and extensions, and some required writing some brand
new plugins.  I'll summarize these aspects below:

### Blog theme ###
As I mentioned, I wanted to keep the look and feel of the blog consistent.
Luckily, someone had gone before me and created an
[octopress Pelican theme](https://github.com/duilio/pelican-octopress-theme)
which did most of the heavy lifting.  I contributed
a few additional features, including the ability to
[specify Disqus tags](https://github.com/duilio/pelican-octopress-theme/pull/12)
and maintain comment history, to
[add Twitter, Google Plus, and Facebook](https://github.com/duilio/pelican-octopress-theme/pull/11) links in the sidebar and footer,
to add a [custom site search](https://github.com/duilio/pelican-octopress-theme/pull/15)
box which appears in the upper right of the
navigation panel, as well as a few
[other](https://github.com/duilio/pelican-octopress-theme/pull/14)
[tweaks](https://github.com/duilio/pelican-octopress-theme/pull/13).
The result is what you see here: nearly identical to the old layout, with
all the bells and whistles included.

### Octopress Markdown to Pelican Markdown ###
Octopress has a few plugins which add some syntactic sugar to the markdown
language.  These are tags specified in
[Liquid](https://github.com/Shopify/liquid)-style syntax:

    {% literal tag arg1 arg2 ... %}

I have made extensive use of these in my octopress posts, primarily to insert
videos, images, and code blocks from file.
In order to accommodate this in Pelican, I wrote
a [Pelican plugin](https://github.com/getpelican/pelican-plugins/pull/21)
which wraps a custom Markdown preprocessor written via the
[Markdown extension API](http://pythonhosted.org/Markdown/extensions/api.html)
which can correctly interpret these types of tags.  The tags ported from
octopress thus far are:

#### The Image Tag ####
The image tag allows insertion of an image into the post with a
specified size and position:

    {% literal img [position] /url/to/img.png [width] [height] [title] [alt] %}

Here is an example of the result of the image tag:

{% img /images/galaxy.jpg 300 200 A Galaxy %}

#### The Video Tag ####
The video tag allows embedding of an HTML5/Flash-compatible video
into the post:

    {% literal video /url/to/video.mp4 [width] [height] [/url/to/poster.png] %}

Here is an example of the output of the video tag:

{% video /downloads/videos/animate_square.mp4 240 180 /downloads/videos/animate_square.png %}

(see [this post](/blog/2012/09/26/optical-illusions-in-matplotlib/) for a
description of this video).

#### The Code Include Tag ####
The ``include_code`` tag allows the insertion of formatted lines from
a file into the post, with a title and a link to the source file:

    {% literal include_code filename.py [lang:python] [title] %}

Here is an example of the output of the code include tag:

{% include_code hello_world.py lang:python Hello World %}

For more information on using these tags, refer to the
[module doc-strings](https://github.com/getpelican/pelican-plugins/pull/21).

### Maintaining Disqus Comment Threads ###
Static blogs are fast, lightweight, and easy to deploy.  A disadvantage, though,
is the inability to natively include dynamic elements such as comment threads.
[Disqus](http://disqus.com/)
is a third-party service that skirts this disadvantage very
seamlessly.  All it takes is to add a small javascript snippet with some
identifiers in the appropriate place on your page, and Disqus takes care of
the rest.  To keep the comment history on each page required assuring that
the site identifier and page identifiers remained the same between blog
versions.  This part happens within the theme, and my
[Disqus PR](https://github.com/duilio/pelican-octopress-theme/pull/12)
to the Pelican Octopress theme made this work correctly.

### Maintaining the URL structure ###
By default, Octopress stores posts with a structure looking like
``blog/YYYY/MM/DD/article-slug/``.  The Pelican default is different, but
easy enough to change.  In the ``pelicanconf.py``
settings file, this corresponds to the following:

    ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
    ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

Next, at the top of the markdown file for each article, the metadata needs
to be slightly modified from the form used by Octopress -- here is the
actual metadata used in the document that generates this page:

    Title: Migrating from Octopress to Pelican
    date: 2013-05-07 17:00
    slug: migrating-from-octopress-to-pelican

Additionally, the static elements of the blog (images, videos, IPython
notebooks, code snippets, etc.) must be put within the correct directory
structure.  These static files should be put in paths which are specified
via the ``STATIC_PATHS`` setting:

    STATIC_PATHS = ['images', 'figures', 'downloads']

Pelican presented a challenge here: as of the time of this
writing, Pelican has a hard-coded ``'static'`` subdirectory where these
static paths are saved.  I submitted a
[pull request](https://github.com/getpelican/pelican/pull/875) to Pelican
that replaces this hard-coded setting with a configurable path: because
the change conflicts with a
[bigger refactoring](https://github.com/getpelican/pelican/pull/795)
of the code which is ongoing, the PR will not be merged.  But until this
new refactoring is finished, I'll be using
[my own branch](https://github.com/jakevdp/pelican/tree/specify-static)
of Pelican to make this blog, and specify the correct static paths.

### Inserting Notebooks ###
The ability to seamlessly insert IPython notebooks into posts was one of the
biggest drivers of my switch to Pelican.  Pelican has an
[ipython notebook plugin](http://danielfrg.github.io/blog/2013/03/08/pelican-ipython-notebook-plugin/)
available, but I wasn't completely happy with it.  The plugin implements
a reader which treats the notebooks themselves as the source of a post,
leading to the requirement to insert blog metadata into the notebook itself.
This is a suitable solution, but for my own purposes I much prefer a solution
in which the content of a notebook could be inserted into a stand-alone post,
such that the notebook and the blog metadata are completely separate.

To accomplish this, I added a submodule to my
[liquid_tags](https://github.com/jakevdp/pelican-plugins/blob/liquid_tags/liquid_tags/notebook.py) Pelican plugin which allows the insertion of notebooks
using the following syntax:

    {% literal notebook path/to/notebook.ipynb [cells[i:j]] %}

This inserts the notebook at the given location in the post, optionally
selecting a given range of notebook cells with standard Python list slicing
syntax.

The formatting of notebooks requires some special CSS styles which must
be inserted into the header of each page where notebooks are shown.  Rather
than requiring the theme to be customized to support notebooks, I decided
on a solution where an ``EXTRA_HEADER`` setting is used to specify html
and CSS which
should be added to the header of the main page.  The notebook plugin
saves the required header to a file called ``_nb_header.html`` within
the main source directory.  To
insert the appropriate formatting, we add the following lines to the
settings file, ``pelicanconf.py``:

    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

In the theme file, within the header tag, we add the following:

     {% if EXTRA_HEADER %}
     {{ EXTRA_HEADER }}
     {% endif %}

Here is the result: a short notebook inserted directly into the post:

{% notebook TestNotebook.ipynb %}

##  ##
With all those things in place, the blog was ready to be built.  The result
is right in front of you: you're reading it.  If you'd like to see the source
from which this blog built, it's available at
[http://www.github.com/jakevdp/PythonicPerambulations](http://www.github.com/jakevdp/PythonicPerambulations).  Feel free to adapt the configurations and theme
to suit your own needs.

I'm glad to be working purely in Python from now on!