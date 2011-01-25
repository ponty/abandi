

# id should be the last! it's integer in db.py
fields='''
name
source
platform
gameFileURL
dir
zip
releaseYear
genre
programmer
language
musician
publisher
homePageURL
musicFileURL
screenshotUrls
id
'''.strip().split()

class Game:
    def __init__(self):
        for x in fields:
            self.__dict__[x] = None
        #=======================================================================
        # self.id= -1
        # self.source= None
        # self.publisher         = None
        # self.gameFileURL       = None
        # self.name              = None
        # self.language          = None
        # self.musician          = None
        # self.musicFileURL      = None
        # self.releaseYear       = None
        # self.genre            = None
        # self.programmer        = None
        # self.homePageURL= None
        # self.platform= None
        # self.dir= None
        # self.zip= None
        # self.screenshotUrls= None
        #=======================================================================

#fields = Game().__dict__.keys()
#priolist=['id','source']
#fields.sort(key=lambda x: priolist.index(x) if x in priolist else 2)

def print_game(game):
    if not game:
        print game
        return
    gd = game.__dict__
    for k in fields:
        v=gd[k]
        s = k + ':' + ' ' * (20 - len(k))
        if type(v) == list:
            s += (','.join(v))
        #elif k == 'source':
        #    s += ','.join(map((lambda (x, y):str(x) + ':' + str(y)), v.items()))
        else:
            s += str(v)
        print s

def print_games(games, columns='all'):
    if columns=='all':
        columns=fields

    for g in games:
        gd = g.__dict__
        line = u'[{source} {id} {platform}] {name}'.format(**gd)
#        for f in columns:
#            line = line  + unicode(gd[f])+ ' '
        print line
