======
abandi
======

Console-based abandonware game installer and runner.
No GUI.
Games are downloaded over internet.

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
------------

The easiest way to get abandi is if you have setuptools_ installed::

    easy_install abandi

.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall


