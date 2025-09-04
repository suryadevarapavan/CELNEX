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