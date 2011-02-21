from abandi.runner import Runner
import unittest

game_list = '''
atlantis             Indiana Jones and the Fate of Atlantis
indy3                Indiana Jones and the Last Crusade
loom                 Loom
maniac               Maniac Mansion
monkey               The Secret of Monkey Island
monkey2              Monkey Island 2: LeChuck's Revenge
pass                 Passport to Adventure
samnmax              Sam & Max Hit the Road
tentacle             Day of the Tentacle
zak                  Zak McKracken and the Alien Mindbenders
ft                   Full Throttle
dig                  The Dig
comi                 The Curse of Monkey Island
activity             Putt-Putt & Fatty Bear's Activity Pack
brstorm              Bear Stormin'
fbear                Fatty Bear's Birthday Surprise
fbpack               Fatty Bear's Fun Pack
funpack              Putt-Putt's Fun Pack
puttmoon             Putt-Putt Goes to the Moon
puttputt             Putt-Putt Joins the Parade
arttime              Blue's Art Time Activities
baseball2001         Backyard Baseball 2001
Baseball2003         Backyard Baseball 2003
basketball           Backyard Basketball
football2002         Backyard Football 2002
freddicove           Freddi Fish 5: The Case of the Creature of Coral Cove
moonbase             Moonbase Commander
pjgames              Pajama Sam: Games to Play on Any Day
readtime             Blue's Reading Time Activities
Soccer2004           Backyard Soccer 2004
SoccerMLS            Backyard Soccer MLS Edition
spyozon              SPY Fox 3: Operation Ozone
airport              Let's Explore the Airport with Buzzy
balloon              Putt-Putt and Pep's Balloon-O-Rama
baseball             Backyard Baseball
Blues123Time         Blue's 123 Time Activities
BluesABCTime         Blue's ABC Time Activities
BluesBirthday        Blue's Birthday Adventure
BluesTreasureHunt    Blue's Treasure Hunt
catalog              Humongous Interactive Catalog
chase                SPY Fox in Cheese Chase
dog                  Putt-Putt and Pep's Dog on a Stick
farm                 Let's Explore the Farm with Buzzy
football             Backyard Football
freddi               Freddi Fish 1: The Case of the Missing Kelp Seeds
freddi2              Freddi Fish 2: The Case of the Haunted Schoolhouse
freddi3              Freddi Fish 3: The Case of the Stolen Conch Shell
freddi4              Freddi Fish 4: The Case of the Hogfish Rustlers of Briny Gulch
FreddisFunShop       Freddi Fish's One-Stop Fun Shop
jungle               Let's Explore the Jungle with Buzzy
lost                 Pajama Sam's Lost & Found
maze                 Freddi Fish and Luther's Maze Madness
mustard              SPY Fox in Hold the Mustard
pajama               Pajama Sam 1: No Need to Hide When It's Dark Outside
pajama2              Pajama Sam 2: Thunder and Lightning Aren't so Frightening
pajama3              Pajama Sam 3: You Are What You Eat From Your Head to Your Feet
puttcircus           Putt-Putt Joins the Circus
puttrace             Putt-Putt Enters the Race
PuttsFunShop         Putt-Putt's One-Stop Fun Shop
putttime             Putt-Putt Travels Through Time
puttzoo              Putt-Putt Saves the Zoo
SamsFunShop          Pajama Sam's One-Stop Fun Shop
soccer               Backyard Soccer
socks                Pajama Sam's Sock Works
spyfox               SPY Fox 1: Dry Cereal
spyfox2              SPY Fox 2: Some Assembly Required
thinker1             Big Thinkers First Grade
thinkerk             Big Thinkers Kindergarten
water                Freddi Fish and Luther's Water Worries
agi                  Sierra AGI game
pn                   Personal Nightmare
elvira1              Elvira - Mistress of the Dark
elvira2              Elvira II - The Jaws of Cerberus
waxworks             Waxworks
simon1               Simon the Sorcerer 1
simon2               Simon the Sorcerer 2
feeble               The Feeble Files
dimp                 Demon in my Pocket
jumble               Jumble
puzzle               NoPatience
swampy               Swampy Adventures
cine                 Cinematique evo.1 engine game
cruise               Cinematique evo.2 engine game
draci                Draci Historie
drascula             Drascula: The Vampire Strikes Back
gob                  Gob engine game
groovie              Groovie engine game
kyra1                The Legend of Kyrandia
kyra2                The Legend of Kyrandia: The Hand of Fate
kyra3                The Legend of Kyrandia: Malcolm's Revenge
lure                 Lure of the Temptress
made                 MADE engine game
parallaction         Parallaction engine game
nippon               Nippon Safes Inc.
bra                  The Big Red Adventure
queen                Flight of the Amazon Queen
saga                 SAGA Engine game
sky                  Beneath a Steel Sky
sword1               Broken Sword: The Shadow of the Templars
sword1demo           Broken Sword: The Shadow of the Templars (Demo)
sword1mac            Broken Sword: The Shadow of the Templars (Mac)
sword1macdemo        Broken Sword: The Shadow of the Templars (Mac demo)
sword1psx            Broken Sword: The Shadow of the Templars (PlayStation)
sword1psxdemo        Broken Sword: The Shadow of the Templars (PlayStation demo)
sword2               Broken Sword II: The Smoking Mirror
sword2alt            Broken Sword II: The Smoking Mirror (alt)
sword2psx            Broken Sword II: The Smoking Mirror (PlayStation)
sword2psxdemo        Broken Sword II: The Smoking Mirror (PlayStation/Demo)
sword2demo           Broken Sword II: The Smoking Mirror (Demo)
teenagent            Teen Agent
tinsel               Tinsel engine game
touche               Touche: The Adventures of the Fifth Musketeer
tucker               Bud Tucker in Double Trouble
'''


yes = '''
Beneath a Steel Sky
Beneath a steel sky
Day of the Tentacle
Flight of the Amazon Queen
Gobliiins|gob
Indiana Jones and the Fate of Atlantis
Indiana Jones and the Last Crusade
Indiana Jones and the Last Crusade
Legend of Kyrandia 1, The|kyra1
Legend of Kyrandia 2 - Hand of Fate, The|kyra2
Legend of Kyrandia 3 - Malcolms Revenge, The|kyra3
Legend of Kyrandia, The
Lure of the Temptress
Maniac Mansion
Sam and Max Hit the Road
Secret of Monkey Island
Teen Agent
Waxworks
Elvira - Mistress of the Dark
Big Red Adventure, The
Nippon Safes, Inc.
Future Wars|cine
Future Wars - Time Travellers|cine
'''.strip().splitlines()
yes=dict([(x.split('|')+[''])[0:2] for x in yes])


no = '''
2010
Dig Dug
Dig It
Digger
Diggits
Digital Tangram
F1
Flying Digger, The
Flying Digits
Ghosts & Goblins
Ghosts N Goblins
Ghosts'n Goblins
Ghosts'n Goblins Construction Set
Ghosts'n Goblins II
Jumble [Preview]
Mr. Dig
PP Digger
Powers of Gloom
Prodigy, The
Sexy Ghosts'n Goblins
'''.strip().splitlines()
#One on One Backyard Basketball


class dummy:
    pass

class TestScummvm(unittest.TestCase):

    def setUp(self):
        #self.seq = range(10)
        pass

    def test_no(self):
        r=Runner('scummvm')
        for x in no:
            #print x
            g = dummy()
            g.name = x
            #r.scummvm_id(g)
            self.assertRaises(AssertionError, r.scummvm_id, g)
    
    def test_yes(self):
        r=Runner('scummvm')
        for x in yes.keys():
            #print x
            g = dummy()
            g.name = x
            id=r.scummvm_id(g)
            if yes.get(x):
                self.assertEquals(id, yes.get(x))
