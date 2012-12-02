from path import path
from abandi.iplugin import IPlugin


'''
def preRun(emu, game):
    # To properly play this game, original data files are needed.
    # You should copy the data files from the original TTD into the data
    # directory
    # (/usr/share/games/openttd/data). You should copy these files:
    # * trg1r.grf
    # * trgcr.grf
    # * trghr.grf
    # * trgir.grf
    # * trgtr.grf
    # * sample.cat

    # only linux
    (openttd_path, _) = cli.call("which openttd")
    #openttd_path = "/usr/games/openttd";

    openttd_gamedir = "/usr/share/games/openttd/";
    ttd_gamedir = path(game.dir);

    target_dir = ttd_gamedir / ".openttd";

    openttd_gamedir.copytree(target_dir);

    gmFiles = ttd_gamedir.files("*.gm");
    for x in gmFiles:
        x.copy(target_dir/ "gm");

    grfFiles = ttd_gamedir.files("*.grf");
    for x in grfFiles:
        x.copy(target_dir/ "data");

    grfFiles = ttd_gamedir.files("*.cat");
    for x in grfFiles:
        x.copy(target_dir/ "data");

    emulator_path = openttd_path.copy(target_dir);
    emulator_path.chmod(0755)


def run_game(game):
    command = 'openttd'
    call(command)

class Openttd(IPlugin):
    hook='runner'
#    info = dict(name=name,
#                extensions=extensions,
#                platforms=platforms)
    run_game=staticmethod(run_game)
'''