# polyend-tracker-pti-creator
Python 3 [Polyend Tracker](https://polyend.com/tracker/) .pti instrument creator.

Initial purpose of the utility python CLI app is threefold.
- Create .pti forward-looping instruments with clean loop points that are encoded in a wave file sample. Currently Polyend Tracker doesn't read these loop points and thus makes clean looping of instrument samples rather challenging.
- Create .pti beat-slicer/slicer instruments from a series of individual wave-files to create drum-kits and perfect conversions of previously sliced loops (REX for example) into .pti loops.
- Batch convert wave files into individual pti instruments. For individuals making sample packs or libraries for distribution, this may save time over individually creating the .pti files in Polyend Tracker directly.

Special thanks to [@jaap3](https://github.com/jaap3) for his excellent .pti file format [documentation](https://github.com/jaap3/pti-file-format).


## Installation
1. Install dependencies

    ### Python
    #### MacOS
    Follow Instructions to install [Homebrew](https://brew.sh/).
    ```brew update && brew install python```
    #### Windows
    1. Download Python installer from [python.org](https://www.python.org/).
    2. Install. Be sure to select "Add Python to path" during installation as well as disable path length limit.
   
    ### ffmpeg
    #### MacOS
    ```brew install ffmpeg```
    #### Windows
    1. Download the latest Windows binary from [ffmpeg.org](http://ffmpeg.org/).
    2. Unzip and move contents of bin to "C:\Program Files\ffmpeg".
    3. Add ffmpeg to path.
        1. Open Start Menu.
        2. Type "Edit Environment Variables".
        3. Click on "Edit Environment Variables For Your Account".
        4. In Edit Environment Variables, you will see two boxes. In system variables box find and select "path" variables.
        5. Click "Edit".
        6. In window pop up, click "New".
        7. Type "C:\Program Files\ffmpeg", then click OK twice to save your changes.
    

2. Install pet-pti-creator command
    1. Clone or download polyend-tracker-pti-creator package from GitHub. Unzip if downloaded.
    2. In Terminal (MacOS) or Command Prompt (Windows) navigate to the polyend-tracker-pti-creator package folder.
    3. Run ```python setup.py install```. This will install pet-pti-creator to your path and be accessible as a terminal command.
    4. Restart Terminal or Command Prompt before first usage.
    
## Usage
### Basic Usage
```pet-pti-creator --source path/of/wave/file```

### Specify Destination
```pet-pti-creator --source path/of/wave/file --destination path/of/destination/directory```

### Batch processing
```pet-pti-creator --source path/of/wave/file/directory```

### Merge multiple files to single beat slice instrument 
```pet-pti-creator --source path/of/wave/file/directory --mode merge```

### Help
```pet-pti-creator --help```

## Notes

- Currently, only .WAV is supported as a source file. This is because of robust [documentation](https://sites.google.com/site/musicgapi/technical-documents/wav-file-format#fmt) of the format for extracting loop points out of the file. AIFF and CAF are feasible to support, but not in initial version.

- Currently, loop points for loop-playback modes are pulled by parsing the wave file itself. If you're unsure if your wave file has loop-points, download the free [Endless WAV](https://www.bjoernbojahr.de/endlesswav.html) editor. In addition to being able to view file loop points, it can also algorithmically create loop points for files without them originally.

- To convert a REX file into a sliced .pti instrument, use an application that can export REX loops as individual wave file slices then use 'merge' mode to keep those slice points exactly the same in the resulting .pti file. Easiest way to convert REX/RX2 files to individual wave slices is use [Recycle](https://www.reasonstudios.com/recycle).

- Another use for the merge mode is to collect up to 48 individual drum hits into a drumkit.

- As mentioned in the MIT license, this software is provided as-is without warranty. Although care is taken to prevent damage to the original audio files, please back up originals to a separate location prior to use. I'm not aware of an straight-forward freeware solution at this time.