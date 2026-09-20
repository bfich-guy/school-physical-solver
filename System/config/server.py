from enum import Enum

from system.config.system import Folders, Files, FileExtenstions


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

    EQUATIONS = f"/{Files.EQUATIONS.value}"
    FUNCTIONS = f"/{Files.FUNCTIONS.value}"
    MEAN = f"/{Files.MEAN.value}"
    PROGRESSIONS = f"/{Files.PROGRESSIONS.value}"
    VECTORS = f"/{Files.VECTORS.value}"

    CIRCLES = f"/{Files.CIRCLES.value}"
    PARALLELOGRAMS = f"/{Files.PARALLELOGRAMS.value}"
    POLYGONS = f"/{Files.POLYGONS.value}"
    TRAPEZOIDS = f"/{Files.TRAPEZOIDS.value}"
    TRIANGLES = f"/{Files.TRIANGLES.value}"

    ELECTRICITY = f"/{Files.ELECTRICITY.value}"
    MAGNETISM = f"/{Files.MAGNETISM.value}"

    KINEMATICS = f"/{Files.KINEMATICS.value}"
    DYNAMICS = f"/{Files.DYNAMICS.value}"
    STATICS = f"/{Files.STATICS.value}"


class Templates(Enum):
    INDEX = f"{Files.INDEX.value}.{FileExtenstions.HTML.value}"

    USAGEPOLICY = f"{Folders.ABOUTUS.value}/{Files.USAGEPOLICY.value}.{FileExtenstions.HTML.value}"
    FAQ = f"{Folders.ABOUTUS.value}/{Files.FAQ.value}.{FileExtenstions.HTML.value}"
    EXTRAINFO = f"{Folders.ABOUTUS.value}/{Files.EXTRAINFO.value}.{FileExtenstions.HTML.value}"

    MATH = f"{Files.MATH.value}.{FileExtenstions.HTML.value}"
    PHYSICS = f"{Files.PHYSICS.value}.{FileExtenstions.HTML.value}"

    ALGEBRA = f"/{Folders.MATH.value}/{Files.ALGEBRA.value}.{FileExtenstions.HTML.value}"
    GEOMETRY = f"/{Folders.MATH.value}/{Files.GEOMETRY.value}.{FileExtenstions.HTML.value}"\

    ELECTROMAGNETICS = f"/{Folders.PHYSICS.value}/{Files.ELECTROMAGNETICS.value}.{FileExtenstions.HTML.value}"
    MECHANICS = f"/{Folders.PHYSICS.value}/{Files.MECHANICS.value}.{FileExtenstions.HTML.value}"
    THERMODYNAMICS = f"/{Folders.PHYSICS.value}/{Files.THERMODYNAMICS.value}.{FileExtenstions.HTML.value}"  

    EQUATIONS = f"/{Folders.MATH.value}/{Folders.ALGEBRA.value}/{Files.EQUATIONS.value}.{FileExtenstions.HTML.value}"
    FUNCTIONS = f"/{Folders.MATH.value}/{Folders.ALGEBRA.value}/{Files.FUNCTIONS.value}.{FileExtenstions.HTML.value}"
    MEAN = f"/{Folders.MATH.value}/{Folders.ALGEBRA.value}/{Files.MEAN.value}.{FileExtenstions.HTML.value}"
    PROGRESSIONS = f"/{Folders.MATH.value}/{Folders.ALGEBRA.value}/{Files.PROGRESSIONS.value}.{FileExtenstions.HTML.value}"
    VECTORS = f"/{Folders.MATH.value}/{Folders.ALGEBRA.value}/{Files.VECTORS.value}.{FileExtenstions.HTML.value}"

    CIRCLES = f"/{Folders.MATH.value}/{Folders.GEOMETRY.value}/{Files.CIRCLES.value}.{FileExtenstions.HTML.value}"
    PARALLELOGRAMS = f"/{Folders.MATH.value}/{Folders.GEOMETRY.value}/{Files.PARALLELOGRAMS.value}.{FileExtenstions.HTML.value}"
    POLYGONS = f"/{Folders.MATH.value}/{Folders.GEOMETRY.value}/{Files.POLYGONS.value}.{FileExtenstions.HTML.value}"
    TRAPEZOIDS = f"/{Folders.MATH.value}/{Folders.GEOMETRY.value}/{Files.TRAPEZOIDS.value}.{FileExtenstions.HTML.value}"
    TRIANGLES = f"/{Folders.MATH.value}/{Folders.GEOMETRY.value}/{Files.TRIANGLES.value}.{FileExtenstions.HTML.value}"

    ELECTRICITY = f"/{Folders.PHYSICS.value}/{Folders.ELECTROMAGNETICS.value}/{Files.ELECTRICITY.value}.{FileExtenstions.HTML.value}"
    MAGNETISM = f"/{Folders.PHYSICS.value}/{Folders.ELECTROMAGNETICS.value}/{Files.MAGNETISM.value}.{FileExtenstions.HTML.value}"

    KINEMATICS = f"/{Folders.PHYSICS.value}/{Folders.MECHANICS.value}/{Files.KINEMATICS.value}.{FileExtenstions.HTML.value}"
    DYNAMICS = f"/{Folders.PHYSICS.value}/{Folders.MECHANICS.value}/{Files.DYNAMICS.value}.{FileExtenstions.HTML.value}"
    STATICS = f"/{Folders.PHYSICS.value}/{Folders.MECHANICS.value}/{Files.STATICS.value}.{FileExtenstions.HTML.value}"
