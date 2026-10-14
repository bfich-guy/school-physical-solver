from enum import Enum
from pydantic import BaseModel


#region System

class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    ABOUTUS = "aboutus"

    MATH = "math"
    PHYSICS = "physics"

    ALGEBRA = "algebra"
    GEOMETRY = "geometry"

    ELECTROMAGNETICS = "electromagnetics"
    MECHANICS = "mechanics"
    THERMODYNAMICS = "thermodynamics"


class Files(Enum):
    INDEX = "index"
    ABOUTUS = "aboutus"

    MATH = "math"
    PHYSICS = "physics"

    ALGEBRA = "algebra"
    GEOMETRY = "geometry"

    ELECTROMAGNETICS = "electromagnetics"
    MECHANICS = "mechanics"
    THERMODYNAMICS = "thermodynamics"

    CALCULATE = "calculate"


class FileExtenstions(Enum):
    HTML = "html"


class DotenvServerKeys(Enum):
    APP_NAME = "APP_NAME"
    APP_HOST = "APP_HOST"
    APP_PORT = "APP_POST"
    APP_RELOAD = "APP_RELOAD"

#endregion


#region Server

origins: list[str] = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "https://school-physmath-solver.vercel.app",
]


class Mounts(Enum):
    STATIC = f"/{Folders.STATIC.value}"    


class Prefix(Enum):
    INDEX = ""

    MATH = f"/{Files.MATH.value}"
    PHYSICS = f"/{Files.PHYSICS.value}"

    ALGEBRA = f"/{Files.MATH.value}/{Files.ALGEBRA.value}"
    GEOMETRY = f"/{Files.MATH.value}/{Files.GEOMETRY.value}"

    ELECTROMAGNETICS = f"/{Files.PHYSICS.value}/{Files.ELECTROMAGNETICS.value}"
    MECHANICS = f"/{Files.PHYSICS.value}/{Files.MECHANICS.value}"
    THERMODYNAMICS = f"/{Files.PHYSICS.value}/{Files.THERMODYNAMICS.value}"


class Endpoints(Enum):
    INDEX = f"/"
    ABOUTUS = f"/{Files.ABOUTUS.value}"
    CALCULATE = f"/{Files.CALCULATE.value}"

    MATH = f"/{Files.MATH.value}"
    PHYSICS = f"/{Files.PHYSICS.value}"

    ALGEBRA = f"/{Files.ALGEBRA.value}"
    GEOMETRY = f"/{Files.GEOMETRY.value}"

    ELECTROMAGNETICS = f"/{Files.ELECTROMAGNETICS.value}"
    MECHANICS = f"/{Files.MECHANICS.value}"
    THERMODYNAMICS = f"/{Files.THERMODYNAMICS.value}"


class Templates(Enum):
    INDEX = f"{Files.INDEX.value}.{FileExtenstions.HTML.value}"
    ABOUTUS = f"{Files.ABOUTUS.value}.{FileExtenstions.HTML.value}"

    MATH = f"{Files.MATH.value}.{FileExtenstions.HTML.value}"
    PHYSICS = f"{Files.PHYSICS.value}.{FileExtenstions.HTML.value}"

    ALGEBRA = f"/{Folders.MATH.value}/{Files.ALGEBRA.value}.{FileExtenstions.HTML.value}"
    GEOMETRY = f"/{Folders.MATH.value}/{Files.GEOMETRY.value}.{FileExtenstions.HTML.value}"

    ELECTROMAGNETICS = f"/{Folders.PHYSICS.value}/{Files.ELECTROMAGNETICS.value}.{FileExtenstions.HTML.value}"
    MECHANICS = f"/{Folders.PHYSICS.value}/{Files.MECHANICS.value}.{FileExtenstions.HTML.value}"
    THERMODYNAMICS = f"/{Folders.PHYSICS.value}/{Files.THERMODYNAMICS.value}.{FileExtenstions.HTML.value}" 

#endregion


#region General constants

class ErrorMessages(Enum):
    USER_INPUT = (
        "Некорректный ввод"
    )
    CALCULATIONS = (
        "Математические ошибки"
    )
    UNKNOWN_FORMULA = (
        "Неизвестная формула"
    )
    TECHNICAL = (
        "Техническая ошибка"
    )


class InputMethod(Enum):
    SCALAR = "scalar"
    VECTOR = "vector"


class CalculationSchema(BaseModel):
    formula: list[str]
    quantities: dict

#endregion
