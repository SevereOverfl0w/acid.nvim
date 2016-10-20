from acid.handlers import BaseHandler
from acid.nvim import format_payload


class Handler(BaseHandler):

    name = "Proto"

    def on_init(self):
        self.buf_nr = None

    def on_pre_handle(self, *_):
        if self.buf_nr is None or self.nvim.funcs.winbufnr(self.buf_nr) == -1:
            self.nvim.command(
                "topleft vertical split | enew | setlocal nolist"
            )
            self.buf_nr = self.nvim.current.buffer.number

    def on_handle(self, msg, *_):
        [self.nvim.buffers[self.buf_nr].append(i) for i in format_payload(msg)]
