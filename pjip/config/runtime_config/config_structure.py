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
    logging: Logging = field(default_factory=Logging)
    process: Process = field(default_factory=Process)
    ui: UI = field(default_factory=UI)
    features: Features = field(default_factory=Features)
    debug: Debug = field(default_factory=Debug)

