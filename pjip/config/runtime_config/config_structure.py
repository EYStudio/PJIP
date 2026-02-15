from dataclasses import dataclass, field

from .config_enums import KillMethod


@dataclass
class Update:
    auto_get_update: bool = True
    auto_download_update: bool = False
    # extended_update_urls: list[str] = field(default_factory=lambda: ["a"])
    extended_update_urls: list = field(default_factory=list)

@dataclass
class App:
    # first_use: bool = False
    update: Update = field(default_factory=Update)

@dataclass
class Logging:
    enable_log_output: bool = True

@dataclass
class Process:
    kill_method: KillMethod = KillMethod.DEFAULT

@dataclass
class UI:
    pass

@dataclass
class Features:
    pass

@dataclass
class Debug:
    debug: bool = False
    advanced_module: bool = False

@dataclass
class ConfigRoot:
    app: App = field(default_factory=App)
    logging: Logging = field(default_factory=Logging)
    process: Process = field(default_factory=Process)
    ui: UI = field(default_factory=UI)
    features: Features = field(default_factory=Features)
    debug: Debug = field(default_factory=Debug)

