Console-based abandonware game installer and runner.

Links:
 * home: https://github.com/ponty/abandi
 * documentation: http://ponty.github.com/abandi

Features:
 - Games are serached on abandonware sites, downloaded over internet, 
   unpacked and run by emulators
 - HTML parser back-ends:
     * lxml_
     * BeautifulSoup_
 - downloader back-end: urllib_
 - unpacker back-end: pyunpack_
 - simulator back-ends: 
     * dosbox_
     * openmsx_
     * scummvm_
     * stella_
     * vice_
 - supported python versions: 2.6, 2.7
 
Known problems:
 - tested mostly on linux

Basic usage
------------
The selected game will be downloaded,
unpacked and started by an emulator.

if you know the id::

    $ python -m abandi.run --auto-install gb64 3021

if you have an up-to-date database::

    $ python -m abandi.srun --auto-install --name galaga


.. note::

   It is only a wrapper,so you have to install unpackers (7zip, unrar,..)
   and emulators (dosbox, scummvm, stella, vice,..)

Installation
============

General
--------

 * install Python_
 * install pip_
 * install back-ends for pyunpack_ (optional)
 * install supported emulators (optional)
 * install HTML parsers (optional)
 * install the program::

    # as root
    pip install https://github.com/ponty/abandi/zipball/master    


Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo pip install https://github.com/ponty/abandi/zipball/master
    # optional
    sudo apt-get install unzip unrar p7zip-full
    sudo apt-get install dosbox openmsx scummvm stella vice hatari
    sudo apt-get install python-beautifulsoup python-lxml

Uninstall
----------

::
	
    # as root
    pip uninstall abandi
    
    # database, games
    rm -r ~/.abandi

.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _pyunpack: https://github.com/ponty/pyunpack
.. _Python: http://www.python.org/
.. _dosbox: http://www.dosbox.com/
.. _openmsx: http://openmsx.sourceforge.net/
.. _scummvm: http://www.scummvm.org/
.. _stella: http://stella.sourceforge.net/
.. _vice:   http://www.viceteam.org/
.. _lxml: http://lxml.de/
.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/
.. _urllib: http://docs.python.org/library/urllib.html