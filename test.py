from mipslite import Module

module = Module()
main = module.function("main")
addr = main.allocate(4)

test = module.function("test")
addr2 = test.allocate(8)

print(module)
