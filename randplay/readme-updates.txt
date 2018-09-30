will add sql datebase support for played playlists so played playlists can be easily reviewed as to if that particular playlist has been played, or not, using the sha512 checksum of the recordered playlists.

the program will review the playlist.txt.tmp and add the songs to a table identified by the sha512sum for organization.

the program will be a function for randplay.player that if the playlist exists in the database, then another playlist will be generated.

a gui will later be added that will directly review the database for playlist and allow playing the playlists recorded back, or play another random playlist and have it recorded into the database.
