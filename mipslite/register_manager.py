class RegisterManager:
    def __init__(self):
        """
        Types of registers:
        arg: arguments
        temp: temporary
        saved: saved
        v: value (return)registers
        special: special registers
        """
        self.registers = {
            'arg': ['$a0', '$a1', '$a2', '$a3'],
            'temp': ['$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$t8', '$t9'],
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
        return reg

    def free(self, reg):
        for reg_type, reg_list in self.used_registers.items():
            if reg in reg_list:
                reg_list.remove(reg)
                self.registers[reg_type].append(reg)
                return
        raise ValueError(f"Register {reg} not found in used registers")