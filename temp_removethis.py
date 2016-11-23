import StringIO
from eppy.iddcurrent import iddcurrent
import eppy.idf_helpers as idf_helpers
from eppy.modeleditor import IDF
from eppy.EPlusInterfaceFunctions.eplusdata import removecomment
from eppy.useful_scripts import loopdiagram
iddfile = '/Applications/EnergyPlus-8-3-0/Energy+.idd'

if IDF.getiddname() == None:
    IDF.setiddname(iddfile)

fname = "/Users/santoshphilip/Documents/coolshadow/github/weppy/examplefiles/5ZoneReturnFan.idf"

idf = IDF(fname)

from eppy.useful_scripts import loopdiagram1
edges = loopdiagram1.getedges(fname, iddfile)
print edges