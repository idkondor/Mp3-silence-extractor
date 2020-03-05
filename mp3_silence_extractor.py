from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("-in", "--folderIn", dest="pathToMp3", help="Input folder path with files to extract silence!")
parser.add_argument("-p", "--pauseTime", dest="pauseTime", help="How many seconds has to be pause span between sounds!")
args = parser.parse_args()
pathToMp3 = args.pathToMp3
pauseTime = args.pauseTime
dirOrFilesLst = list()

for (dirPath, dirNames, audioNames) in os.walk(pathToMp3):
    dirOrFilesLst += [os.path.join(dirPath, file) for file in audioNames]

for path in dirOrFilesLst:
    audioFileName = path.split("/")[-1]
    silenceSlicedDir = path.replace(audioFileName, "") + "Silence_sliced"
    if ".mp3" in path:
        if not os.path.isdir(silenceSlicedDir):
            os.mkdir(silenceSlicedDir)

        os.system(f"sox '{path}' '{silenceSlicedDir}/s_{audioFileName}' silence 1 0.1 1% -1 "
                  f"{pauseTime} 1%")

    elif ".m4a" in path:
        if not os.path.isdir(silenceSlicedDir):
            os.mkdir(silenceSlicedDir)
        print(f"Converting {path} ......")
        os.system(f"ffmpeg -i '{path}' -f sox - | sox -p "
                  f"'{silenceSlicedDir}/s_{audioFileName.replace('m4a', 'mp3')}' silence 1 0.1 1% -1 "
                  f"{pauseTime} 1%")
