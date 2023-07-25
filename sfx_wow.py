# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SfxWow(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x53\x66\x78\x4C":
            raise kaitaistruct.ValidationNotEqualError(b"\x53\x66\x78\x4C", self.magic, self._io, u"/seq/0")
        self.entry_count = self._io.read_u4le()
        self.entries = []
        for i in range(self.entry_count):
            self.entries.append(SfxWow.Entry(self._io, self, self._root))


    class Entry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes(8)).decode(u"ascii")
            self.length = self._io.read_u4le()
            self.offset = self._io.read_u4le()



