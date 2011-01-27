

# id should be the last! it's integer in db.py
fields_key='''
source
id
'''.strip().split()

fields_parse='''
name
platform
game_file_url
release_year
genre
programmer
language
musician
publisher
home_url
music_file_url
screenshot_url_list
'''.strip().split()

fields_install='''
zip
dir
'''.strip().split()

fields=fields_key+fields_parse+fields_install

class Game:
    def __init__(self):
        for x in fields:
            self.__dict__[x] = None

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

def print_games(games, col_format='name'):
    #if format=='all':
    #    columns=fields

    ls=sorted(fields,key=len, reverse=1)
    #print ls
    for x in ls:
        if x in col_format:
            #columns.append(x)
            col_format=col_format.replace(x, '{'+x+'}')
    #print col_format
    
    for g in games:
        gd = g.__dict__
#        line = u'[{source} {id} {platform}] {name}'.format(**gd)
        line = unicode(col_format).format(**gd)

#        for f in columns:
#            line = line  + unicode(gd[f])+ ' '
        print line
