Usage
==================================

update
---------

update some games from `gamebase64 <http://www.gamebase64.com>`_

..  [[[cog
..  sh2(cog,'python -m abandi.update gb64 3021-3023 --force')
..  ]]]
::

	$ python -m abandi.update gb64 3021-3023 --force
	force updating gb64/3021... found:"Galaga"... OK
	force updating gb64/3022... found:"Galaxia 7"... OK
	force updating gb64/3023... found:"Galaxian"... OK
..
..  [[[end]]]

install
---------

install `Galaga <http://www.gamebase64.com/game.php?id=3021>`_

..  [[[cog
..  sh2(cog,'python -m abandi.install gb64 3021')
..  ]]]
::

	$ python -m abandi.install gb64 3021
	downloading Galaga... OK
	unpacking Galaga... OK
..
..  [[[end]]]


check database
---------------


..  [[[cog
..  sh2(cog,'python -m abandi.info gb64 3021')
..  ]]]
::

	$ python -m abandi.info gb64 3021
	source:              gb64
	id:                  3021
	name:                Galaga
	platform:            c64
	game_file_url:       http://gamebase64.hardabasht.com/games/g/GALAGA2_03021_01.zip
	release_year:        1983
	genre:               Shoot'em Up - Space Invaders
	programmer:          Henrik Wening
	language:            English
	musician:            None
	publisher:           (Not Published)
	home_url:            http://www.gamebase64.com/game.php?id=3021
	music_file_url:      None
	screenshot_url_list: http://www.gb64.com/Screenshots/G/Galaga_v2.png
	zip:                 /home/titi/.abandi/cache/gamezip/gb64/http___gamebase64.hardabasht.com_games_g_GALAGA2_03021_01.zip
	dir:                 /home/titi/.abandi/games/gb64/Galaga.3021
..
..  [[[end]]]


search database
---------------


..  [[[cog
..  sh2(cog,'python -m abandi.search -n galaga')
..  ]]]
::

	$ python -m abandi.search -n galaga
	[gb64 3020 c64] Galaga
	[gb64 3021 c64] Galaga
..
..  [[[end]]]
