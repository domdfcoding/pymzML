from _typeshed import Incomplete
from pymzml.file_classes import bytesMzml as bytesMzml, indexedGzip as indexedGzip, standardGzip as standardGzip, standardMzml as standardMzml
from pymzml.utils import GSGR as GSGR

class FileInterface:
    build_index_from_scratch: Incomplete
    encoding: Incomplete
    index_regex: Incomplete
    file_handler: Incomplete
    offset_dict: Incomplete
    def __init__(self, path, encoding, build_index_from_scratch: bool = False, index_regex: Incomplete | None = None) -> None: ...
    def close(self) -> None: ...
    def read(self, size: int = -1): ...
    def __getitem__(self, identifier): ...
