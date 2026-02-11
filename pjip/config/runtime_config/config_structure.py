from dataclasses import dataclass, field


@dataclass
class App:
    pass

@dataclass
class Logging:
    pass

@dataclass
class Process:
    pass

@dataclass
class UI:
    pass

@dataclass
class Features:
    pass

@dataclass
class Debug:
    pass

@dataclass
class ConfigRoot:
    app: App = field(default_factory=App)

