from .. import regex_patterns as regex_patterns
from .standardMzml import StandardMzml as StandardMzml
from _typeshed import Incomplete

class BytesMzml(StandardMzml):
    binary: Incomplete
    file_handler: Incomplete
    offset_dict: Incomplete
    spec_open: Incomplete
    spec_close: Incomplete
    def __init__(self, binary, encoding, build_index_from_scratch: bool = False) -> None: ...
    def get_binary_file_handler(self): ...
    def get_file_handler(self, encoding): ...
