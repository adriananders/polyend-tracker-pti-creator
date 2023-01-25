import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--source",
        help="source file or source file path - required."
    )
    parser.add_argument(
        "-d",
        "--destination",
        help="destination directory path - optional, defaults to source directory path."
    )
    parser.add_argument(
        "-m",
        "--mode",
        help="instrument creation mode - optional. Possible values are normal and merge. Defaults to normal."
    )
    parser.add_argument(
        "-p",
        "--playback",
        help="instrument playback setting - optional. Possible values are one-shot, "
             "forward-loop, backward-loop, ping-pong-loop, slice, beat-slice, wavetable, "
             "granular. Defaults to beat-slice in merge mode. "
             "Defaults to 'dynamic' in normal mode. 'dynamic' playback setting sets the "
             "playback to either forward-loop or one-shot depending on if a loop is found in the .wav file."
    )
    parser.add_argument(
        "-in",
        "--instrument-name",
        help="instrument name - optional. Must be less than 32 of alpha, numeric, space, +, -, or @ characters. "
             "Defaults to file name stripped of invalid characters then trimmed to 32 character length."
    )
    parser.add_argument(
        "-fn",
        "--file-name",
        help="destination file name - optional. Defaults to first file-name specified in destination parameter, "
             "then original source file name if a file name not specified in destination parameter."
    )
    return parser.parse_args()
