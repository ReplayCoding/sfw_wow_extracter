meta:
  id: sfx_wow
  file-extension: wow
  endian: le
seq:
  - id: magic
    contents: "SfxL"
  - id: num_entries
    type: u4
  - id: entries
    type: entry
    repeat: expr
    repeat-expr: entry_count
types:
  entry:
    seq:
      - id: name
        type: str
        size: 8
        encoding: ascii
      - id: length
        type: u4
      - id: offset
        type: u4
