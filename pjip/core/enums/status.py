from enum import Enum, auto


class PJIPGeneralStatus(Enum):
    SUCCESS = 0
    FAILED = 1
    ERROR = 2


class SuspendState(Enum):
    NOT_FOUND = 0
    SUSPENDED = 1
    RUNNING = 2


class UpdateState(Enum):
    NORMAL = 0
    FIND_LATEST = 1
    IS_LATEST = 2
    NOT_FOUND = 3
    ERROR = 4


class PidStatus(Enum):
    EXISTS = auto()
    NOT_EXISTS = auto()
    ACCESS_DENIED = auto()
    ERROR = auto()

    # Reserved extension status
    ZOMBIE = auto()
    STOPPED = auto()
    UNKNOWN = auto()
