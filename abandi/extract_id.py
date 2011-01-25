
def extract_id(id, limit):
    if id == 'all':
        return xrange(0, limit+1)
    ret = set()
    for x in str(id).split(','):
        if '-' in x:
            (start,stop)=x.split('-')
            ret.update(range(int(start),int(stop)+1))
        else:
            ret.add(int(x))
    ls =sorted(list(ret))
    ls =filter(lambda x:x<=limit,ls)
    return ls

def test_id():
    data = [
            ('all', 5)
            ,('1,4,3', 5)
            ,('2-5,1', 5)
            ,('1-10', 5)
            ,('3-5', 5)
            ,('1,3-5', 5)
            ,(1, 5)
            ]
    for (i, l) in data:
        print str(i) + ' ; ' + str(l) + "=>" + str(list(extract_id(i, l)))

if __name__ == '__main__':
    test_id()
