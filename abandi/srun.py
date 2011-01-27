from abandi.run import run_game
from abandi.search import search
import cli4func
import game
import logging


def srun(columns='[source id platform] name', where='', orderby='name', name='', platform='', source='', 
         runner='auto', auto_install=False,
         index=0):
    ''' search and run'''
    
    index=int(index)
    games=search(columns, where, orderby, name, platform, source)
    if len(games)>index and index>=0:
        g=games[index]
        #print 'starting game:'+g.name
        run_game(g.source, g.id,  auto_install=auto_install, runner=runner)
    else:
        print 'index out of bounds!'
cli4func.main(srun)
