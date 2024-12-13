import smbus # type: ignore
import time

class I2C:
    def __init__(self, address: int, i2c_bus: int = 1, read_command: int = 0x00) -> None:
        self.I2C = smbus.SMBus(i2c_bus)
        self.ReadCommand = read_command
        self.Address = address

    def SplitCommand(self, command: int) -> list:
        msb = (command >> 8) & 0xFF
        lsb = command & 0xFF
        return [msb, lsb]

    def CombineCommand(self, first: int, second: int) -> int:
        return first << 8 | second

    def SendCommand(self, command: int) -> bool:
        split = self.SplitCommand(command)
        msb = split[0]
        lsb = split[1]
        self.I2C.write_i2c_block_data(self.Address,msb,[lsb])
        time.sleep(0.2)
        return True
    
    def ReadData(self, bytesToRead: int) -> list:
        if bytesToRead < 0:
            return []
        data = self.I2C.read_i2c_block_data(self.Address, self.ReadCommand, bytesToRead)
        return data

    def ReadFrom(self, register: int, bytesToRead: int) -> list:
        if bytesToRead < 0:
            return []
        data = self.I2C.read_i2c_block_data(self.Address, register, bytesToRead)
        return data

    def CalculateCRC(self, data: list) -> int:
        crc = 0xff
        for current_byte in data:
            crc ^= current_byte
            for _ in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ 0x31
                else:
                    crc <<= 1
                crc &= 0xFF  # Ensure that the result stays within 8 bits
        
        return crc

    def SendData(self, register: int, data: list) -> bool:
        self.I2C.write_i2c_block_data(self.Address, register, data)
        time.sleep(0.01)
        return True