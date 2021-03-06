# 0.1 Navigation
Deoplete completion will be maintained on
[async-clj-omni](https://github.com/clojure-vim/async-clj-omni/)

- [x] Make async **for real**
 - [x] Use WatchableConnection
- [x] Automatic Require
 - [x] Autocommand
- [x] Implement Go To Symbol v1
 - [x] Same Project
- [x] Stable API

# 0.2 Refactoring

- [ ] Docs
- [ ] Implement Go To Symbol v2
 - [ ] Different project with local source
  - [ ] Warn about different version
 - [ ] Different project with no source (open jar)
- [ ] Add missing require/import
- [ ] Convert chained fns to threads
- [ ] Convert threads back to fns
- [ ] Extract variables
  - [ ] To `let`
  - [ ] To `def`
- [ ] Extract functions
  - [ ] To `defn`
  - [ ] To `fn`
  - [ ] To `#()`
- [ ] Change data type
  - [ ] To `vec`
  - [ ] To `list`
  - [ ] To `map`
  - [ ] To `set`

# 0.3 Static

- [ ] Add lein static analysis
  - [ ] [kibit](https://github.com/jonase/kibit)
  - [ ] [bikeshed](https://github.com/dakrone/lein-bikeshed)
  - [ ] [eastwood](https://github.com/jonase/eastwood)
- [ ] Neomake integration

# 1.0 
