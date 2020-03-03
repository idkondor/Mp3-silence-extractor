# Mp3-silence-extractor
Extracts silence from mp3 files

Installation:
1. Download and Install "ffmpeg"
https://www.ffmpeg.org
2. Install "sox" 
https://at.projects.genivi.org/wiki/display/PROJ/Installation+of+SoX+on+different+Platforms
3. Install "libsox"
sudo apt-get install libsox-fmt-mp3

Usage:
  Run script from terminal for example:

python mp3_pause_splitter.py -in "/home/user/Desktop/mp3_pause_splitter/pyAudioAnalysis/pyAudioAnalysis/new files" -out "/home/user/Desktop/mp3_pause_splitter/pyAudioAnalysis/pyAudioAnalysis/new files" -p "1.5"
