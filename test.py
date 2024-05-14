from mipslite import Module

module = Module()
main = module.function("main")
addr = main.allocate(4)
if_block = main.spawn("if")
if_block.load("$t0", addr)
main = if_block.kill()

test = module.function("test")
addr2 = test.allocate(8)

print(module)
