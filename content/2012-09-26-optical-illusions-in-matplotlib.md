Title: Optical Illusions in Matplotlib
date: 2012-09-26 07:27
comments: true
slug: optical-illusions-in-matplotlib

<!-- PELICAN_BEGIN_SUMMARY -->
A while ago I posted some information on the new matplotlib animation
package (see my tutorial
[here](/blog/2012/08/18/matplotlib-animation-tutorial) and
a followup post [here](/blog/2012/09/05/quantum-python)).  In them, I show
how easy it is to  use matplotlib to create simple animations.

This morning I came across this cool optical illusion on
[gizmodo](http://gizmodo.com/5945194/this-optical-trick-is-annoying-the-hell-out-of-me)

{% img /images/original_illusion.gif %}

<!-- PELICAN_END_SUMMARY -->

It intrigued me, so I decided to see if I could create it using matplotlib.
Using my previous template and a bit of geometry, I was able to finish it
before breakfast!  Here's the code:

{% include_code animate_square.py Optical Illusion  %}

And here's the result:

{% video /downloads/videos/animate_square.mp4 360 270 /downloads/videos/animate_square.png %}

This just confirms my suspicion that a few lines of python really can do
anything.