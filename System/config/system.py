from enum import Enum


class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    MATH = "mathfolder"
    PHYSICS = "physicsfolder"

    ALGEBRA = "algebrafolder"
    GEOMETRY = "geometryfolder"
    PROBSTATS = "probstatsfolder"

    ELECTROMAGNETICS = "electromagneticsfolder"
    MECHANICS = "mechanicsfolder"
    THERMODYNAMICS = "thermodynamicsfolder"


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

    FUNCTIONS = "functions"
    EQUATIONS = "equations"
    PROGRESSIONS = "progressions"
    VECTORS = "vectors"

    CIRCLES = "circles"
    PARALLELOGRAMS = "parallelograms"
    POLYGONS = "polygons"
    TRAPEZOIDS = "trapezoids"
    TRIANGLES = "triangles"

    ANSWER = "answer"


class FileExtenstions(Enum):
    HTML = "html"
    PY = "py"
    PNG = "png"


class DotenvServerKeys(Enum):
    APP_NAME = "APP_NAME"
    APP_HOST = "APP_HOST"
    APP_PORT = "APP_POST"
    APP_RELOAD = "APP_RELOAD"
