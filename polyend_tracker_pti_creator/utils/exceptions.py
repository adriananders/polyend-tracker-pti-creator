# pylint: disable=unnecessary-pass
class CreatorSourceMissingException(Exception):
    """
    Indicates the source argument is missing.
    """

    pass


class CreatorDestinationInvalidException(Exception):
    """
    Indicates the source argument is missing.
    """

    pass


class CreatorNoSourceWavFilesException(Exception):
    """
    Indicates the source is either a non-wave file or path contains no wave files
    """

    pass


class CreatorModeInvalidException(Exception):
    """
    Indicates the mode argument is invalid value.
    Valid Values:
        normal
        merge
    """

    pass


class CreatorPlaybackInvalidException(Exception):
    """
    Indicates the playback argument is invalid value.
    Valid Values:
        one-shot
        forward-loop
        backward-loop
        ping-pong-loop
        slice
        beat-slice
        wavetable
        granular
        dynamic
    """

    pass


class CreatorTooManyMergeFilesException(Exception):
    """
    Indicates the number of files to merge (and slice) is greater than 48.
    """

    pass


class CreatorSampleTooLongException(Exception):
    """
    Indicates the sample is longer than 30 seconds, the maximum length supported by Polyend Tracker.
    """

    pass


class FfmpegNotInstalledException(Exception):
    """
    Indicates that ffmpeg is not installed.
    """

    pass
