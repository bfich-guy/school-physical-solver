from enum import Enum


class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    MATH = "math"
    PHYSICS = "physics"

    ALGEBRA = "algebra"
    GEOMETRY = "/geometry"
    PROBSTATS = "probstats"

    ELECTROMAGNETICS = "electromagnetics"
    ALGEMECHANICSBRA = "mechanics"
    THERMODYNAMICS = "thermodynamics"


class Files(Enum):
    INDEX = "index"
    ABOUTUS = "aboutus"

    MATH = "math"
    PHYSICS = "physics"

    ALGEBRA = "algebra"
    GEOMETRY = "geometry"
    PROBSTATS = "probstats"

    ELECTROMAGNETICS = "electromagnetics"
    MECHANICS = "mechanics"
    THERMODYNAMICS = "thermodynamics"


class FileExtenstions(Enum):
    HTML = "html"
    PY = "py"
    PNG = "png"


class DotenvServerKeys(Enum):
    APP_NAME = "APP_NAME"
    APP_HOST = "APP_HOST"
    APP_PORT = "APP_POST"
    APP_RELOAD = "APP_RELOAD"
