import llvmlite.ir as ir

int8 = ir.IntType(8)
int32 = ir.IntType(32)

ctx = ir.global_context
node_type = ctx.get_identified_type('struct.Node')
node_type_ptr_type = ir.PointerType(node_type)
node_type.set_body(int8, int8, node_type_ptr_type)

m = ir.Module()
f = ir.Function(m, ir.FunctionType(int32, []), 'main')
bldr = ir.IRBuilder(f.append_basic_block())

node_1 = bldr.alloca(node_type)
bldr.store(node_type([int8(5), int8(4), node_type_ptr_type(None)]), node_1)

node_2 = bldr.alloca(node_type)
node_2_val = ir.Constant(node_type, None)
node_2_val = bldr.insert_value(node_2_val, int8(5), [0])
node_2_val = bldr.insert_value(node_2_val, int8(4), [1])
node_2_val = bldr.insert_value(node_2_val, node_1, [2])
bldr.store(node_2_val, node_2)
bldr.ret(int32(0))

print(m)
