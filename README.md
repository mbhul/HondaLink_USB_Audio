# HondaLink_USB_Audio
HondaLink didn't like my USB music library, so I tried this

This script will squash a libary organized by artist and album into one that is organized by artist only (with filenames updated to include album name by acronym so that albums are still relatively easy to find). The purpose is to reduce the number of folders in the library, because HondaLink seems to not like too complex of a file system.

This script assumes the following file structure to begin with:
.\
.\Artist1\Album\song.mp3
or
.\Artist2\Album\CD1\song.mp3

The rule is that the top level folder from the root is the artist name.
Any folders contained therein are assumed to be albums. 

The result is a library that looks like this
.\
.\Artist1\A-song.mp3
.\Artist2\AC-song.mp3