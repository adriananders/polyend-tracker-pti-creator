# pylint: disable=too-many-instance-attributes, too-many-arguments, unused-variable
from __future__ import annotations
from struct import unpack, pack
from typing import BinaryIO, List, Dict
from wave_chunk_parser.exceptions import (
    InvalidHeaderException,
)
from wave_chunk_parser.chunks import Chunk, RiffChunk, FormatChunk, DataChunk, CartChunk
from wave_chunk_parser.utils import seek_and_read


class SampleChunk(Chunk):
    """
    The sample chunk defines how the audio is played back by a sampler.
    """

    __manufacturer: int
    __product: int
    __sample_period: int
    __midi_unity_note: int
    __midi_pitch_fraction: int
    __smpte_format: int
    __smpte_offset: int
    __number_of_sample_loops: int
    __sampler_data: int
    __first_cue_point_id: int

    LENGTH_CHUNK = 68
    LENGTH_STANDARD_SIZE = 60
    HEADER_SAMPLE = b"smpl"

    def __init__(
        self,
        manufacturer: int,
        product: int,
        sample_period: int,
        midi_unity_note: int,
        midi_pitch_fraction: int,
        smpte_format: int,
        smpte_offset: int,
        number_of_sample_loops: int,
        sampler_data: int,
        first_cue_point_id: int,
        first_loop_type: int,
        first_loop_start: int,
        first_loop_end: int,
        first_loop_fraction: int,
        first_loop_play_count: int,
    ) -> None:
        """
        Creates a new instance of the sample block.
        https://sites.google.com/site/musicgapi/technical-documents/wav-file-format#fmt
        TODO: extract more than first cue point.
        Args:
            manufacturer (int): MIDI Manufacturer's Association Manufacturer code.
            product (int): MIDI model ID.
            sample_period (int): Duration of time that passes during the playback of one sample in nanoseconds.
            midi_unity_note (int): Musical note at which the sample will be played.
            midi_pitch_fraction (int): Fraction of a semitone up from the specified MIDI unity note field.
            smpte_format (int): SMPTE time format used in the following SMPTE Offset field.
            smpte_offset (int): SMPTE time offset to be used.
            number_of_sample_loops (int): Number of sample loops.
            sampler_data (int): Number of bytes that will follow this chunk.
            first_cue_point_id (int): Unique ID that corresponds to one of the defined cue points.
            first_loop_type (int): Defines how the waveform samples will be looped.
            first_loop_start (int): Byte offset into the waveform data of the first sample to be played in the loop.
            first_loop_end (int): Byte offset into the waveform data of the last sample to be played in the loop.
            first_loop_fraction (int): Fraction of a sample at which to loop.
            first_loop_play_count (int): Number of times to play the loop.
        """

        self.__manufacturer = manufacturer
        self.__product = product
        self.__sample_period = sample_period
        self.__midi_unity_note = midi_unity_note
        self.__midi_pitch_fraction = midi_pitch_fraction
        self.__smpte_format = smpte_format
        self.__smpte_offset = smpte_offset
        self.__number_of_sample_loops = number_of_sample_loops
        self.__sampler_data = sampler_data
        self.__first_cue_point_id = first_cue_point_id
        self.__first_loop_type = first_loop_type
        self.__first_loop_start = first_loop_start
        self.__first_loop_end = first_loop_end
        self.__first_loop_fraction = first_loop_fraction
        self.__first_loop_play_count = first_loop_play_count

    @classmethod
    def from_file(cls, file_handle: BinaryIO, offset: int) -> SampleChunk:

        # Sanity check

        (header_str, length) = cls.read_header(file_handle, offset)

        if not header_str == cls.HEADER_SAMPLE:
            raise InvalidHeaderException("Sample chunk must start with smpl")

        # Read from the chunk

        (
            manufacturer,
            product,
            sample_period,
            midi_unity_note,
            midi_pitch_fraction,
            smpte_format,
            smpte_offset,
            number_of_sample_loops,
            sampler_data,
            first_cue_point_id,
            first_loop_type,
            first_loop_start,
            first_loop_end,
            first_loop_fraction,
            first_loop_play_count,
        ) = unpack(
            "<IIIIIIIIIIIIIII",
            seek_and_read(
                file_handle,
                offset + cls.OFFSET_CHUNK_CONTENT,
                cls.LENGTH_CHUNK - cls.OFFSET_CHUNK_CONTENT,
            ),
        )

        # Generate our object

        return SampleChunk(
            manufacturer,
            product,
            sample_period,
            midi_unity_note,
            midi_pitch_fraction,
            smpte_format,
            smpte_offset,
            number_of_sample_loops,
            sampler_data,
            first_cue_point_id,
            first_loop_type,
            first_loop_start,
            first_loop_end,
            first_loop_fraction,
            first_loop_play_count,
        )

    @property
    def manufacturer(self) -> int:
        """
        MIDI Manufacturer's Association Manufacturer code.
        """
        return self.__manufacturer

    @property
    def product(self) -> int:
        """
        MIDI model ID.
        """
        return self.__product

    @property
    def sample_period(self) -> int:
        """
        Duration of time that passes during the playback of one sample in nanoseconds.
        """
        return self.__sample_period

    @property
    def midi_unity_note(self) -> int:
        """
        Musical note at which the sample will be played.
        """
        return self.__midi_unity_note

    @property
    def midi_pitch_fraction(self) -> int:
        """
        Fraction of a semitone up from the specified MIDI unity note field.
        """
        return self.__midi_pitch_fraction

    @property
    def smpte_format(self) -> int:
        """
        SMPTE time format used in the following SMPTE Offset field.
        """
        return self.__smpte_format

    @property
    def smpte_offset(self) -> int:
        """
        SMPTE time offset to be used.
        """
        return self.__smpte_offset

    @property
    def number_of_sample_loops(self) -> int:
        """
        Number of sample loops.
        """
        return self.__number_of_sample_loops

    @property
    def sampler_data(self) -> int:
        """
        Number of bytes that will follow this chunk.
        """
        return self.__sampler_data

    @property
    def first_cue_point_id(self) -> int:
        """
        Unique ID that corresponds to one of the defined cue points.
        """
        return self.__first_cue_point_id

    @property
    def first_loop_type(self) -> int:
        """
        Defines how the waveform samples will be looped.
        """
        return self.__first_loop_type

    @property
    def first_loop_start(self) -> int:
        """
        Byte offset into the waveform data of the first sample to be played in the loop.
        """
        return self.__first_loop_start

    @property
    def first_loop_end(self) -> int:
        """
        Byte offset into the waveform data of the last sample to be played in the loop.
        """
        return self.__first_loop_end

    @property
    def first_loop_fraction(self) -> int:
        """
        Fraction of a sample at which to loop.
        """
        return self.__first_loop_fraction

    @property
    def first_loop_play_count(self) -> int:
        """
        Number of times to play the loop.
        """
        return self.__first_loop_play_count

    @property
    def get_name(self) -> str:
        return self.HEADER_SAMPLE

    def to_bytes(self) -> List[bytes]:

        # Build up our chunk

        return pack(
            "<4sIIIIIIIIIIIIIIII",
            self.HEADER_SAMPLE,
            self.LENGTH_STANDARD_SIZE,
            self.manufacturer,
            self.product,
            self.sample_period,
            self.midi_unity_note,
            self.midi_pitch_fraction,
            self.smpte_format,
            self.smpte_offset,
            self.number_of_sample_loops,
            self.sampler_data,
            self.first_cue_point_id,
            self.first_loop_type,
            self.first_loop_start,
            self.first_loop_end,
            self.first_loop_fraction,
            self.first_loop_play_count,
        )


class RiffChunkExtended(RiffChunk):
    CHUNK_SAMPLE = b"smpl"

    RiffChunk.CHUNK_HEADER_MAP = {
        RiffChunk.CHUNK_FORMAT: FormatChunk,
        RiffChunk.CHUNK_DATA: DataChunk,
        RiffChunk.CHUNK_CART: CartChunk,
        CHUNK_SAMPLE: SampleChunk,
    }

    def __init__(self, sub_chunks: Dict[str, Chunk]) -> None:
        super().__init__(sub_chunks)
        self.__sub_chunks = sub_chunks

    @property
    def sub_chunks(self) -> Dict[str, Chunk]:
        return self.__sub_chunks

    @classmethod
    def from_file(cls, file_handle: BinaryIO, offset: int = 0) -> Chunk:
        return RiffChunk.from_file(file_handle, offset)

    def to_bytes(self) -> List[bytes]:
        data = RiffChunk(self.__sub_chunks).to_bytes()
        if self.CHUNK_SAMPLE in self.sub_chunks:
            data += self.sub_chunks.get(self.CHUNK_SAMPLE).to_bytes()
        header_length = 8
        replacement_header = pack("<4sI", self.HEADER_RIFF, len(data) - header_length)
        return replacement_header + data[header_length:]
