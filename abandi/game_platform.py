import logging


platform_dict = dict(
                   megadrive=['SEGA Genesis', 'Mega Drive'],
                   mastersystem=['master system'],
                   cplus4=['Commodore +4'],
                   c64=['Commodore 64'],
                   c128=['Commodore 128'],
                   msx=['Sony MSX', 'Sony MSX 2'],
                   gb=['Nintendo GameBoy'],
                   win=['Win32'],
                   atari2k6=['Atari 2600'],
                   dos=['ms-dos'],
                   nes=['Nintendo Entertainment System'],
                   snes=['Super Nintendo Entertainment System'],
                   linux=[],
                   amiga=[],
                   )

PLATFORMS = platform_dict.keys()

def id(name):
    name = name.lower().strip()
    id = None
    if name in PLATFORMS:
        id = name
    for (k, ls) in platform_dict.items():
        for s in ls :
            if s.lower() in name:
                id = k
                break
    if id=='nes' and 'super' in name:
        id='snes'
    if not id:
        print 'error: unknown platform:' + name
        id = name
    else:
        assert id in PLATFORMS
    return id
