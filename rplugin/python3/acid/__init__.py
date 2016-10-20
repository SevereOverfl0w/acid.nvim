# encoding:utf-8
""" Acid stands for Asynchronous Clojure Interactive Development. """
import neovim
from acid.nvim import (
    localhost, path_to_ns, get_acid_ns,
    find_file_in_path, find_extensions, import_extensions
)
from acid.session import send, SessionHandler


@neovim.plugin
class Acid(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.sessions = SessionHandler()
        self.repls = {}
        self.handlers = {}
        self._init = False


    @neovim.command("AcidInit")
    def init(self, bang=True):
        self.init_handlers()
        self.init_vars()
        self._init = True

    def init_vars(self):
        def init_var(var, default=0):
            self.nvim.vars[var] = self.nvim.vars.get(var, default)

        [init_var(i, j)
         for i, j
         in [
             ('acid_loaded', 1),
             ('acid_auto_require', 1),
             ('acid_auto_start_repl', 0),
             ('acid_namespace', 'user'),
             ('acid_start_repl_fn', 'jobstart'),
             ('acid_start_repl_args', ['lein repl'])]]

    def init_handlers(self):
        for path in find_extensions(self.nvim, 'handlers'):
            handler = import_extensions(path, 'handlers', 'Handler')
            if handler:
                name = handler.name

                if name not in self.handlers:
                    self.handlers[name] = handler
                    handler.init_handler(self.nvim)

    def get_handler(self, handler):
        if isinstance(handler, (tuple, list)):
            handler, match = handler
        else:
            handler, match = handler, {}

        return (self.handlers.get(handler), match)

    def eval(self, data, *handlers):
        address = localhost(self.nvim)

        if address is None:
            self.nvim.command('echom "No repl open"')
            return

        handlers = [self.get_handler(i) for i in handlers]

        if not 'op' in data:
            data.update({'op': 'eval'})

        if not 'ns' in data:
            data.update({'ns': get_acid_ns(self.nvim)})

        send(self.sessions, address, handlers, data)

    @neovim.function("AcidEval")
    def acid_eval(self, data):
        payload = data[0]
        self.eval(payload, "Proto")

    @neovim.function("AcidGoTo")
    def acid_goto(self, data):
        payload = {"op": "info", "symbol": data[0]}
        self.eval(payload, ("Goto", {"resource": None}))

    @neovim.command("AcidGoToDefinition")
    def acid_goto_def(self):
        self.nvim.command('normal! "syiw')
        data = self.nvim.funcs.getreg('s')
        self.acid_goto([data])

    @neovim.command("AcidRequire")
    def acid_require(self):
        data = "(require '[{} :refer :all])".format(path_to_ns(self.nvim))
        self.eval({"code": data}, "Ignore")

    @neovim.command("AcidStartRepl", bang=True)
    def acid_init_repl(self, bang):
        nv = self.nvim
        # explicitly requiring tab cwd
        pwd = nv.funcs.getcwd(-1, 0)

        if pwd not in self.repls or bang:
            fn = nv.vars['acid_start_repl_fn']
            args = nv.vars['acid_start_repl_args']
            nv.call(fn, *args)
