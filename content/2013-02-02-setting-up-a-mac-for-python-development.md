Title: Setting Up a Mac for Python Development
date: 2013-02-02 11:01
comments: true
slug: setting-up-a-mac-for-python-development

<!-- PELICAN_BEGIN_SUMMARY -->

*Edit, August 2013: my current favorite way to set up a python installation
on mac (and any other system) is to use the
[anaconda](https://store.continuum.io/) package offered by Continuum
Analytics.  It's free, full-featured, and extremely easy to use.*

{% img left /images/OSX10.8.png 'OSX 10.8 Logo' %} A few weeks ago,
after years of using Linux exclusively for all my computing,
I started a research fellowship in a new department
and found a brand new Macbook Pro on my
desk.  Naturally, my first instinct was to set up the system for efficient
Python development.  In order to help others who  might find themself in a
similar situation, I took some notes on the process, and I'll summarize
what I learned below.

<!-- PELICAN_END_SUMMARY -->

First, a disclaimer: I can't promise that these suggestions are the best or most
effective way to proceed.  I'm by no stretch of the imagination
a Mac expert: the last Apple product I used regularly was the trusty
Macintosh Classic my parents bought when I was in middle school.  I
primarily used it for all-day marathons of
[RoboSport](http://en.wikipedia.org/wiki/RoboSport) and
[Civilization](http://en.wikipedia.org/wiki/Civilization_%28video_game%29),
with occasional breaks to teach myself programming in Hypercard. But I digress.

Before moving on to the summary of what I learned,
I should note that all of the following was done on OSX 10.8: there
will likely be differences between OSX versions.  I've done my best to note
all the relevant details, and I hope you will find this helpful!


## Accessing the Terminal ##
{% img left /images/OSX_terminal.png 'OSX 10.8 Terminal Icon' %} 
Being from a Linux background, I was interested in setting up a
Linux-like work environment, doing nearly everything from the terminal.
Fortunately, OSX is built on unix, with a terminal integrated into the
operating system.

To open a terminal, open the finder, click "Applications" and search for
"Terminal".  To make it easier to access in the future, I dragged the icon down
to the *dock*, the collection of icons usually found on the bottom or side
of the screen.  Clicking the icon will open a familiar bash terminal that
can be used to explore your Mac in a more user-friendly way.



## Setting Up MacPorts ##
To set up the rest of the system components, I opted to use MacPorts, which is
a package management system similar to ``apt`` or ``yum`` on ubuntu and
debian systems.  There are probably alternatives to MacPorts, but I found
it very intuitive, quick, and powerful.

You can download MacPorts for free on the
[MacPorts website](http://www.macports.org).  You'll have to install it for
the correct OSX version --  to check which OSX version you're running,
click "about this computer" under the apple icon at the top-left of
the desktop. Unfortunately, I was following the slightly outdated
[MacPorts guide](http://guide.macports.org/) and got a few errors:

```
Error: No Xcode installation was found.
Error: Please install Xcode and/or run xcode-select to specify its location.
Error:
Warning: xcodebuild exists but failed to execute
Warning: Xcode does not appear to be installed; most ports will likely fail to build.
```

This indicates that [Xcode](https://developer.apple.com/xcode/)
is not yet installed.  Xcode is a a collection of developer tools for the
Mac, and it can be freely downloaded at the Apple App store.  You'll need
to create an Apple account to access it, and then make sure you have a
fast internet connection: the download is about 1.6GB.  Once it's downloaded,
find the XCode icon in the Applications menu and click to install.

With this done, I tried installing MacPorts again, but still got an error:

```
Error: Unable to open port: can't read "build.cmd": Failed to locate 'make' in path: '/opt/local/bin:/opt/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin' or at its MacPorts configuration time location, did you move it?
```

This indicates that the command-line tools are not installed by default.
To fix this, run Xcode, select Xcode->preferences from the menu bar, click
downloads, select "command-line tools", and click install.
You'll also need Xorg tools, which I installed through
[XQuartz](http://xquartz.macosforge.org/landing/).


## Installing Python ##
Now that MacPorts is installed, it's very straightforward to install several
versions of Python and other programs.  MacPorts allows access to a standard
repository of programs and packages, which can be explored, downloaded, and
installed using the ``port`` command.

First of all, run

```
sudo port selfupdate
```

which updates the MacPorts base to the latest release.  Another useful
thing to know about is the MacPorts ``search`` command.  For example, to
see all the available packages which mention "python", use

```
port search python
```

This will list all the python versions available.  I installed both Python
2.7 and Python 3.3

```
sudo port install python27
sudo port install python33
```

If you want ``python`` on the command-line to point to a particular version,
this can be specified with the ``select`` command:

```
sudo port select --set python python27
```

You can now check that typing ``python --version`` in the terminal returns
version 2.7.


## Installing Numpy, Scipy, etc. ##
My scientific development in Python relies on several packages:
particularly ``numpy``, ``scipy``, ``matplotlib``, ``ipython``, ``cython``,
``scikits-learn``, ``virtualenv``, ``nose``, ``pep8``, and ``pip``.
Here is the series of commands to set these up for Python 2.7:

```
sudo port install py27-numpy
sudo port install py27-scipy
sudo port install py27-matplotlib

sudo port install py27-tornado
sudo port install py27-zmq  # zmq & tornado needed for notebook/parallel
sudo port install py27-ipython
sudo port select --set ipython ipython27

sudo port install py27-cython
sudo port select --set python cython27

sudo port install py27-scikits-learn

sudo port install py27-virtualenv
sudo port install virtualenv_select
sudo port select --set virtualenv virtualenv27

sudo port install py27-nose-testconfig
sudo port select --set nosetests nosetests27

sudo port install py27-pep8
sudo port install pep8_select
sudo port select --set pep8 pep827

sudo port install py27-pip
```
Unfortunately, there seems to not yet be a ``port select`` command
for pip.  This bug has been reported and is noted
[here](http://trac.macports.org/ticket/36178).


### Setting up a Virtual Environment ###
For Python development, I find it vital to make a good use of virtual
environments.  Virtual environments, enabled by the
[virtualenv](http://pypi.python.org/pypi/virtualenv) package,
allow you to install several different versions of various python packages,
such that the installations are mostly independent.  I generally keep
stable released versions of packages in the system-wide python install,
and use these environments to develop the packages.  That way, I can
test the compilation/installation of a new feature in scipy or scikit-learn
without breaking my tried-and-true system installation.

Here we'll set up a virtual environment called ``default``
in a ``PyEnv`` subdirectory, and
then install ``numpy`` in that environment using ``pip``.
```
mkdir ~/PyEnv
cd ~/PyEnv
virtualenv default
source default/bin/activate
pip install numpy
```


## Other Programs to Install ##
There are several other things I found helpful to install.  First, the ``g95``
Fortran compiler for building scipy and other packages which require fortran:
```
sudo port install g95
```
Also, we'll install and configure the tool every open source developer needs:
```
sudo port install git
git config --global user.name "John Doe"
git config --global user.email john@doe.com
```

Another essential is a good text editor.  There are several good open source
options for this.

{% img left /images/textmate_icon.jpg 80 80 'Textmate icon' %}
**Textmate** is a Mac native text editor which has many nice features, works
nicely on mac, and is fairly clean and nice to use:
```
sudo port install textmate2
mate tmp.txt
```

{% img left /images/vim_icon.png 80 80 'Vim icon' %}
**Vim** is another popular text editor: there is both a command-line version
and a GUI version available:
```
sudo port install vim
sudo port install MacVim
vim tmp.txt
```

{% img left /images/emacs_icon.jpeg 80 80 'Emacs icon' %}
**Emacs** is my text editor of choice, and like Vim there is both a
command-line version and a GUI version:
```
sudo port install emacs
sudo port install emacs-app
emacs tmp.txt
```
There are several other GUI emacs versions available as well (e.g.
``xemacs`` and ``emacs-mac-app``): I found that I liked ``emacs-app`` the
best.  Unfortunately, it lives in the "Applications" folder, and there
doesn't seem to be a way to configure the emacs GUI to work the same way
as the default emacs behavior on linux (see the related discussion thread
[here](http://stackoverflow.com/questions/10171280/how-to-launch-gui-emacs-from-command-line-in-osx)).
I ended up putting the emacs GUI in the dock next to the terminal, and I
access it from there.


## Final Thoughts ##
I've had this setup on my new Macbook for about two weeks now,
and it seems to be working well for my daily python programming tasks.
I hope that this post will be useful to someone out there.  I'm still
learning as well -- if you have any pro tips for me or for other readers,
feel free to leave them in the comments below!

Happy hacking.
