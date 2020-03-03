from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("-in", "--folderIn", dest="pathToMp3", help="Input folder path with files to extract silence!")
parser.add_argument("-out", "--folderOut", dest="convertedMp3Path", help="Input folder path where to put converted "
                                                                         "files!")
parser.add_argument("-p", "--pauseTime", dest="pauseTime", help="How many seconds has to be pause span between sounds!")
args = parser.parse_args()
pathToMp3 = args.pathToMp3
convertedMp3Path = args.convertedMp3Path
pauseTime = args.pauseTime


for mp3Track in os.listdir(pathToMp3):
    print(f"Converting {mp3Track} ......")
    mp3TrackPath = os.path.join(pathToMp3, mp3Track)
    if "m4a" in mp3Track:
        os.system(f"ffmpeg -i '{mp3TrackPath}' -f sox - | sox -p "
                  f"'{convertedMp3Path}/s_{mp3Track.replace('m4a', 'mp3')}' silence 1 0.1 1% -1 {pauseTime} 1%")
    else:
        os.system(f"sox '{mp3TrackPath}' '{convertedMp3Path}/s_{mp3Track}' silence 1 0.1 1% -1 {pauseTime} 1%")
