system information
==================================

versions
---------

..  [[[cog
..  sh2(cog,'python -m abandi.lsversion')
..  ]]]

::

	$ python -m abandi.lsversion
	python 		2.6.6
	abandi 		0.0.2
	dosbox		0.74
	hatari		1.4.0
	openmsx		0.8.0
	p7zip		9.04
	patool		unknown
	scummvm		1.1.1
	soup		3.1.0.1
	stella		3.1.2
	unrar		3.93
	vice		unknown
	zsnes		unknown

..
..  [[[end]]]

plugins
---------

..  [[[cog
..  sh2(cog,'python -m abandi.lsplugin')
..  ]]]

::

	$ python -m abandi.lsplugin
	abandoneer		game_source
	abandonia		game_source
	allunpacker		unpacker
	cache		downloader
	curl		downloader
	dosbox		runner
	gb64		game_source
	hatari		runner
	lxml		html_parser
	openmsx		runner
	oscomp		game_source
	osd		game_source
	p7zip		unpacker
	patool		unpacker
	scummvm		runner
	soup		html_parser
	stella		runner
	unrar		unpacker
	urllib		downloader
	vice		runner
	zsnes		runner

..
..  [[[end]]]
