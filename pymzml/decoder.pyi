import pynumpress

MSDecoder = pynumpress

class Decoder:
    def __init__(self, nb_workers: int = 2) -> None: ...
    def pool_decode(self, data, callback) -> None: ...
