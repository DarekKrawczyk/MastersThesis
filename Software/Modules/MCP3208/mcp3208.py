from HardwareUtilities.SPI_Wrapper import SPI, SPIconfiguration

class MCP3208:
    def __init__(self, spi_config: SPIconfiguration, v_ref: float) -> None:
        self.__SPI_config = spi_config
        self.__vRef = v_ref
        self.__SPI = SPI(spi_config=spi_config)
        
    def ReadChannel(self, channel_id:int, single: bool) -> int:
        if channel_id < 0 or channel_id > 7:
            raise Exception("Invalid channel!")
        
        d2 = channel_id >> 2
        d1d0 = (channel_id & 0b00000011) << 6
        
        oct1 = 0b00000110
        if single == False:
            oct1 &= 0b00000100
        
        oct1 |= d2
        oct2 = 0b00000000 | d1d0
        oct3 = 0b00000000
        
        request = [oct1, oct2, oct3]
        
        data_buffer = self.__SPI.PerformTransaction(request)
        
        data = ((data_buffer[1] & 0b00001111) << 8) | data_buffer[2]
        
        return data 
        
    def ReadChannelSingle(self, channel_id:int) -> int:
        data = self.ReadChannel(channel_id=channel_id, single=True)
        return data
    
    def ReadChannelSingleToVolts(self, channel_id: int) -> float:
        bit_code = self.ReadChannelSingle(channel_id=channel_id)
        v_in = (bit_code * self.__vRef)/4096
        return v_in
    
    def ReadChannelDiff(self, channel_config:int) -> int:
        data = self.ReadChannel(channel_id=channel_config, single=False)
        return data
    
    def ReadChannelDiffToVolts(self, channel_config: int) -> float:
        bit_code = self.ReadChannelDiff(channel_config=channel_config)
        v_in = (bit_code * self.__vRef)/4096
        return v_in
