Usage
==================================

update
---------

update some games  in database from gamebase64_

.. program-output:: python -m abandi.update gb64 3020-3023 --force
    :prompt:


or download the default game database::

    $ python -m abandi.dbdownload

install
---------

install galaga_

.. program-output:: python -m abandi.install gb64 3020
    :prompt:


check database
---------------

.. program-output:: python -m abandi.info gb64 3020
    :prompt:


search database
---------------

.. program-output:: python -m abandi.search -n galaga
    :prompt:

run game
---------------

run galaga_ by id:

.. program-screenshot:: python -m abandi.run -a gb64 3020
    :prompt:
    :scale: 50 %
    :timeout: 30
    :wait: 5

run galaga_ by name:

.. program-screenshot:: python -m abandi.srun -a --name galaga
    :prompt:
    :scale: 50 %
    :timeout: 30
    :wait: 10

run `maniac mansion`_ using vice_:

.. program-screenshot:: python -m abandi.run -a gb64 4577 --runner vice
    :prompt:
    :scale: 50 %
    :timeout: 30
    :wait: 10

run `maniac mansion`_ using scummvm_:

.. program-screenshot:: python -m abandi.run -a gb64 4577 --runner scummvm
    :prompt:
    :scale: 50 %
    :timeout: 30
    :wait: 10

.. _galaga: http://www.gamebase64.com/game.php?id=3020
.. _scummvm: http://www.scummvm.org/
.. _vice: http://www.viceteam.org/
.. _`maniac mansion`: http://www.gamebase64.com/game.php?id=4577
.. _gamebase64: http://www.gamebase64.com



