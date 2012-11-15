from . import buchheim
from . import knuth
from . import reingold_actual
from . import reingold_addmod
from . import reingold_naive
from . import reingold_thread
from . import walker
from . import ws1
from . import ws2

buchheim = buchheim.buchheim
knuth = knuth.layout
reingold_actual = reingold_actual.layout
reingold_addmod = reingold_addmod.layout
reingold_naive  = reingold_naive.reingold_tilford
reingold_thread = reingold_thread.reingold_tilford
walker = walker.walker
ws1 = ws1.layout
ws2 = ws2.layout

layout = buchheim
