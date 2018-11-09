import os, fnmatch
import ctypes
import shutil
import eyed3

def followPath(root, folder, recursiveName):
    pathstr = root + "\\" + folder
    dirs = [d for d in os.listdir(pathstr) if os.path.isdir(os.path.join(folder, d))]
    for dir in dirs:
        followPath(root, pathstr + "\\" + dir, folder + "_" + dir)
    
    abvFName = ""
    changemade = False
    filecount = 0
    
    #first get the abbreviated album name to use as a prefix for sorting purposes
    words = recursiveName.split()
    for a_word in words:
        abvFName += a_word[0].upper()
    
    listOfFiles = os.listdir(pathstr)
    for entry in listOfFiles: 
        if fnmatch.fnmatch(entry, pattern_mp3) or fnmatch.fnmatch(entry, pattern_wma):
            try:
                filecount += 1
                audiofile = eyed3.load(pathstr + "\\" + entry)
                
                #fill in any missing attributes
                if audiofile.tag.artist is None:
                    audiofile.tag.artist = unicode(artist, "utf-8")
                    changemade = True
                if audiofile.tag.album is None:
                    audiofile.tag.album = unicode(recursiveName, "utf-8")
                    changemade = True
                if audiofile.tag.title is None:
                    audiofile.tag.title = unicode(os.path.splitext(entry)[0], "utf-8")
                    changemade = True
                    
                #save if a change was made
                if changemade is True:
                    audiofile.tag.save()
                    
            except:
                file.write(pathstr + "\\" + entry + "\r\n")
            
            #now move the file
            shutil.move(pathstr + "\\" + entry, root + "\\" + abvFName + " - " + entry)
                
    #Now kill the subfolder
    #os.rmdir(pathstr)
    if filecount > 0:
        shutil.rmtree(pathstr)
    
    return

def is_hidden(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result
    
    
    
root_dir = "E:\\"
artist_dir = ""
artist = ""
album = ""
song = ""
count = 0

pattern_mp3 = "*.mp3" 
pattern_wma = "*.wma"

artists = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

file = open("FileAccessFailures.txt","w") 

for artist in artists:
    #Build the full path for the artist
    artist_dir = root_dir + artist

    #ignor hidden folders
    if is_hidden(artist_dir) is False:
        print("Processing Artist: ", artist)
        albums = [d for d in os.listdir(artist_dir) if os.path.isdir(os.path.join(artist_dir, d))]
        #temp limit for debug
        if count <= 1:
            #count += 1
            for album in albums:
                followPath(artist_dir, album, album)
                #print(album)

file.close() 
os.system("pause")

