# pylint: disable=consider-using-generator
import struct
from copy import deepcopy
from lazy_property import LazyProperty
from polyend_tracker_pti_creator.utils.pti.constants import PTI_HEADER_DEFINITION


class Header:
    def __init__(self, settings):
        self.definition = deepcopy(PTI_HEADER_DEFINITION)
        for key, value in settings.items():
            if isinstance(value, str):
                value = self.encode_string(value)
            self.definition[key]['value'] = value

    @LazyProperty
    def format(self) -> str:
        return '<' + ''.join([value['type'] for value in self.definition.values()])

    @LazyProperty
    def data(self) -> tuple:
        return tuple([value['value'] for value in self.definition.values()])

    @LazyProperty
    def data_bytes(self) -> bytearray:
        return bytearray(struct.pack(self.format, * self.data))

    @staticmethod
    def encode_string(string):
        ascii_string = string.encode('ASCII')
        pad_length = 32 - len(ascii_string)
        pad = b''.join([b'\x00' for x in range(pad_length)])
        return ascii_string + pad
