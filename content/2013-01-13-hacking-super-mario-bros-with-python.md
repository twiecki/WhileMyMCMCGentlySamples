Title: Hacking Super Mario Bros. with Python
date: 2013-01-13 10:32
comments: true
slug: hacking-super-mario-bros-with-python

<!-- PELICAN_BEGIN_SUMMARY -->

This weekend I was coming home from the meeting of the
[LSST](http://www.lsst.org) Dark Energy Science Collaboration,
and found myself with a few extra hours in the airport.
I started passing the time by poking around on the [imgur](http://imgur.com)
gallery, and saw a couple animated gifs based on
one of my all-time favorite games, Super Mario Bros.
It got me wondering: could I use matplotlib's animation tools to create these
sorts of gifs in Python?  Over a few beers at an SFO bar, I started to try
to figure it out.  To spoil the punchline a bit, I managed to do it, and the
result looks like this:

{% img center /images/mario.gif %}

This animation was created *entirely in Python and matplotlib*, by scraping the
image data directly from the Super Mario Bros. ROM.  Below I'll explain how
I managed to do it.

<!-- PELICAN_END_SUMMARY -->

## Scraping the Pixel Data ##

Clearly, the first requirement for this pursuit
is to get the pixel data used to construct the
mario graphics.  My first thought was to do something sophisticated like
[dictionary learning](http://en.wikipedia.org/wiki/Machine_learning#Sparse_Dictionary_Learning) on a collection of screen-shots from the game
to build up a library of thumbnails.  That would be an interesting pursuit
in itself, but it turns out it's much more straightforward to directly
scrape the graphics from the source.

It's possible to find digital copies of most
Nintendo Entertainment System (NES) games online.
These are known as ROMs, and can be played using one of
several NES emulators available for various operating systems.
I'm not sure about the legality of these
digital game copies, so I won't provide a link to them here.  But the internet
being what it is, you can search Google for some variation of "Super Mario
ROM" and pretty easily find a copy to download.

One interesting aspect of ROMs for the original NES is that
they use raw byte-strings to store 2-bit (i.e. 4-color), 8x8 thumbnails from
which all of the game's graphics are built.
The collection of these byte-strings
are known as the "pattern table" for the game, and there is generally a
separate pattern table for foreground and background images.
In the case of NES games, there are
256 foreground and 256 background tiles, which can be extracted directly from
the ROMs if you know where to look (incidentally, this is one of the things
that made the NES an "8-bit" system.  2^8 = 256, so eight bits are required
to specify any single tile from the table).

## Extracting Raw Bits from a File ##
If you're able to obtain a copy of the ROM, the first step to getting at the
graphics is to extract the raw bit information.
This can be done easily in Python using ``numpy.unpackbits``
and ``numpy.frombuffer`` or ``numpy.fromfile``.
Additionally, the ROMs are generally stored using
zip compression.  The uncompressed data can be extracted using Python's
built-in ``zipfile`` module.  Combining all of this, we extract the raw file
bits using a function like the following:

``` python
import zipfile
import numpy as np

def extract_bits(filename):
    if zipfile.is_zipfile(filename):
        zp = zipfile.ZipFile(filename)
        raw_buffer = zp.read(zp.filelist[0])
        bytes = np.frombuffer(raw_buffer, dtype=np.uint8)
    else:
        bytes = np.fromfile(filename, dtype=np.uint8)
    return np.unpackbits(bytes)
```

This function checks whether the file is compressed using zip, and extracts
the raw bit information in the appropriate way.

## Assembling the Pattern Tables ##
The thumbnails which contain the game's graphics patterns are not at any set
location within the file.  The location is specified within the assembly
code that comprises the program, but for our purposes
it's much simpler to just visualize
the data and find it by-eye.  To accomplish this,
I wrote a Python script
(download it [here](/downloads/code/mario/view_pattern_table.py))
based on the above data extraction code
which uses matplotlib to interactively display the contents of the file.
Each thumbnail is composed from 128 bits:
two 64-bit chunks each representing an 8x8 image with one bit per pixel.
Stacking the two results in two bits per pixel, which are able to
represent four colors within each thumbnail.
The first few hundred chunks are difficult to interpret by-eye. They appear
similar to a 2D bar code: in this case the "bar code" represents pieces of the
assembly code which store the Super Mario Bros. program.

{% img center /images/mario_pattern_sourcecode.png 400 %}

Scrolling down toward the end of the file, however, we can quickly recognize
the thumbnails which make up the game's graphics:

{% img center /images/mario_pattern_foreground.png 400 %}

This first pattern table contains all the foreground graphics for the game.
Looking closely, the first few thumbnails
are clearly recognizable as pieces of Mario's head and body.
Going on we see pieces of various enemies in the game, as well as the iconic
mushrooms and fire-flowers.

{% img center /images/mario_pattern_background.png 400 %}

The second pattern table contains all the background graphics for the game.
Along with numbers and text, this contains the pieces which make up mario's
world: bricks, blocks, clouds, bushes, and coins.
Though all of the above tiles are shown in grayscale, we can add color by
simply changing the matplotlib Colormap, as we'll see below.

## Combining Thumbnails and Adding Color ##
Examining the pattern tables above, we can see that big Mario is made up of
eight pattern tiles stitched together, while small Mario is made up of four.
With a bit of trial and error, we can create each of the full frames and
add color to make them look more authentic.  Below are all of the frames used
to animate Mario's motion throughout the game:

{% img center /images/mario_graphics1.png 400 %}

Similarly, we can use the thumbnails to construct some of the other
familiar graphics from the game, including the goombas, koopa troopas,
beetle baileys, mushrooms, fire flowers, and more.

{% img center /images/mario_graphics2.png 350 %}

The Python code to extract, assemble, and plot these images can be downloaded
[here](/downloads/code/mario/draw_mario.py).

## Animating Mario ##
With all of this in place, creating an animation of Mario is relatively easy.
Using matplotlib's animation tools (described in a
[previous post](/blog/2012/08/18/matplotlib-animation-tutorial/)), all it
takes is to decide on the content of each frame, and stitch the frames together
using matplotlib's animation toolkit.  Putting together big Mario with some
scenery and a few of his friends, we can create a cleanly looping animated gif.

The code used to generate this animation is shown below.  We use the same
``NESGraphics`` class used to draw the frames above, and stitch them together
with a custom class that streamlines the building-up of the frames.
By uncommenting the line near the bottom, the result will be saved as an
animated GIF using the ImageMagick animation writer that I
[recently contributed](https://github.com/matplotlib/matplotlib/pull/1337)
to matplotlib.  The ImageMatick plugin has not yet made it into a
released matplotlib version, so using the save command below will
require installing the development version of matplotlib, available for
download on [github](http://github.com/matplotlib/matplotlib).

{% include_code mario/animate_mario.py lang:python "Mario Animation" %}

The result looks like this:

{% img center /images/mario.gif %}

Pretty good!  With a bit more work, it would
be relatively straightforward to use the above code to do some more
sophisticated animations: perhaps recreate a full
level from the original Super Mario Bros, or even design your own custom
level.  You might think about taking the extra step and trying to make Mario's
movements interactive.  This could be a lot of fun, but probably very difficult
to do well within matplotlib.
For tackling an interactive mario in Python, another framework such as
[Tkinter](http://docs.python.org/2/library/tkinter.html) or
[pygame](http://www.pygame.org/) might be a better choice.

I hope you enjoyed this one as much as I did -- happy coding!
