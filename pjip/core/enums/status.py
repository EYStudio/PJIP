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
    IDLE = auto()
    CHECKING = auto()
    UPDATE_AVAILABLE = auto()
    IS_LATEST = auto()
    LOCAL_NEWER = auto()
    NOT_FOUND = auto()
    ERROR = auto()
    # WILL BE REMOVE IN VERSION 2.0
    FIND_LATEST = UPDATE_AVAILABLE
    NORMAL = CHECKING


class PidStatus(Enum):
    EXISTS = auto()
    NOT_EXISTS = auto()
    ACCESS_DENIED = auto()
    ERROR = auto()

    # Reserved extension status
    ZOMBIE = auto()
    STOPPED = auto()
    UNKNOWN = auto()
