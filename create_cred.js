show dbs;

use celnex;

db.createCollection('cred')

db.cred.insertMany([{
    pid:641326
                   },
{
    pid:939496
}])

db.cred.find().pretty()

db.createCollection('deck')

db.deck.insertMany([{
    char:'A.V',
    deck:['STAR_CANON','BLAST_EM'],
    HP:50
},
{
    char:'MARIA',
    deck:['BLOOD_BATH','CURSE'],
    HP:65
},
{
    char:'Yurei Shogun',
    deck:['SPIRIT_DRAIN','CURSED_FLAME','PHASE_SHIFT'],
    HP:70
}])
