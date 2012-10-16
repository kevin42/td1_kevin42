"""Code pour compter le nombre de mots d'une page web"""

import pdb
import httplib
import sys
from datetime import datetime

SAVE = sys.stdout
LOGFILE = open('compter.log', 'w')
sys.stdout = LOGFILE

#permet de passer l'adresse du site en parametre
#au lieu de la programmer en dur
ADRESS = sys.argv[1]
print datetime.now().strftime("[%d/%m/%y %H:%M]"), "Adresse indiquee :", ADRESS

#pdb.set_trace()
#pdb permet d'executer pas a pas notre application 
#(c=continue, n=ligne suivante, s=entrer dans fonction)

CONN = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128)
CONN.request("GET", ADRESS)
#si on veut on peut mettre directement
#notre adresse a la place de adress

REPONSE = CONN.getresponse()
PAGE = REPONSE.read()
print "le nombre de mots est :", PAGE.count(" ")

sys.stdout = SAVE
LOGFILE.close()
print file('compter.log').read()
CONN.close()
