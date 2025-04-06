from enum import Enum
import json
from typing import TypeAlias


class ResponseCode(Enum):
    OK = 0              # 请求正常
    Timeout = 1         # 请求超时
    QueueFull = 2       # 请求队列已满
    NetError = 3        # 网络异常
    RequestFailed = 4   # 请求失败


class Response:
    def __init__(self, code: ResponseCode = ResponseCode.OK, msg: str = "", data: json = "") -> None:
        self.code = code
        self.msg = msg
        self.data = data

# 机器人状态


class RobotState(Enum):
    Unknow = -1         # 未知
    Init = 0            # 初始化
    StandBy = 1         # 已下电
    Ready = 2           # 手动模式
    Rescue = 3          # 救援模式
    Auto = 4            # 自动模式
    Error = 6           # 机器人出错

# 速度


class Speed:
    def __init__(self, joint: float, tcp: float, ori: float) -> None:
        self.joint = joint
        self.tcp = tcp
        self.ori = ori


Acc: TypeAlias = Speed


class UserCommand(Enum):
    SwitchOn = 1  # 上电
    SwitchOff = 2  # 下电
    ToReady = 3  # 进入手动模式
    ToAuto = 5  # 进入自动模式
    AcknowledgeError = 100  # 清除错误
    Recovery = 1000 # 恢复故障点模式
    ExitRecovery = 0 # 退出恢复故障点


class JogSpeed(Enum):
    Low = 1  # 低速
    Mid = 2  # 中速
    High = 3  # 高速


class Direction(Enum):
    Positive = 1  # 正方向
    Negative = -1  # 负方向


class UserCoor:
    def __init__(self, x: float, y: float, z: float, a: float, b: float, c: float):
        self.x = x  # 用户坐标系原点相对于世界坐标系在 x 方向的位移偏移量, 单位: mm
        self.y = y  # 用户坐标系原点相对于世界坐标系在 y 方向的位移偏移量, 单位: mm
        self.z = z  # 用户坐标系原点相对于世界坐标系在 z 方向的位移偏移量, 单位: mm
        self.a = a  # 用户坐标系相对于世界坐标系 x 轴旋转的欧拉角, 单位: deg
        self.b = b  # 用户坐标系相对于世界坐标系 y 轴旋转的欧拉角, 单位: deg
        self.c = c  # 用户坐标系相对于世界坐标系 z 轴旋转的欧拉角, 单位: deg

# @brief 质心矢量是以安装的工具或负载在坐标系 Otool-XYZ 上的位置设定.


class CenterPos:
    def __init__(self, Mx: float = 0, My: float = 0, Mz: float = 0):
        self.Mx = Mx  # 安装的工具或装夹的负载的重心 C 在坐标系 Otool-XYZ 的 X 方向上的偏移量, 单位: mm
        self.My = My  # 安装的工具或装夹的负载的重心 C 在坐标系 Otool-XYZ 的 Y 方向上的偏移量, 单位: mm
        self.Mz = Mz  # 安装的工具或装夹的负载的重心 C 在坐标系 Otool-XYZ 的 Z 方向上的偏移量, 单位: mm

# @brief 该参数是以安装的工具或负载由输出坐标系 Otool-XYZ 决定的惯性张量.


class InertiaTensor:
    def __init__(self, Ixx: float = 0, Iyy: float = 0, Izz: float = 0, Ixy: float = 0, Ixz: float = 0, Iyz: float = 0):
        self.Ixx = Ixx  # 安装的工具或装夹的负载在重心处 X 方向回转的惯量, 单位: kg*mm2
        self.Iyy = Iyy  # 安装的工具或装夹的负载在重心处 Y 方向回转的惯量, 单位: kg*mm2
        self.Izz = Izz  # 安装的工具或装夹的负载在重心处 Z 方向回转的惯量, 单位: kg*mm2
        self.Ixy = Ixy  # 安装的工具或装夹的负载在重心处 XY 交叉方向的惯量积, 单位: kg*mm2
        self.Ixz = Ixz  # 安装的工具或装夹的负载在重心处 XZ 交叉方向的惯量积, 单位: kg*mm2
        self.Iyz = Iyz  # 安装的工具或装夹的负载在重心处 YZ 交叉方向的惯量积, 单位: kg*mm2

# @brief 用来存储机器人末端工具和负载质量信息参数，用于机器人动力学全模型计算.


class LoadDyn:
    def __init__(self, mass: float = 0, centerPos: CenterPos = CenterPos(), inertiaTensor: InertiaTensor = InertiaTensor()):
        self.mass = mass  # 工具&负载的重量, 单位: kg;
        self.centerPos = centerPos  # 参见 CenterPos;
        self.inertiaTensor = inertiaTensor  # 参见 InertiaTensor;


class Tool:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, a: float = 0, b: float = 0, c: float = 0, dyn: LoadDyn = LoadDyn()) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c
        self.dyn = dyn

# 过渡类型


class ZoneType(Enum):
    Fine = 0  # 不过渡
    Relative = 1  # 相对过渡
    Absolute = 2  # 绝对过渡


class Zone:
    def __init__(self, per: float = 0, dis: float = 0):
        self.per = per  # 转弯百分比值，过渡类型为相对过渡时生效，适用所有运动类型
        self.dis = dis  # 笛卡尔空间转弯区大小，单位: mm，过渡类型为绝对过渡时生效，不适用MovJ


class MovType(Enum):
    MovJ = 0
    MovL = 1
    MovC = 2
    MovCircle = 3


class PointType(Enum):
    Joint = 0  # 关节位置
    Cart = 1  # 笛卡尔位置


class Apos:
    def __init__(self, jotPos: list[float] | None = [0.0]*7) -> None:
        self.jotPos = jotPos  # 机器人 n 关节的位置, 单位: m(直线电机) 或 rad(旋转电机);


class AposJson(object):

    @staticmethod
    def toJson(value: Apos) -> str:
        data = {
            "jntpos1": value.jotPos[0],
            "jntpos2": value.jotPos[1],
            "jntpos3": value.jotPos[2],
            "jntpos4": value.jotPos[3],
            "jntpos5": value.jotPos[4],
            "jntpos6": value.jotPos[5],
            "jntpos7": value.jotPos[6],
        }
        return json.dumps(data)

    @staticmethod
    def fromJson(value: str) -> Apos:
        data = json.loads(value)
        return Apos([data["jntpos1"], data["jntpos2"], data["jntpos3"], data["jntpos4"], data["jntpos5"], data["jntpos6"], data["jntpos7"] if "jntpos7" in data else 0.0])

# 机器人在相同的笛卡尔空间位置下，可以具备多种关节位置组合对应
#       (机器人逆解的多解).该属性用于定义空间目标点对应的形态配置数据.


class PosCfg:
    def __init__(self, mode: int = -1, cf: list[int] = [0]*7) -> None:
        self.mode = mode  # 机器人工作构型选取参数;
        self.cf = cf  # 关节 n 号轴角度所在的象限取值;


class PosCfgJson(object):

    @staticmethod
    def toJson(value: PosCfg) -> str:
        data = {
            "mode": value.mode,
            "cf1": value.cf[0],
            "cf2": value.cf[1],
            "cf3": value.cf[2],
            "cf4": value.cf[3],
            "cf5": value.cf[4],
            "cf6": value.cf[5],
            "cf7": value.cf[6],
        }
        return json.dumps(data)

    @staticmethod
    def fromJson(value: str) -> PosCfg:
        data = json.loads(value)
        return PosCfg(data["mode"], [data["cf1"], data["cf2"], data["cf3"], data["cf4"], data["cf5"], data["cf6"], data["cf7"] if "cf7" in data else 0.0])

# TCP 点在笛卡尔坐标系下位置.


class Cpos:
    def __init__(self, cfgData: PosCfg = PosCfg(), x: float = 0.0, y: float = 0.0, z: float = 0.0, a: float = 0.0, b: float = 0.0, c: float = 0.0, e: float = 0.0) -> None:
        self.cfgData = cfgData  # 参见 PosCfg;
        self.x = x  # TCP 点在参考坐标系上 x 方向的坐标, 单位: m;
        self.y = y  # TCP 点在参考坐标系上 y 方向的坐标, 单位: m;
        self.z = z  # TCP 点在参考坐标系上 z 方向的坐标, 单位: m;
        self.a = a  # TCP 点相对于参考坐标系 z 轴旋转的欧拉角, 单位: rad;
        self.b = b  # TCP 点相对于参考坐标系 y′轴旋转的欧拉角, 单位: rad;
        self.c = c  # TCP 点相对于参考坐标系 x″轴旋转的欧拉角, 单位: rad;
        self.e = e  # 7 自由度机器人肘关节 (elbow) 姿态;


class CposJson(object):

    @staticmethod
    def toJson(value: Cpos) -> str:
        data = {
            "poscfg": PosCfgJson.toJson(value.cfgData),
            "x": value.x,
            "y": value.y,
            "z": value.z,
            "a": value.a,
            "b": value.b,
            "c": value.c,
            "e": value.e,
        }
        return json.dumps(data)

    @staticmethod
    def fromJson(value: str) -> Cpos:
        data = json.loads(value)
        return Cpos(
            PosCfgJson.fromJson(data["poscfg"]),
            data["x"],
            data["y"],
            data["z"],
            data["a"],
            data["b"],
            data["c"],
            data["e"] if "e" in data else 0,
        )


class Point:
    def __init__(self, mtype: PointType = PointType.Joint, apos: Apos = Apos(), cpos: Cpos = Cpos()) -> None:
        self.type = mtype
        self.apos = apos
        self.cpos = cpos


class MovSegment:
    def __init__(self, mtype: MovType = None, targetPosition: Point = None, middlePosition: Point = None, speed: Speed = None, acc: Acc = None, zoneType: ZoneType = None, zone: Zone = None):
        self.type = mtype
        self.targetPosition = targetPosition
        self.middlePosition = middlePosition
        self.speed = speed
        self.acc = acc
        self.zoneType = zoneType
        self.zone = zone


class MovJointSegments:
    def __init__(self, segments: list[MovSegment]):
        self.segments = segments

    def AddMovJ(self, position: Point, speed: Speed, acc: Acc, zoneType: ZoneType, zone: Zone):
        if zoneType == ZoneType.Absolute:
            raise ValueError("zoneType can not be ABSOLUTE")

        self.segments.append()
        segment = self.segments[-1]
        segment.type = MovType.MovJ
        segment.targetPosition = position
        segment.speed = speed
        segment.acc = acc
        segment.zoneType = zoneType
        segment.zone = zone


class MovCartSegments:
    def __init__(self, segments: list[MovSegment] = []) -> None:
        self.segments = segments

    def AddMovL(self, position: Point, speed: Speed, acc: Acc, zoneType: ZoneType, zone: Zone):
        # self.segments.append()
        segment = MovSegment()

        segment.type = MovType.MovL
        segment.targetPosition = position
        segment.speed = speed
        segment.acc = acc
        segment.zoneType = zoneType
        segment.zone = zone
        self.segments.append(segment)

    def AddMovC(self, middlePosition: Point, targetPosition: Point, speed: Speed, acc: Acc, zoneType: ZoneType, zone: Zone):
        segment = MovSegment()

        segment.type = MovType.MovC
        segment.middlePosition = middlePosition
        segment.targetPosition = targetPosition
        segment.speed = speed
        segment.acc = acc
        segment.zoneType = zoneType
        segment.zone = zone
        self.segments.append(segment)

    def AddMovCircle(self, middlePosition: Point, targetPosition: Point, speed: Speed, acc: Acc, zoneType: ZoneType, zone: Zone):
        segment = MovSegment()

        segment.type = MovType.MovCircle
        segment.middlePosition = middlePosition
        segment.targetPosition = targetPosition
        segment.speed = speed
        segment.acc = acc
        segment.zoneType = zoneType
        segment.zone = zone
        self.segments.append(segment)
