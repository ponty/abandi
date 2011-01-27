Usage
==================================

update
---------

update some games  in database from gamebase64_

..  [[[cog
..  sh2(cog,'python -m abandi.update gb64 3020-3023 --force')
..  ]]]

::

	$ python -m abandi.update gb64 3020-3023 --force
	force updating gb64/3020... found:"Galaga"... OK
	force updating gb64/3021... found:"Galaga"... OK
	force updating gb64/3022... found:"Galaxia 7"... OK
	force updating gb64/3023... found:"Galaxian"... OK

..
..  [[[end]]]

or download the default game database::

    $ python -m abandi.dbdownload

install
---------

install galaga_

..  [[[cog
..  sh2(cog,'python -m abandi.install gb64 3020')
..  ]]]

::

	$ python -m abandi.install gb64 3020
	downloading Galaga... OK
	unpacking Galaga... OK

..
..  [[[end]]]


check database
---------------


..  [[[cog
..  sh2(cog,'python -m abandi.info gb64 3020')
..  ]]]

::

	$ python -m abandi.info gb64 3020
	source:              gb64
	id:                  3020
	name:                Galaga
	platform:            c64
	game_file_url:       http://gamebase64.hardabasht.com/games/g/GALAGA1_03020_02.zip
	release_year:        1982
	genre:               Shoot'em Up - Space Invaders
	programmer:          Henrik Wening
	language:            English
	musician:            None
	publisher:           Henrik Wening
	home_url:            http://www.gamebase64.com/game.php?id=3020
	music_file_url:      None
	screenshot_url_list: http://www.gb64.com/Screenshots/G/Galaga_v1.png|http://www.gb64.com/Screenshots/G/Galaga_v1_1.png
	zip:                 /home/titi/.abandi/cache/gamezip/gb64/http___gamebase64.hardabasht.com_games_g_GALAGA1_03020_02.zip
	dir:                 /home/titi/.abandi/games/gb64/Galaga.3020

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

run game
---------------

run galaga_ by id::

    $ python -m abandi.run gb64 3020

run galaga_ by name::

    $ python -m abandi.srun --name galaga

run `maniac mansion`_ using vice_::

    $ python -m abandi.run gb64 4577 --runner vice

run `maniac mansion`_ using scummvm_::

    $ python -m abandi.run gb64 4577 --runner scummvm

.. _galaga: http://www.gamebase64.com/game.php?id=3020
.. _scummvm: http://www.scummvm.org/
.. _vice: http://www.viceteam.org/
.. _`maniac mansion`: http://www.gamebase64.com/game.php?id=4577
.. _gamebase64: http://www.gamebase64.com



