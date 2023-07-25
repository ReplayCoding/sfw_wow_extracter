from sfx_wow import SfxWow
from kaitaistruct import KaitaiStream
import wave
import sys

f = open(sys.argv[1], "rb")
stream = KaitaiStream(f)

sfx = SfxWow(stream)
for entry in sfx.entries:
    f.seek(entry.offset, 0)
    raw_data = f.read(entry.length)

    fixed_name = entry.name.replace("\0", "")
    with wave.open(f"{fixed_name}.wav", "wb") as wavfile:
        wavfile.setparams((1, 2, 44100, 0, "NONE", "NONE"))
        wavfile.writeframes(raw_data)

    print(entry.name, entry.length, entry.offset)
