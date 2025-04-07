from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ConnectionException, ModbusIOException


class ModbusTCP:
    def __init__(self, host='127.0.0.1', port=502):
        """
        初始化 ModbusTCP 客户端。

        :param host: Modbus 服务器的 IP 地址。
        :param port: Modbus 服务器的端口号，默认为 502。
        """
        self.host = host
        self.port = port
        self.client = ModbusTcpClient(host=self.host, port=self.port)

    def connect(self):
        """
        连接到 Modbus 服务器。

        :return: 连接成功返回 True，否则返回 False。
        """
        try:
            if not self.client.is_socket_open():
                self.client.connect()
            return self.client.is_socket_open()
        except ConnectionException as e:
            print(f"连接失败: {e}")
            return False

    def disconnect(self):
        """
        断开与 Modbus 服务器的连接。
        """
        self.client.close()

    def read_holding_registers(self, address, count=1, unit=1):
        """
        读取保持寄存器。

        :param address: 起始地址。
        :param count: 要读取的寄存器数量，默认为 1。
        :param unit: 设备单元标识符，默认为 1。
        :return: 读取到的寄存器值列表，或 None 如果读取失败。
        """
        try:
            response = self.client.read_holding_registers(address, count, unit=unit)
            if response.isError():
                print(f"读取保持寄存器失败: {response}")
                return None
            return response.registers
        except ModbusIOException as e:
            print(f"读取保持寄存器时发生 I/O 错误: {e}")
            return None

    def write_single_register(self, address, value, unit=1):
        """
        写入单个保持寄存器。

        :param address: 寄存器地址。
        :param value: 要写入的值。
        :param unit: 设备单元标识符，默认为 1。
        :return: 写入成功返回 True，否则返回 False。
        """
        try:
            response = self.client.write_single_register(address, value, unit=unit)
            if response.isError():
                print(f"写入单个保持寄存器失败: {response}")
                return False
            return True
        except ModbusIOException as e:
            print(f"写入单个保持寄存器时发生 I/O 错误: {e}")
            return False

    def write_multiple_registers(self, address, values, unit=1):
        """
        写入多个保持寄存器。

        :param address: 起始地址。
        :param values: 要写入的值列表。
        :param unit: 设备单元标识符，默认为 1。
        :return: 写入成功返回 True，否则返回 False。
        """
        try:
            response = self.client.write_registers(address, values, unit=unit)
            if response.isError():
                print(f"写入多个保持寄存器失败: {response}")
                return False
            return True
        except ModbusIOException as e:
            print(f"写入多个保持寄存器时发生 I/O 错误: {e}")
            return False


# 示例用法
if __name__ == "__main__":
    modbus_client = ModbusTCP(host='192.168.1.100', port=502)

    if modbus_client.connect():
        print("连接成功")

        # 读取保持寄存器
        registers = modbus_client.read_holding_registers(address=0, count=3, unit=1)
        if registers is not None:
            print(f"读取到的寄存器值: {registers}")

        # 写入单个保持寄存器
        success = modbus_client.write_single_register(address=0, value=1234, unit=1)
        if success:
            print("写入单个保持寄存器成功")

        # 写入多个保持寄存器
        success = modbus_client.write_multiple_registers(address=0, values=[100, 200, 300], unit=1)
        if success:
            print("写入多个保持寄存器成功")

        modbus_client.disconnect()
        print("断开连接")
    else:
        print("连接失败")



