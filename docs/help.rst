command line help
==================================

..  [[[cog
..  import abandi
..  ls='dbdownload parse update info search install run srun'.split()
..  for x in ls:
..      cog.outl('\n%s\n---------\n' % x)
..      sh2(cog,'python -m abandi.%s --help' % x)
..  ]]]

dbdownload
---------


::

	$ python -m abandi.dbdownload --help
	usage: dbdownload.py [-h] [-u URL] [--debug]
	
	downloads and unpacks game database
	
	optional arguments:
	  -h, --help         show this help message and exit
	  -u URL, --url URL  : packed sqlite file [default=https://github.com/download
	                     s/ponty/abandi/parsedb.sqlite.7z]
	  --debug            Set logging level to DEBUG

..

parse
---------


::

	$ python -m abandi.parse --help
	usage: parse.py [-h] [--debug] source id
	
	parse game on source and print all information
	
	positional arguments:
	  source      : ['gb64',..]
	  id          : ['1',..]
	
	optional arguments:
	  -h, --help  show this help message and exit
	  --debug     Set logging level to DEBUG

..

update
---------


::

	$ python -m abandi.update --help
	usage: update.py [-h] [-f] [--debug] source id
	
	parse and update game in database
	
	positional arguments:
	  source       : ['all','gb64',..]
	  id           : ['all','1','1-5','1,5-8,10',..]
	
	optional arguments:
	  -h, --help   show this help message and exit
	  -f, --force
	  --debug      Set logging level to DEBUG

..

info
---------


::

	$ python -m abandi.info --help
	usage: info.py [-h] [--debug] source id
	
	print all information for game in database
	
	positional arguments:
	  source      : ['gb64',..]
	  id          : ['1',..]
	
	optional arguments:
	  -h, --help  show this help message and exit
	  --debug     Set logging level to DEBUG

..

search
---------


::

	$ python -m abandi.search --help
	usage: search.py [-h] [-c COLUMNS] [-w WHERE] [-o ORDERBY] [-n NAME]
	                 [-p PLATFORM] [-s SOURCE] [-r RUNNER] [--debug]
	
	search in game database
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -c COLUMNS, --columns COLUMNS
	                        [default=[source id platform] name]
	  -w WHERE, --where WHERE
	                        : SQL where, e.g. "id>5 and name like falcon"
	  -o ORDERBY, --orderby ORDERBY
	                        [default=name]
	  -n NAME, --name NAME  : game name like this
	  -p PLATFORM, --platform PLATFORM
	                        : check lsplatform for list
	  -s SOURCE, --source SOURCE
	                        : check lsplugin for list
	  -r RUNNER, --runner RUNNER
	  --debug               Set logging level to DEBUG

..

install
---------


::

	$ python -m abandi.install --help
	usage: install.py [-h] [-d] [-u] [-r] [-n] [--debug] source id
	
	download and unpack game found in database
	
	positional arguments:
	  source              : ['gb64',..]
	  id                  : ['1',..]
	
	optional arguments:
	  -h, --help          show this help message and exit
	  -d, --downloadonly
	  -u, --unpackonly
	  -r, --removezip
	  -n, --nocache
	  --debug             Set logging level to DEBUG

..

run
---------


::

	$ python -m abandi.run --help
	usage: run.py [-h] [-r RUNNER] [-a] [--debug] source id
	
	start game using selected emulator
	
	positional arguments:
	  source                : ['gb64',..]
	  id                    : ['1',..]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -r RUNNER, --runner RUNNER
	                        : emulator ['auto','dosbox','scummvm',..]
	                        [default=auto]
	  -a, --auto-install
	  --debug               Set logging level to DEBUG

..

srun
---------


::

	$ python -m abandi.srun --help
	usage: srun.py [-h] [-c COLUMNS] [-w WHERE] [-o ORDERBY] [-n NAME]
	               [-p PLATFORM] [-s SOURCE] [-r RUNNER] [-a] [-i INDEX] [--debug]
	
	search and run
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -c COLUMNS, --columns COLUMNS
	                        [default=[source id platform] name]
	  -w WHERE, --where WHERE
	  -o ORDERBY, --orderby ORDERBY
	                        [default=name]
	  -n NAME, --name NAME
	  -p PLATFORM, --platform PLATFORM
	  -s SOURCE, --source SOURCE
	  -r RUNNER, --runner RUNNER
	                        [default=auto]
	  -a, --auto-install
	  -i INDEX, --index INDEX
	  --debug               Set logging level to DEBUG

..
..  [[[end]]]

