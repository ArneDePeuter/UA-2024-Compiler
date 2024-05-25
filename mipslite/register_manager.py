class RegisterManager:
    def __init__(self):
        self.registers = {
            'arg': ['$a0', '$a1', '$a2', '$a3'],
            'temp': ['$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$t8', '$t9'],
            'float': ['$f0', '$f1', '$f2', '$f3', '$f4', '$f5', '$f6', '$f7', '$f8', '$f9', '$f10', '$f11', # '$f12' = reserved for syscall
                      '$f13', '$f14', '$f15', '$f16', '$f17', '$f18', '$f19', '$f20', '$f21', '$f22', '$f23', '$f24', '$f25', '$f26', '$f27', '$f28', '$f29', '$f30', '$f31'],
            'saved': ['$s0', '$s1', '$s2', '$s3', '$s4', '$s5', '$s6', '$s7'],
            'v': ['$v0', '$v1'],
            'special': ['$zero', '$at', '$gp', '$sp', '$fp', '$ra']
        }
        self.used_registers = {key: [] for key in self.registers}

    def allocate(self, reg_type):
        if reg_type not in self.registers or not self.registers[reg_type]:
            raise RuntimeError(f"Out of {reg_type} registers")
        reg = self.registers[reg_type].pop(0)
        self.used_registers[reg_type].append(reg)
        print(f"Allocated {reg} of type {reg_type}")  # Debug print
        return reg

    def free(self, reg):
        for reg_type, reg_list in self.used_registers.items():
            if reg in reg_list:
                reg_list.remove(reg)
                self.registers[reg_type].insert(0, reg)
                print(f"Freed {reg} of type {reg_type}")  # Debug print
                return
        raise ValueError(f"Register {reg} not found in used registers")

    def allocate_temp(self):
        return self.allocate('temp')

    def allocate_float(self):
        return self.allocate('float')

    def allocate_arg(self):
        return self.allocate('arg')
