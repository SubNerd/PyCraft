from terrain.block import *
from core.renderer import *
from core.fileutils import *
from core.util import *
from constants import *


class Chunk:
    def __init__(self, position, parent):
        self.position = (position[0] * CHUNK_SIZE, position[1] * CHUNK_SIZE)
        self.parent = parent
        self.block_data = dict(self.parent.block_data)
        self.blocks = self.block_data["blocks"]
        self._blocks = {}
        self._generated = False
        self.listener = ListenerBase('cache/generated/')
        self.writer   = WriterBase('cache/requested/')
        self.vbo_requester = WriterBase('cache/vbo_request/')

    def block_exists(self, position):
        position = encode_position(position)
        return position in self._blocks

    def generate(self):
        blocktypes = get_block_types(self.blocks)
        self.writer.write(f"chunk{encode_position(self.position)}", {
            "position": encode_position(self.position),
            "seed": self.parent.seed,
            "blocktypes": blocktypes
        })

        # data = self.listener.wait_read(f"chunk{encode_position(self.position)}")
        # if data is not None:
        #     data = data["blocks"]
        #     self._blocks = data

        #     self.vbo_requester.write(f"chunk{encode_position(self.position)}", {
        #         "blocks": data,
        #         "position": encode_position(self.position),
        #         "block_types": blocktypes
        #     })
        self._generated = True
