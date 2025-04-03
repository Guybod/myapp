import time

from Request import *


class CodroidApi:
    def __init__(self, host: str, port: str):
        self._request = Request(host, port)
        self._homePosition: list[float] = [0, 0, 90, 0, 90, 0]
        self._packPosition: list[float] = [89, 0, 148.3, -31.7, 181, 180]
        # self._request.connect()

    # def __del__(self):
    #     self._request.close()

    """
    发送用户命令.

    :param cmd: 参考UserCommand说明
    :param timeout: 超时等待时间
    :return:
    """

    def sendUserCommand(self, cmd: UserCommand, timeout: int = 30) -> Response:
        paramitem: dict = {
            "path": "Robot/Control/command",
            "value": cmd.value
        }
        paramlist = [paramitem]
        param = json.dumps(paramlist)
        future: Future[Response] = self._request.send(
            "common", "setparam", param, timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    获取机器人状态.

    :param timeout: 超时时间
    :return: Response.data 是整数json，可通过 int state = res.data; 拿到数值，
             数值定义参考Define.h文件中 enum class RobotState
             None    = -1,  // 未知
             Init    = 0,   // 初始化
             StandBy = 1,   // 已下电
             Ready   = 2,   // 手动模式
             Rescue  = 3,   // 救援模式
             Auto    = 4,   // 自动模式
             Error   = 6,   // 机器人出错
    """

    def getRobotState(self, timeout: int = 30) -> Response:

        path: str = 'Robot/Control/state'
        param = [path]
        # print(json.loads(json.dumps(param)))
        future: Future = self._request.send(
            "common", "getparam", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = json.loads(json.dumps(res.data))
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    '''
    获取机器人状态标志

    :param timeout: 超时时间
    :return 返回值res.data包含data["robotMode"]， data["safetyMode"]和data["statusFlag"]
    robotMode: "PowerOff", "Idle", "Jogging", "Dragging","ToPoint","AutoReady","AutoRunning", "Rescue", "Fault","other"
    safetyMode	含义	
    2	        急停按下	
    1	        正常模式	
    3	        救援模式	
    4	        缩减模式	
    0	        存在错误
    ----------------------
    statusFlag							
    |位0         |位1         |位2         |位3                 |位4  |位5  |位6  |位7
    |急停按下标志  |上电标志    |拖动中标志    |机器人运动中标志       |(未使用)   (未使用) (未使用) (未使用)
    |位8         |位9 |位10        |位11 |位12 |位13 |位14 |位15
    |仿真标志    |停止、运行、暂停    |(未使用)   (未使用) (未使用) (未使用) 错误标志
    '''

    def getRobotStateFlag(self, timeout: int = 30) -> Response:

        future: Future[Response] = self._request.send("common", "getRobotStates", json.dumps(""), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = json.loads(json.dumps(res.data))
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    获取打包位.

    \param timeout
    \return Response.data 是json数组，double[6] 各关节旋转角度，单位度（deg）
    """

    def getPackPosition(self, timeout: int = 5) -> Response:
        path: str = "Robot/Parameter/Mechanism/packingPosition"
        param = json.dumps([path])
        future: Future[Response] = self._request.send(
            "common", "getparam", param, timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = json.loads(res.data)
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
            else:
                res.data = data["data"][path]
        return res

    """
    通过MovJoint运动到Home位.

    :param speed: 运动速度，单位度/秒
    :param acc: 运动加速度，单位度/秒平方
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def goHome(self, speed: float = 60, acc: float = 80, timeout: int = 30) -> Response:
        point: Point = Point()
        point.apos.jotPos[0] = self._homePosition[0]
        point.apos.jotPos[1] = self._homePosition[1]
        point.apos.jotPos[2] = self._homePosition[2]
        point.apos.jotPos[3] = self._homePosition[3]
        point.apos.jotPos[4] = self._homePosition[4]
        point.apos.jotPos[5] = self._homePosition[5]
        return self.movJ(point, speed, acc, timeout)

    """
    设置Home位.

    :position double[6] 各关节旋转角度，单位度（deg）
    """

    def setHomePosition(self, position: list) -> None:
        self._homePosition = position

    """
    通过MovJoint运动到打包位.

    :param speed: 运动速度，单位度/秒
    :param acc: 运动加速度，单位度/秒平方
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def goPack(self, speed: float = 60, acc: float = 80, timeout: int = 30) -> Response:
        point: Point = Point()
        point.apos.jotPos[0] = self._packPosition[0]
        point.apos.jotPos[1] = self._packPosition[1]
        point.apos.jotPos[2] = self._packPosition[2]
        point.apos.jotPos[3] = self._packPosition[3]
        point.apos.jotPos[4] = self._packPosition[4]
        point.apos.jotPos[5] = self._packPosition[5]
        return self.movJ(point, speed, acc, timeout)

    """
    设置打包位置.

    :param position: double[6] 各关节旋转角度，单位度（deg）
    """

    def setPackPosition(self, position: list) -> None:
        self._packPosition = position

    """
    关节空间运动.

    :param position: 目标位置，类型为double[6]，数组分别为轴1~轴6的旋转角度，单位度（deg），例如[0,0,90,0,90,0]
    :param speed: 运动速度，单位度/秒
    :param acc: 运动加速度，单位度/秒平方
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def movJ(self, position: Point, speed: Speed, acc: Acc, timeout: int = 30) -> Response:
        param: json = {
            "type": "movj"
        }
        if position.type == PointType.Joint:
            param.update({
                "target": {
                    "type": "apos",
                    "apos": AposJson.toJson(position.apos)
                }
            })
        elif position.type == PointType.Cart:
            param.update({
                "target": {
                    "type": "cpos",
                    "apos": CposJson.toJson(position.cpos)
                }
            })

        param["speed"] = {
            "sper": speed.joint,
            "stcp": 0,
            "sori": 0,
            "sexjl": 0,
            "sexjr": 0
        }
        param["acc"] = {
            "aper": acc.joint,
            "atcp": 0,
            "aori": 0,
            "aexjl": 0,
            "aexjr": 0
        }
        future: Future[Response] = self._request.send(
            "common", "mov", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    多段关节空间运动.

    :param segements: 多段路径
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def movJointsSegments(self, segments: MovJointSegments, timeout: float = 30.0) -> Response:
        param = {
            "type": "movJoint",
            "points": []
        }
        for segment in segments.segments:
            param["points"].append()
            data = param["points"][-1]

            if segment.targetPosition.type == PointType.Joint:
                param.update({
                    "target": {
                        "type": "apos",
                        "apos": AposJson.toJson(segment.targetPosition.apos)
                    }
                })
            elif segment.targetPosition.type == PointType.Cart:
                param.update({
                    "target": {
                        "type": "apos",
                        "apos": CposJson.toJson(segment.targetPosition.cpos)
                    }
                })

            data["speed"] = {
                "sper": segment.speed.joint,
                "stcp": 0,
                "sori": 0,
                "sexjl": 0,
                "sexjr": 0,
            }

            data["acc"] = {
                "aper": segment.acc.joint,
                "atcp": 0,
                "aori": 0,
                "aexjl": 0,
                "aexjr": 0,
            }

            if segment.zoneType == ZoneType.Fine:
                data["zone"]["type"] = "FINE"
            elif segment.zoneType == ZoneType.Relative:
                data["zone"]["type"] = "RELATIVE"
            else:
                raise ValueError("Unknown zone type")

        future: Future[Response] = self._request.send(
            "common", "movMulti", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = json.loads(res.data)
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    关节空间运动，不等待返回.

    :param position: 目标位置，类型为double[6]，数组分别为轴1~轴6的旋转角度，单位度（deg），例如[0,0,90,0,90,0]
    :param speed: 运动速度，单位度/秒
    :param acc: 运动加速度，单位度/秒平方
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def movJNoResult(self, position: Point, speed: float = 60, acc: float = 80, timeout: float = 10):
        param = {
            "type": "movj",
        }
        if position.type == PointType.Joint:
            param.update({
                "target": {
                    "type": "apos",
                    "apos": AposJson.toJson(position.apos)
                }
            })

        elif position.type == PointType.Cart:
            param.update({
                "target": {
                    "type": "apos",
                    "apos": CposJson.toJson(position.cpos)
                }
            })

        param["speed"] = {
            "sper": speed,
            "stcp": 0,
            "sori": 0,
            "sexjl": 0,
            "sexjr": 0,
        }

        param["acc"] = {
            "aper": acc,
            "atcp": 0,
            "aori": 0,
            "aexjl": 0,
            "aexjr": 0,
        }
        self._request.send("common", "mov",
                           json.dumps(param), timeout)

    """
    直线运动.
    
    :param position: 目标位置，类型为double[6]，表示[x,y,z,rx,ry,rz]，
                     (x,y,z)表示笛卡尔空间的位置，单位毫米（mm），（rx,ry,rz）表示绕3个坐标轴的旋转角度，单位度（deg）
    :param speed: 运动速度，单位度/秒
    :param acc: 运动加速度，单位度/秒平方
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def movL(self, position: Point, speed: Speed = Speed(0, 250, 80), acc: Acc = Acc(0, 1200, 320),
             timeout: int = 30) -> Response:
        param = {}
        param["type"] = "movl"
        if position.type == PointType.Joint:
            param.update({
                "target": {
                    "type": "apos",
                    "apos": AposJson.toJson(position.apos)
                }
            })

        elif position.type == PointType.Cart:
            param.update({
                "target": {
                    "type": "cpos",
                    "apos": CposJson.toJson(position.cpos)
                }
            })

        param["speed"] = {
            "sper": 0,
            "stcp": speed.tcp,
            "sori": speed.ori,
            "sexjl": 0,
            "sexjr": 0,
        }

        param["acc"] = {
            "aper": 0,
            "atcp": acc.tcp,
            "aori": acc.ori,
            "aexjl": 0,
            "aexjr": 0,
        }

        future: Future[Response] = self._request.send(
            "common", "mov", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    圆弧运动.
    
    :param targetPosition: 目标位置，类型为double[6]，表示[x,y,z,rx,ry,rz]，
                           (x,y,z)表示笛卡尔空间的位置，单位毫米（mm），（rx,ry,rz）表示绕3个坐标轴的旋转角度，单位度（deg）
    :param middlePosition: 中间位置，数据类型同目标位置
    :param speed: 运动速度，单位度/秒
    :param acc: 运动加速度，单位度/秒平方
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def movC(self, middlePosition: Point, targetPosition: Point, speed: Speed = Speed(0, 250, 80),
             acc: Acc = Acc(0, 1200, 320), timeout: int = 30) -> Response:
        param: dict = {}
        param["type"] = "movc"
        if targetPosition.type == PointType.Joint:
            param.update({
                "target": {
                    "type": "apos",
                    "apos": AposJson.toJson(targetPosition.apos)
                }
            })
        elif targetPosition.type == PointType.Cart:
            param.update({
                "target": {
                    "type": "cpos",
                    "apos": CposJson.toJson(targetPosition.cpos)
                }
            })

        if middlePosition.type == PointType.Joint:
            param.update({
                "target": {
                    "type": "apos",
                    "apos": AposJson.toJson(middlePosition.apos)
                }
            })
        elif middlePosition.type == PointType.Cart:
            param.update({
                "target": {
                    "type": "cpos",
                    "apos": CposJson.toJson(middlePosition.cpos)
                }
            })

        param["speed"] = {
            "sper": 0,
            "stcp": speed.tcp,
            "sori": speed.ori,
            "sexjl": 0,
            "sexjr": 0,
        }

        param["acc"] = {
            "aper": 0,
            "atcp": acc.tcp,
            "aori": acc.ori,
            "aexjl": 0,
            "aexjr": 0,
        }

        future: Future[Response] = self._request.send(
            "common", "mov", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    多段笛卡尔空间运动.

    :param segements: 多段路径
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def movCartSegments(self, segments: MovCartSegments, timeout: int = 30) -> Response:
        param = {
            "type": "movCart",
            "points": [],
        }
        for segment in segments.segments:
            data = {
                "type": "movL",
            }

            if segment.type == MovType.MovL:
                data.update({
                    "type": "movL"
                })
            elif segment.type == MovType.MovC:
                data.update({
                    "type": "movC"
                })
            elif segment.type == MovType.MovCircle:
                data.update({
                    "type": "movCircle"
                })
            else:
                raise ValueError("MovType error")

            print(segment.targetPosition)
            if segment.targetPosition.type == PointType.Joint:
                data.update({
                    "target": {
                        "type": "apos",
                        "apos": AposJson.toJson(segment.targetPosition.apos)
                    }
                })
            elif segment.targetPosition.type == PointType.Cart:
                data.update({
                    "target": {
                        "type": "cpos",
                        "cpos": CposJson.toJson(segment.targetPosition.cpos)
                    }
                })

            if segment.type == MovType.MovC or segment.type == MovType.MovCircle:
                if segment.middlePosition.type == PointType.Joint:
                    data.update({
                        "center": {
                            "type": "apos",
                            "apos": AposJson.toJson(segment.middlePosition.apos)
                        }
                    })
                elif segment.middlePosition.type == PointType.Cart:
                    data.update({
                        "center": {
                            "type": "cpos",
                            "cpos": CposJson.toJson(segment.middlePosition.cpos)
                        }
                    })
            data.update({
                "speed": {
                    "sper": segment.speed.joint,
                    "stcp": segment.speed.tcp,
                    "sori": segment.speed.ori,
                    "sexjl": 0,
                    "sexjr": 0,
                }
            })

            data.update({
                "acc": {
                    "aper": segment.speed.joint,
                    "atcp": segment.acc.tcp,
                    "aori": segment.acc.ori,
                    "aexjl": 0,
                    "aexjr": 0,
                }
            })

            if segment.zoneType == ZoneType.Fine:
                data.update({
                    "zone": {
                        "type": "FINE"
                    }
                })
            elif segment.zoneType == ZoneType.Relative:
                data.update({
                    "zone": {
                        "type": "RELATIVE"
                    }
                })
            elif segment.zoneType == ZoneType.Absolute:
                data.update({
                    "zone": {
                        "type": "ABSOLUTE"
                    }
                })
            else:
                raise ValueError("Zonetype error")

            data["zone"].update({
                "data": {
                    "zper": segment.zone.per,
                    "zdis": segment.zone.dis,
                    "zvconst": 0
                }
            })
            param["points"].append(data)

        future: Future[Response] = self._request.send(
            "common", "movMulti", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    让机器人停止运动.
    
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def stopMov(self, timeout: int = 30) -> Response:
        future: Future[Response] = self._request.send(
            "common", "stopMov", json.dumps(), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    关节点动. 该请求发送后，如果要保持点动持续，需要持续调keepJog接口，否则点动持续1s后会自动停止
    :param jogIndex 需要点动的轴，范围1~6
    :param jogSpeed 点动速度
    :param direction 点动方向
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def jointJog(self, jogIndex: int, jogSpped: JogSpeed, direction: Direction, timeout: int = 30) -> Response:
        param = []
        mode = {
            "path": "Robot/Control/jogMode",
            "value": 1
        }
        param.append(mode)
        speed = {
            "path": "Robot/Control/jogSpeed",
            "value": direction.value * jogSpped.value
        }
        param.append(speed)
        index = {
            "path": "Robot/Control/jogIndex",
            "value": jogIndex
        }
        param.append(index)
        future: Future[Response] = self._request.send(
            "common", "setparam", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    末端点动. 该请求发送后，如果要保持点动持续，需要持续调keepJog接口，否则点动持续1s后会自动停止
    :param jogIndex: 1~6 分别对应 x,y,z,rx,ry,rz
    :param jogSpped: 点动速度
    :param direction: 点动方向
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def tcpJog(self, jogIndex: int, jogSpped: JogSpeed, direction: Direction, timeout: int = 30) -> Response:
        param = []
        mode = {
            "path": "Robot/Control/jogMode",
            "value": 2
        }
        param.append(mode)
        speed = {
            "path": "Robot/Control/jogSpeed",
            "value": direction.value * jogSpped.value
        }
        param.append(speed)
        index = {
            "path": "Robot/Control/jogIndex",
            "value": jogIndex
        }
        param.append(index)
        future: Future[Response] = self._request.send(
            "common", "setparam", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    保持当前点动. 以500毫秒左右的频率持续调该接口，可保持点动持续
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def keepJog(self, timeout: int = 30) -> Response:
        param = []
        paramitem = {
            "path": "Robot/Control/commandHeart",
            "value": int(datetime.now().timestamp() * 1000)
        }
        param.append(paramitem)
        future: Future[Response] = self._request.send(
            "common", "setparam", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    停止电动
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def stopJog(self, timeout: int = 30) -> Response:
        param = []
        jogMode = {
            "path": "Robot/Control/stopJog",
            "value": 0
        }
        param.append(jogMode)
        jogSpeed = {
            "path": "Robot/Control/jogSpeed",
            "value": 0
        }
        param.append(jogSpeed)
        jogIndex = {
            "path": "Robot/Control/jogIndex",
            "value": 0
        }
        param.append(jogIndex)
        future: Future[Response] = self._request.send(
            "common", "setparam", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
        return res

    """
    获取当前关节位置
    :param timeout: 超时等待时间
    :return: Response.data是长度为6的json数组，表示1~6关节的旋转角度
    可通过 vector<double> p = res.data 获得，
    或double p[6] = {res.data[0], res.data[1], res.data[2], res.data[3], res.data[4], res.data[5]}
    """

    def getJointPosition(self, timeout: int = 30) -> Response:
        future: Future[Response] = self._request.send(
            "common", "getCurAPos", json.dumps(""), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
            else:
                res.data = {
                    float(data["data"]["jntpos1"]),
                    float(data["data"]["jntpos2"]),
                    float(data["data"]["jntpos3"]),
                    float(data["data"]["jntpos4"]),
                    float(data["data"]["jntpos5"]),
                    float(data["data"]["jntpos6"])
                }
        return res

    """
    获取当前笛卡尔坐标位置

    :param timeout: 超时等待时间
    :return: Response.data是长度为6的json数组，[x,y,z,rx,ry,rz]
             可通过 vector<double> p = res.data 获得，
             或double p[6] = {res.data[0], res.data[1], res.data[2], res.data[3], res.data[4], res.data[5]}
    """

    def getCartPosition(self, timeout: int = 30) -> Response:
        future: Future[Response] = self._request.send(
            "common", "getCurCPos", json.dumps(""), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
            else:
                res.data = {
                    float(data["data"]["x"]),
                    float(data["data"]["y"]),
                    float(data["data"]["z"]),
                    float(data["data"]["a"]),
                    float(data["data"]["b"]),
                    float(data["data"]["c"])
                }
        return res

    """
    根据笛卡尔位置获取关节角

    :param cpos: 需要逆解的笛卡尔坐标
    :param refAPos: 执行逆解时的参考角
    :param timeout: 超时等待时间
    :return: Response.data是长度为6的json数组，表示1~6关节的旋转角度
             可通过 vector<double> p = res.data 获得，
             或double p[6] = {res.data[0], res.data[1], res.data[2], res.data[3], res.data[4], res.data[5]}
    """

    def cposToApos(self, cpos: Cpos, refAPos: Apos, tool: Tool | None = None, coor: UserCoor | None = None,
                   timeout: int = 30) -> Response:
        param = {"cpos": CposJson.toJson(cpos), "apos": AposJson.toJson(refAPos)}
        future: Future[Response] = self._request.send(
            "common", "cpostoapos", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
            else:
                res.data = {
                    float(data["data"]["jntpos1"]),
                    float(data["data"]["jntpos2"]),
                    float(data["data"]["jntpos3"]),
                    float(data["data"]["jntpos4"]),
                    float(data["data"]["jntpos5"]),
                    float(data["data"]["jntpos6"])
                }
        return res

    """
    设置数字输出端口值.

    :param port: 端口号
    :param val: 端口值，只能是0或1
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def setDO(self, port: int, val: int, timeout: int = 30) -> Response:
        param = {"port": port, "val": val}
        future: Future[Response] = self._request.send(
            "common", "setDO", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    获取数字输入端口值.

    :param port: 端口号
    :param timeout: 超时等待时间
    :return: Response.data 是整数json，可通过 int val = res.data; 拿到数值,值为0或1
    """

    def getDI(self, port: int, timeout: int = 30) -> Response:
        param = {"port": port}
        future: Future[Response] = self._request.send(
            "common", "getDI", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = json.loads(res.data)
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
            else:
                res.data = data["data"]

        return res

    """
    设置数字输出端口值.

    :param port: 端口号
    :param val: 端口值，只能是0或1
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def setDOGroup(self, startPort: int, endPoint: int, val: int, timeout: int = 30) -> Response:
        param = {"startPort": startPort, "endPort": endPoint, "val": val}
        future: Future[Response] = self._request.send(
            "common", "setDOGroup", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    获取数字输入端口值.

    :param port: 端口号
    :param timeout: 超时等待时间
    :return: Response.data 是整数json，可通过 int val = res.data; 拿到数值,值为端口从低到高对应的二进制数的十进制值
    """

    def getDIGroup(self, startPort: int, endPoint: int, timeout: int = 30) -> Response:
        param = {"startPort": startPort, "endPort": endPoint}
        future: Future[Response] = self._request.send(
            "common", "getDIGroup", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    设置当前坐标系.

    :param varName: 坐标系变量名
                    注: 该变量名用于在UI界面显示，该变量最好是已有变量，且参数与与下面下发的保持一致，以避免造成一些错误
    :param coor: 坐标系参数
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def setCurrentCoor(self, vaName: str, coor: UserCoor, timeout: int = 30) -> Response:
        param = {
            "key": vaName,
            "value": {
                "USERCOOR": {
                    "x": coor.x,
                    "y": coor.y,
                    "z": coor.z,
                    "a": coor.a,
                    "b": coor.b,
                    "c": coor.c,
                }
            }
        }
        future: Future[Response] = self._request.send(
            "common", "setCurrentCoor", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    设置当前工具.

    :param varName: 工具变量名
                    注: 该变量名用于在UI界面显示，该变量最好是已有变量，且参数与与下面下发的保持一致，以避免造成一些错误
    :param tool: 工具参数
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def setCurrentTool(self, varName: str, tool: Tool, timeout: int = 30) -> Response:
        param = {
            "key": varName,
            "value": {
                "TOOL": {
                    "x": tool.x,
                    "y": tool.y,
                    "z": tool.z,
                    "a": tool.a,
                    "b": tool.b,
                    "c": tool.c,
                    "dyn": {
                        "m": tool.dyn.mass,
                        "pos": {
                            "mx": tool.dyn.centerPos.Mx,
                            "my": tool.dyn.centerPos.My,
                            "mz": tool.dyn.centerPos.Mz,
                        },
                        "tensor": {
                            "ixx": tool.dyn.inertiaTensor.Ixx,
                            "ixy": tool.dyn.inertiaTensor.Ixy,
                            "ixz": tool.dyn.inertiaTensor.Ixz,
                            "iyy": tool.dyn.inertiaTensor.Iyy,
                            "iyz": tool.dyn.inertiaTensor.Iyz,
                            "izz": tool.dyn.inertiaTensor.Izz,
                        }
                    }
                }
            }
        }
        future: Future[Response] = self._request.send(
            "common", "setcurtool", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    设置当前负载.

    :param varName: 负载变量名
                    注: 该变量名用于在UI界面显示，该变量最好是已有变量，且参数与与下面下发的保持一致，以避免造成一些错误
    :param dyn: 负载参数
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def setCurentPayload(self, varName: str, dyn: LoadDyn, timeout: int = 30) -> Response:
        param: dict = {
            "key": varName,
            "PAYLOAD": {
                "dyn": {
                    "m": dyn.mass,
                    "pos": {
                        "mx": dyn.centerPos.Mx,
                        "my": dyn.centerPos.My,
                        "mz": dyn.centerPos.Mz,
                    },
                    "tensor": {
                        "ixx": dyn.inertiaTensor.Ixx,
                        "ixy": dyn.inertiaTensor.Ixy,
                        "ixz": dyn.inertiaTensor.Ixz,
                        "iyy": dyn.inertiaTensor.Iyy,
                        "iyz": dyn.inertiaTensor.Iyz,
                        "izz": dyn.inertiaTensor.Izz,
                    }
                }
            }
        }

        future: Future[Response] = self._request.send(
            "common", "setcurpayload", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    获取工程状态

    :param projectName: 工程名（避免使用中文字符）
    :param taskName: 程序名（避免使用中文字符）
    :param label: 标签名（避免使用中文字符）
    :param timeout: 超时等待时间
    :return: std::string
             IDLE: 空闲，没有工程在运行
             LOADING: 正在加载工程
             RUNNING: 正在运行工程
             PAUSE: 工程已暂停
             ERROR: 工程运行出错
    """

    def getProjectState(self, timeout: int = 30) -> Response:
        future: Future[Response] = self._request.send(
            "projexecute", "getProjectState", json.dumps(""), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
            else:
                res.data = data["data"]

        return res

    """
    运行指定工程

    :param projectName: 工程名（避免使用中文字符）
    :param taskName: 程序名（避免使用中文字符）
    :param label: 标签名（避免使用中文字符）
    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def runProject(self, projectName: str, taskName: str, label: str, timeout: int = 30) -> Response:
        param: dict = {
            "projectName": projectName,
            "taskName": taskName,
            "label": label
        }
        future: Future[Response] = self._request.send(
            "projexecute", "run", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    运行最后打开的工程

    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def runLastProject(self, timeout: int = 30) -> Response:
        param: dict = {

        }
        future: Future[Response] = self._request.send(
            "projexecute", "runLast", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    停止运行工程

    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def stopProject(self, timeout: int = 30) -> Response:
        param: dict = {

        }
        future: Future[Response] = self._request.send(
            "projexecute", "stop", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    暂停工程运行

    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def pauseProject(self, timeout: int = 30) -> Response:
        param: dict = {

        }
        future: Future[Response] = self._request.send(
            "projexecute", "pause", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    恢复工程运行

    :param timeout: 超时等待时间
    :return: 返回操作结果
    """

    def resumeProject(self, timeout: int = 30) -> Response:
        param: dict = {

        }
        future: Future[Response] = self._request.send(
            "projexecute", "resume", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    初始化RS485，建立连接

    :param type: 指定接口, "RS485": keba控制器RS485接口，"EC2RS485": 机械臂末端RS485接口
    :param baudrate: 波特率
    :param stopBit: 停止位, 0: 1停止位; 1: 1 1/2停止位; 2: 2停止位
    :param parity: 奇偶校验 0: 无; 1: 奇校验 2: 偶校验
    :param dataBit: 数据位，注：机械臂末端RS485接口的数据位固定为8，不可更改
    :param timeout: 等待超时时间，单位秒
    :return: 返回操作结果
    """

    def rs485Init(self, type: str, baudrate: int, stopBit: int = 0, parity: int = 0, dataBit: int = 8,
                  timeout: int = 30) -> Response:
        param: dict = {
            "baudrate": baudrate,
            "stopBit": stopBit,
            "parity": parity,
            "dataBit": dataBit
        }
        future: Future[Response] = self._request.send(
            type, "init", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    通过RS485发送数据

    :param type: 指定接口, "RS485": keba控制器RS485接口，"EC2RS485": 机械臂末端RS485接口
    :param msg: 发送的数据，列表中按顺序表示每个字节的数值
    :param timeout: 等待超时时间，单位秒
    :return: 返回操作结果
    """

    def rs485Write(self, type: str, msg: list, timeout: int = 30) -> Response:

        future: Future[Response] = self._request.send(
            type, "write", json.dumps(msg), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    清空读缓存

    :param type: 指定接口, "RS485": keba控制器RS485接口，"EC2RS485": 机械臂末端RS485接口
    :param timeout: 等待超时时间，单位秒
    :return: 返回操作结果
    """

    def rs485FlushReadBuffer(self, type: str, timeout: int = 30) -> Response:

        future: Future[Response] = self._request.send(
            type, "flushReadBuffer", json.dumps(""), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]

        return res

    """
    读取RS485收到的数据

    :param type: 指定接口, "RS485": keba控制器RS485接口，"EC2RS485": 机械臂末端RS485接口
    :param length: 读取的字节数
    :param timeout: 等待超时时间，单位秒
    :return: 返回操作结果
    """

    def rs485Read(self, type: str, length: int, timeout: int = 30) -> Response:
        param: dict = {
            "length": length,
            "timeout": timeout * 10000000
        }
        future: Future[Response] = self._request.send(
            type, "read", json.dumps(param), timeout)
        res: Response = future.result()
        if res.code == ResponseCode.OK:
            data: dict = res.data
            if data["code"] != 0:
                res.code = ResponseCode.RequestFailed
                res.msg = data["msg"]
            else:
                res.data = data["data"]

        return res

    """
    从故障点恢复到运动恢复点

    :param duration 持续时间，单位秒
    """

    def recoveryTaskPoint(self, duration: int = 2) -> Response:
        res: Response = self.sendUserCommand(UserCommand.Recovery)
        deadline = time.time() + duration
        while time.time() < deadline:
            time.sleep(0.01)
            res = self.keepJog()
        return res
