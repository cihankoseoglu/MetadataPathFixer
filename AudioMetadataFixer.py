from tinytag import TinyTag
from tinytag import TinyTagException
import os
import errno
import shutil
from pathlib import Path

def main():

    ## path to the audio files
    path = Path("/Volumes/Data Rescue Storage/MacDisk/Recovered Files/Scan 3/Reconstructed Files/Audio/MP3")

    count = 200
    for root, dirs, filenames in os.walk(path):
        for f in filenames:
            f = f.replace("/", "_")

            if(f[0] is not "."):
                print(f)
                try:
                    tag = TinyTag.get("{}/{}".format(path, f))
                    #print('Track Name: {}'.format(tag.title))
                    #print(tag.album)
                    #print(tag.artist)
                except IndexError as exception:
                    raise

                if tag.album is not "" and tag.album is not " " and tag.album is not None \
                        and tag.artist is not None and tag.artist is not "" and tag.artist is not " ":
                    path_artist = path / tag.artist
                    create_directory(path_artist)
                    path_album = path_artist / tag.album
                    create_directory(path_album)
                    file_to_copy = "{}/{}".format(path, f)

                    #file_to_copy = path / f
                    shutil.move(file_to_copy, path_album)



            #print('The name of the song is {}'.format(tag.title))
            #print('The album of the song is {}'.format(tag.album))
            #print('The genre of the song is {}'.format(tag.genre))


def create_directory(dirname):
    try:
        os.makedirs(dirname)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise




if __name__ == '__main__':
    main()