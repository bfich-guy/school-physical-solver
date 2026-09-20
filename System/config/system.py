from enum import Enum


class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    ABOUTUS = "aboutusfolder"

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

    USAGEPOLICY = "usagepolicy"
    FAQ = "faq"
    EXTRAINFO = "extrainfo"

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
    MEAN = "mean"
    PROGRESSIONS = "progressions"
    VECTORS = "vectors"

    CIRCLES = "circles"
    PARALLELOGRAMS = "parallelograms"
    POLYGONS = "polygons"
    TRAPEZOIDS = "trapezoids"
    TRIANGLES = "triangles"

    ELECTRICITY = "electricity"
    MAGNETISM = "magnetism"

    KINEMATICS = "kinematics"
    DYNAMICS = "dynamics"
    STATICS = "statics"

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
