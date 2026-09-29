from enum import Enum
from decimal import Decimal


#region System

class Folders(Enum):
    TEMPLATES = "templates"
    STATIC = "static"

    ABOUTUS = "aboutusfolder"

    MATH = "mathfolder"
    PHYSICS = "physicsfolder"

    ALGEBRA = "algebrafolder"
    GEOMETRY = "geometryfolder"

    ELECTROMAGNETICS = "electromagneticsfolder"
    MECHANICS = "mechanicsfolder"
    THERMODYNAMICS = "thermodynamicsfolder"


class Files(Enum):
    INDEX = "index"
    ANSWER = "answer"

    USAGEPOLICY = "usagepolicy"
    FAQ = "faq"
    EXTRAINFO = "extrainfo"

    MATH = "math"
    PHYSICS = "physics"

    ALGEBRA = "algebra"
    GEOMETRY = "geometry"

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

#endregion


#region Server

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
    ANSWER = f"/{Files.ANSWER.value}"

    USAGEPOLICY = f"/{Files.USAGEPOLICY.value}"
    FAQ = f"/{Files.FAQ.value}"
    EXTRAINFO = f"/{Files.EXTRAINFO.value}"

    MATH = f"/{Files.MATH.value}"
    PHYSICS = f"/{Files.PHYSICS.value}"

    ALGEBRA = f"/{Files.ALGEBRA.value}"
    GEOMETRY = f"/{Files.GEOMETRY.value}"

    ELECTROMAGNETICS = f"/{Files.ELECTROMAGNETICS.value}"
    MECHANICS = f"/{Files.MECHANICS.value}"
    THERMODYNAMICS = f"/{Files.THERMODYNAMICS.value}"


class Templates(Enum):
    INDEX = f"{Files.INDEX.value}.{FileExtenstions.HTML.value}"
    ANSWER = f"{Files.ANSWER.value}.{FileExtenstions.HTML.value}"

    USAGEPOLICY = f"{Folders.ABOUTUS.value}/{Files.USAGEPOLICY.value}.{FileExtenstions.HTML.value}"
    FAQ = f"{Folders.ABOUTUS.value}/{Files.FAQ.value}.{FileExtenstions.HTML.value}"
    EXTRAINFO = f"{Folders.ABOUTUS.value}/{Files.EXTRAINFO.value}.{FileExtenstions.HTML.value}"

    MATH = f"{Files.MATH.value}.{FileExtenstions.HTML.value}"
    PHYSICS = f"{Files.PHYSICS.value}.{FileExtenstions.HTML.value}"

    ALGEBRA = f"/{Folders.MATH.value}/{Files.ALGEBRA.value}.{FileExtenstions.HTML.value}"
    GEOMETRY = f"/{Folders.MATH.value}/{Files.GEOMETRY.value}.{FileExtenstions.HTML.value}"

    ELECTROMAGNETICS = f"/{Folders.PHYSICS.value}/{Files.ELECTROMAGNETICS.value}.{FileExtenstions.HTML.value}"
    MECHANICS = f"/{Folders.PHYSICS.value}/{Files.MECHANICS.value}.{FileExtenstions.HTML.value}"
    THERMODYNAMICS = f"/{Folders.PHYSICS.value}/{Files.THERMODYNAMICS.value}.{FileExtenstions.HTML.value}" 

#endregion


#region Constants

class PhysMathConstants(Enum):
    EARTH_GRAVITY_ACCELERATION = Decimal("9.81")
    GAS_CONSTANT = Decimal("8.31446261815324")
    COULOMB_CONSTANT = Decimal("8987551792.3")


class SystemConstants(Enum):
    USER_INPUT_MAX_LENGTH = 64


user_input_error_message: str = (
    "К сожалению, Ваш ввод оказался недействительным для Физмат-калькулятора." 
    f"Проверьте, что Ваш ввод не больше {SystemConstants.USER_INPUT_MAX_LENGTH.value} символов."
    "Так же рекомендуем убедиться, что Вы ввели хотя бы одно число в поле формулы."
)

calculations_error_message: str = (
    "Увы, но Физмат-калькулятор заметил математические ошибки в Вашем вводе. "
    "Проверьте, чтобы в Вашем следующем вводе не содержалось деление на ноль или отрицательных корней. "
)

#endregion
