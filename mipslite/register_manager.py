class RegisterManager:
    def __init__(self):
        # List of all general-purpose MIPS registers
        self.available_registers = [
            '$zero', '$at', '$v0', '$v1',
            '$a0', '$a1', '$a2', '$a3',
            '$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$t8', '$t9',
            '$s0', '$s1', '$s2', '$s3', '$s4', '$s5', '$s6', '$s7',
            '$k0', '$k1',
            '$gp', '$sp', '$fp', '$ra'
        ]
        self.used_registers = []

    def allocate(self):
        if not self.available_registers:
            raise RuntimeError("Out of registers")
        reg = self.available_registers.pop(0)
        self.used_registers.append(reg)
        return reg

    def free(self, reg):
        if reg in self.used_registers:
            self.used_registers.remove(reg)
            self.available_registers.append(reg)