export const calculateEndpoint = "/calculate";


export const FormulasData = {
    "linear-equation-x-button": {
        "input": {
            "linear-equation-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "linear-equation-b-input": {
                "name": "b",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "linear-equation-answer-output",
        },
        "formula": [
            "LinearEquation", "get_x",
        ],
    },
    "quadratic-equation-x-button": {
        "input": {
            "quadratic-equation-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "quadratic-equation-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "quadratic-equation-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "quadratic-equation-answer-output",
        },
        "formula": [
            "QuadraticEquation", "get_x",
        ],
    },
    "linear-function-y-button": {
        "input": {
            "linear-function-k-input": {
                "name": "k",
                "mode": "scalar",
            },
            "linear-function-x-input": {
                "name": "x",
                "mode": "scalar",
            },
            "linear-function-b-input": {
                "name": "b",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "linear-function-answer-output",
        },
        "formula": [
            "LinearFunction", "get_y",
        ],
    },
    "linear-function-k-button": {
        "input": {
            "linear-function-y-input": {
                "name": "y",
                "mode": "scalar",
            },
            "linear-function-x-input": {
                "name": "x",
                "mode": "scalar",
            },
            "linear-function-b-input": {
                "name": "b",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "linear-function-answer-output",
        },
        "formula": [
            "LinearFunction", "get_k",
        ],
    },
    "linear-function-b-button": {
        "input": {
            "linear-function-y-input": {
                "name": "y",
                "mode": "scalar",
            },
            "linear-function-k-input": {
                "name": "k",
                "mode": "scalar",
            },
            "linear-function-x-input": {
                "name": "x",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "linear-function-answer-output",
        },
        "formula": [
            "LinearFunction", "get_b",
        ],
    },
    "quadratic-function-y-button": {
        "input": {
            "quadratic-function-x-input": {
                "name": "x",
                "mode": "scalar",
            },
            "quadratic-function-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "quadratic-function-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "quadratic-function-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "quadratic-function-answer-output",
        },
        "formula": [
            "QuadraticFunction", "get_y",
        ],
    },
    "quadratic-function-a-button": {
        "input": {
            "quadratic-function-y-input": {
                "name": "y",
                "mode": "scalar",
            },
            "quadratic-function-x-input": {
                "name": "x",
                "mode": "scalar",
            },
            "quadratic-function-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "quadratic-function-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "quadratic-function-answer-output",
        },
        "formula": [
            "QuadraticFunction", "get_a",
        ],
    },
    "quadratic-function-b-button": {
        "input": {
            "quadratic-function-y-input": {
                "name": "y",
                "mode": "scalar",
            },
            "quadratic-function-x-input": {
                "name": "x",
                "mode": "scalar",
            },
            "quadratic-function-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "quadratic-function-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "quadratic-function-answer-output",
        },
        "formula": [
            "QuadraticFunction", "get_b",
        ],
    },
    "quadratic-function-c-button": {
        "input": {
            "quadratic-function-y-input": {
                "name": "y",
                "mode": "scalar",
            },
            "quadratic-function-x-input": {
                "name": "x",
                "mode": "scalar",
            },
            "quadratic-function-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "quadratic-function-b-input": {
                "name": "b",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "quadratic-function-answer-output",
        },
        "formula": [
            "QuadraticFunction", "get_c",
        ],
    },
    "arithmetic-progression-sum-theorem-S-button": {
        "input": {
            "arithmetic-progression-sum-theorem-a1-input": {
                "name": "a1",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-an-input": {
                "name": "an",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-n-input": {
                "name": "n",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-sum-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionSumTheorem", "get_S",
        ],
    },
    "arithmetic-progression-sum-theorem-a1-button": {
        "input": {
            "arithmetic-progression-sum-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-an-input": {
                "name": "an",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-n-input": {
                "name": "n",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-sum-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionSumTheorem", "get_a1",
        ],
    },
    "arithmetic-progression-sum-theorem-an-button": {
        "input": {
            "arithmetic-progression-sum-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-a1-input": {
                "name": "a1",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-n-input": {
                "name": "n",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-sum-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionSumTheorem", "get_an",
        ],
    },
    "arithmetic-progression-sum-theorem-n-button": {
        "input": {
            "arithmetic-progression-sum-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-a1-input": {
                "name": "a1",
                "mode": "scalar",
            },
            "arithmetic-progression-sum-theorem-an-input": {
                "name": "an",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-sum-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionSumTheorem", "get_n",
        ],
    },
    "geometric-progression-sum-theorem-S-button": {
       "input": {
            "geometric-progression-sum-theorem-b1-input": {
                "name": "b1",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-bn-input": {
                "name": "bn",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-q-input": {
                "name": "q",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "geometric-progression-sum-theorem-answer-output",
        },
        "formula": [
            "GeometricProgressionSumTheorem", "get_S",
        ],
    },
    "geometric-progression-sum-theorem-b1-button": {
       "input": {
            "geometric-progression-sum-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-bn-input": {
                "name": "bn",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-q-input": {
                "name": "q",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "geometric-progression-sum-theorem-answer-output",
        },
        "formula": [
            "GeometricProgressionSumTheorem", "get_b1",
        ],
    },
    "geometric-progression-sum-theorem-bn-button": {
       "input": {
            "geometric-progression-sum-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-b1-input": {
                "name": "b1",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-q-input": {
                "name": "q",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "geometric-progression-sum-theorem-answer-output",
        },
        "formula": [
            "GeometricProgressionSumTheorem", "get_bn",
        ],
    },
    "geometric-progression-sum-theorem-q-button": {
       "input": {
            "geometric-progression-sum-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-b1-input": {
                "name": "b1",
                "mode": "scalar",
            },
            "geometric-progression-sum-theorem-bn-input": {
                "name": "bn",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "geometric-progression-sum-theorem-answer-output",
        },
        "formula": [
            "GeometricProgressionSumTheorem", "get_q",
        ],
    },
    "arithmetic-progression-term-theorem-an-button": {
        "input": {
            "arithmetic-progression-term-theorem-a1-input": {
                "name": "a1",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-d-input": {
                "name": "d",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-n-input": {
                "name": "n",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-term-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionTermTheorem", "get_an",
        ],
    },
    "arithmetic-progression-term-theorem-a1-button": {
        "input": {
            "arithmetic-progression-term-theorem-an-input": {
                "name": "an",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-d-input": {
                "name": "d",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-n-input": {
                "name": "n",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-term-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionTermTheorem", "get_a1",
        ],
    },
    "arithmetic-progression-term-theorem-d-button": {
        "input": {
            "arithmetic-progression-term-theorem-an-input": {
                "name": "an",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-a1-input": {
                "name": "a1",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-n-input": {
                "name": "n",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-term-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionTermTheorem", "get_d",
        ],
    },
    "arithmetic-progression-term-theorem-n-button": {
        "input": {
            "arithmetic-progression-term-theorem-an-input": {
                "name": "an",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-a1-input": {
                "name": "a1",
                "mode": "scalar",
            },
            "arithmetic-progression-term-theorem-d-input": {
                "name": "d",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "arithmetic-progression-term-theorem-answer-output",
        },
        "formula": [
            "ArithmeticProgressionTermTheorem", "get_n",
        ],
    },
    "vector-coordinates-theorem-a-button": {
        "input": {
            "vector-coordinates-theorem-A-input": {
                "name": "A",
                "mode": "vector",
            },
            "vector-coordinates-theorem-B-input": {
                "name": "B",
                "mode": "vector",
            },
        },
        "output": {
            "id": "vector-coordinates-theorem-answer-output",
        },
        "formula": [
            "VectorCoordinatesTheorem", "get_a",
        ],
    },
    "vector-coordinates-theorem-A-button": {
        "input": {
            "vector-coordinates-theorem-a-input": {
                "name": "a",
                "mode": "vector",
            },
            "vector-coordinates-theorem-B-input": {
                "name": "B",
                "mode": "vector",
            },
        },
        "output": {
            "id": "vector-coordinates-theorem-answer-output",
        },
        "formula": [
            "VectorCoordinatesTheorem", "get_A",
        ],
    },
    "vector-coordinates-theorem-B-button": {
        "input": {
            "vector-coordinates-theorem-a-input": {
                "name": "a",
                "mode": "vector",
            },
            "vector-coordinates-theorem-A-input": {
                "name": "A",
                "mode": "vector",
            },
        },
        "output": {
            "id": "vector-coordinates-theorem-answer-output",
        },
        "formula": [
            "VectorCoordinatesTheorem", "get_B",
        ],
    },
    "vector-magnitude-theorem-la-button": {
        "input": {
            "vector-magnitude-theorem-a-input": {
                "name": "a",
                "mode": "vector",
            },
        },
        "output": {
            "id": "vector-magnitude-theorem-answer-output",
        },
        "formula": [
            "VectorMagnitudeTheorem", "get_la",
        ],
    },
    "vector-dot-product-theorem-ab-button": {
        "input": {
            "vector-dot-product-theorem-a-input": {
                "name": "a",
                "mode": "vector",
            },
            "vector-dot-product-theorem-b-input": {
                "name": "b",
                "mode": "vector",
            },
        },
        "output": {
            "id": "vector-dot-product-theorem-answer-output",
        },
        "formula": [
            "VectorDotProductTheorem", "get_ab",
        ],
    },
    "vector-angle-cosinus-theorem-cosa-button": {
        "input": {
            "vector-angle-cosinus-theorem-ab-input": {
                "name": "ab",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-la-input": {
                "name": "la",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-lb-input": {
                "name": "lb",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vector-angle-cosinus-theorem-answer-output",
        },
        "formula": [
            "VectorAngleCosinusTheorem", "get_cosa",
        ],
    },
    "vector-angle-cosinus-theorem-ab-button": {
        "input": {
            "vector-angle-cosinus-theorem-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-la-input": {
                "name": "la",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-lb-input": {
                "name": "lb",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vector-angle-cosinus-theorem-answer-output",
        },
        "formula": [
            "VectorAngleCosinusTheorem", "get_ab",
        ],
    },
    "vector-angle-cosinus-theorem-la-button": {
        "input": {
            "vector-angle-cosinus-theorem-ab-input": {
                "name": "ab",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-lb-input": {
                "name": "lb",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vector-angle-cosinus-theorem-answer-output",
        },
        "formula": [
            "VectorAngleCosinusTheorem", "get_la",
        ],
    },
    "vector-angle-cosinus-theorem-lb-button": {
        "input": {
            "vector-angle-cosinus-theorem-ab-input": {
                "name": "ab",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
            "vector-angle-cosinus-theorem-la-input": {
                "name": "la",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vector-angle-cosinus-theorem-answer-output",
        },
        "formula": [
            "VectorAngleCosinusTheorem", "get_lb",
        ],
    },
    "vector-scaling-theorem-b-button": {
        "input": {
            "vector-scaling-theorem-a-input": {
                "name": "a",
                "mode": "vector",
            },
            "vector-scaling-theorem-k-input": {
                "name": "k",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vector-scaling-theorem-answer-output",
        },
        "formula": [
            "VectorScalingTheorem", "get_b",
        ],
    },
    "circle-area-theorem-S-button": {
        "input": {
            "circle-area-theorem-pi-input": {
                "name": "pi",
                "mode": "scalar",
            },
            "circle-area-theorem-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "circle-area-theorem-answer-output",
        },
        "formula": [
            "CircleAreaTheorem", "get_S",
        ],
    },
    "circle-area-theorem-r-button": {
        "input": {
            "circle-area-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "circle-area-theorem-pi-input": {
                "name": "pi",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "circle-area-theorem-answer-output",
        },
        "formula": [
            "CircleAreaTheorem", "get_r",
        ],
    },
    "circumference-theorem-l-button": {
        "input": {
            "circumference-theorem-pi-input": {
                "name": "pi",
                "mode": "scalar",
            },
            "circumference-theorem-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "circumference-theorem-answer-output",
        },
        "formula": [
            "CircumferenceTheorem", "get_l",
        ],
    },
    "circumference-theorem-r-button": {
        "input": {
            "circumference-theorem-l-input": {
                "name": "l",
                "mode": "scalar",
            },
            "circumference-theorem-pi-input": {
                "name": "pi",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "circumference-theorem-answer-output",
        },
        "formula": [
            "CircumferenceTheorem", "get_r",
        ],
    },
    "parallelogram-area-by-base-and-height-theorem-S-button": {
        "input": {
            "parallelogram-area-by-base-and-height-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "parallelogram-area-by-base-and-height-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "parallelogram-area-by-base-and-height-theorem-answer-output",
        },
        "formula": [
            "ParallelogramAreaByBaseAndHeightTheorem", "get_S",
        ],
    },
    "parallelogram-area-by-base-and-height-theorem-a-button": {
        "input": {
            "parallelogram-area-by-base-and-height-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "parallelogram-area-by-base-and-height-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "parallelogram-area-by-base-and-height-theorem-answer-output",
        },
        "formula": [
            "ParallelogramAreaByBaseAndHeightTheorem", "get_a",
        ],
    },
    "parallelogram-area-by-base-and-height-theorem-h-button": {
        "input": {
            "parallelogram-area-by-base-and-height-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "parallelogram-area-by-base-and-height-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "parallelogram-area-by-base-and-height-theorem-answer-output",
        },
        "formula": [
            "ParallelogramAreaByBaseAndHeightTheorem", "get_h",
        ],
    },
    "trapezoid-midline-theorem-m-button": {
        "input": {
            "trapezoid-midline-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "trapezoid-midline-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trapezoid-midline-theorem-answer-output",
        },
        "formula": [
            "TrapezoidMidlineTheorem", "get_m",
        ],
    },
    "trapezoid-midline-theorem-a-button": {
        "input": {
            "trapezoid-midline-theorem-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "trapezoid-midline-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trapezoid-midline-theorem-answer-output",
        },
        "formula": [
            "TrapezoidMidlineTheorem", "get_a",
        ],
    },
    "trapezoid-midline-theorem-b-button": {
        "input": {
            "trapezoid-midline-theorem-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "trapezoid-midline-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trapezoid-midline-theorem-answer-output",
        },
        "formula": [
            "TrapezoidMidlineTheorem", "get_b",
        ],
    },
    "trapezoid-area-by-midline-and-height-theorem-S-button": {
        "input": {
            "trapezoid-area-by-midline-and-height-theorem-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "trapezoid-area-by-midline-and-height-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trapezoid-area-by-midline-and-height-theorem-answer-output",
        },
        "formula": [
            "TrapezoidAreaByMidlineAndHeightTheorem", "get_S",
        ],
    },
    "trapezoid-area-by-midline-and-height-theorem-m-button": {
        "input": {
            "trapezoid-area-by-midline-and-height-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "trapezoid-area-by-midline-and-height-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trapezoid-area-by-midline-and-height-theorem-answer-output",
        },
        "formula": [
            "TrapezoidAreaByMidlineAndHeightTheorem", "get_m",
        ],
    },
    "trapezoid-area-by-midline-and-height-theorem-h-button": {
        "input": {
            "trapezoid-area-by-midline-and-height-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "trapezoid-area-by-midline-and-height-theorem-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trapezoid-area-by-midline-and-height-theorem-answer-output",
        },
        "formula": [
            "TrapezoidAreaByMidlineAndHeightTheorem", "get_h",
        ],
    },
    "triangle-area-by-base-and-height-theorem-S-button": {
        "input": {
            "triangle-area-by-base-and-height-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "triangle-area-by-base-and-height-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-base-and-height-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByBaseAndHeightTheorem", "get_S",
        ],
    },
    "triangle-area-by-base-and-height-theorem-a-button": {
        "input": {
            "triangle-area-by-base-and-height-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "triangle-area-by-base-and-height-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-base-and-height-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByBaseAndHeightTheorem", "get_a",
        ],
    },
    "heron-theorem-S-button": {
        "input": {
            "heron-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "heron-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "heron-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "heron-theorem-answer-output",
        },
        "formula": [
            "HeronTheorem", "get_S",
        ],
    },
    "cosine-theorem-a-button": {
        "input": {
            "cosine-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "cosine-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "cosine-theorem-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "cosine-theorem-answer-output",
        },
        "formula": [
            "CosineTheorem", "get_a",
        ],
    },
    "cosine-theorem-b-button": {
        "input": {
            "cosine-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "cosine-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "cosine-theorem-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "cosine-theorem-answer-output",
        },
        "formula": [
            "CosineTheorem", "get_b",
        ],
    },
    "cosine-theorem-c-button": {
        "input": {
            "cosine-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "cosine-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "cosine-theorem-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "cosine-theorem-answer-output",
        },
        "formula": [
            "CosineTheorem", "get_c",
        ],
    },
    "cosine-theorem-cosa-button": {
        "input": {
            "cosine-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "cosine-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "cosine-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "cosine-theorem-answer-output",
        },
        "formula": [
            "CosineTheorem", "get_cosa",
        ],
    },
    "sine-theorem-a-button": {
        "input": {
            "sine-theorem-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
            "sine-theorem-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "sine-theorem-answer-output",
        },
        "formula": [
            "SineTheorem", "get_a",
        ],
    },
    "sine-theorem-sina-button": {
        "input": {
            "sine-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "sine-theorem-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "sine-theorem-answer-output",
        },
        "formula": [
            "SineTheorem", "get_sina",
        ],
    },
    "sine-theorem-R-button": {
        "input": {
            "sine-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "sine-theorem-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "sine-theorem-answer-output",
        },
        "formula": [
            "SineTheorem", "get_R",
        ],
    },
    "pythagorean-theorem-a-button": {
        "input": {
            "pythagorean-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "pythagorean-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "pythagorean-theorem-answer-output",
        },
        "formula": [
            "PythagoreanTheorem", "get_a",
        ],
    },
    "pythagorean-theorem-b-button": {
        "input": {
            "pythagorean-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "pythagorean-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "pythagorean-theorem-answer-output",
        },
        "formula": [
            "PythagoreanTheorem", "get_b",
        ],
    },
    "pythagorean-theorem-c-button": {
        "input": {
            "pythagorean-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "pythagorean-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "pythagorean-theorem-answer-output",
        },
        "formula": [
            "PythagoreanTheorem", "get_c",
        ],
    },
    "triangle-area-by-inscribed-circle-theorem-S-button": {
        "input": {
            "triangle-area-by-inscribed-circle-theorem-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "triangle-area-by-inscribed-circle-theorem-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-inscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByInscribedCircleTheorem", "get_S",
        ],
    },
    "triangle-area-by-inscribed-circle-theorem-p-button": {
        "input": {
            "triangle-area-by-inscribed-circle-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "triangle-area-by-inscribed-circle-theorem-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-inscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByInscribedCircleTheorem", "get_p",
        ],
    },
    "triangle-area-by-inscribed-circle-theorem-r-button": {
        "input": {
            "triangle-area-by-inscribed-circle-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "triangle-area-by-inscribed-circle-theorem-p-input": {
                "name": "p",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-inscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByInscribedCircleTheorem", "get_r",
        ],
    },
    "triangle-area-by-circumscribed-circle-theorem-S-button": {
        "input": {
            "triangle-area-by-circumscribed-circle-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-circumscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByCircumscripedCircleTheorem", "get_S",
        ],
    },
    "triangle-area-by-circumscribed-circle-theorem-a-button": {
        "input": {
            "triangle-area-by-circumscribed-circle-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-circumscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByCircumscripedCircleTheorem", "get_a",
        ],
    },
    "triangle-area-by-circumscribed-circle-theorem-b-button": {
        "input": {
            "triangle-area-by-circumscribed-circle-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-circumscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByCircumscripedCircleTheorem", "get_b",
        ],
    },
    "triangle-area-by-circumscribed-circle-theorem-c-button": {
        "input": {
            "triangle-area-by-circumscribed-circle-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-circumscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByCircumscripedCircleTheorem", "get_c",
        ],
    },
    "triangle-area-by-circumscribed-circle-theorem-R-button": {
        "input": {
            "triangle-area-by-circumscribed-circle-theorem-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-b-input": {
                "name": "b",
                "mode": "scalar",
            },
            "triangle-area-by-circumscribed-circle-theorem-c-input": {
                "name": "c",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-area-by-circumscribed-circle-theorem-answer-output",
        },
        "formula": [
            "TriangleAreaByCircumscripedCircleTheorem", "get_R",
        ],
    },
    "triangle-side-projection-theorem-h-button": {
        "input": {
            "triangle-side-projection-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "triangle-side-projection-theorem-cossina-input": {
                "name": "cossina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-side-projection-theorem-answer-output",
        },
        "formula": [
            "TriangleSideProjectionTheorem", "get_h",
        ],
    },
    "triangle-side-projection-theorem-a-button": {
        "input": {
            "triangle-side-projection-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
            "triangle-side-projection-theorem-cossina-input": {
                "name": "cossina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-side-projection-theorem-answer-output",
        },
        "formula": [
            "TriangleSideProjectionTheorem", "get_a",
        ],
    },
    "triangle-side-projection-theorem-cossina-button": {
        "input": {
            "triangle-side-projection-theorem-h-input": {
                "name": "h",
                "mode": "scalar",
            },
            "triangle-side-projection-theorem-a-input": {
                "name": "a",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "triangle-side-projection-theorem-answer-output",
        },
        "formula": [
            "TriangleSideProjectionTheorem", "get_cossina",
        ],
    },
    "figure-area-by-similarity-coefficient-theorem-S2-button": {
        "input": {
            "figure-area-by-similarity-coefficient-theorem-S1-input": {
                "name": "S1",
                "mode": "scalar",
            },
            "figure-area-by-similarity-coefficient-theorem-k-input": {
                "name": "k",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "figure-area-by-similarity-coefficient-theorem-answer-output",
        },
        "formula": [
            "FigureAreaBySimilarityCoefficientTheorem", "get_S2",
        ],
    },
    "figure-area-by-similarity-coefficient-theorem-S1-button": {
        "input": {
            "figure-area-by-similarity-coefficient-theorem-S2-input": {
                "name": "S2",
                "mode": "scalar",
            },
            "figure-area-by-similarity-coefficient-theorem-k-input": {
                "name": "k",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "figure-area-by-similarity-coefficient-theorem-answer-output",
        },
        "formula": [
            "FigureAreaBySimilarityCoefficientTheorem", "get_S1",
        ],
    },
    "figure-area-by-similarity-coefficient-theorem-k-button": {
        "input": {
            "figure-area-by-similarity-coefficient-theorem-S2-input": {
                "name": "S2",
                "mode": "scalar",
            },
            "figure-area-by-similarity-coefficient-theorem-S1-input": {
                "name": "S1",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "figure-area-by-similarity-coefficient-theorem-answer-output",
        },
        "formula": [
            "FigureAreaBySimilarityCoefficientTheorem", "get_k",
        ],
    },
    "ohms-specific-law-U-button": {
        "input": {
            "ohms-specific-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
            "ohms-specific-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "ohms-specific-law-answer-output",
        },
        "formula": [
            "OhmsSpecificLaw", "get_U",
        ],
    },
    "ohms-specific-law-I-button": {
        "input": {
            "ohms-specific-law-U-input": {
                "name": "U",
                "mode": "scalar",
            },
            "ohms-specific-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "ohms-specific-law-answer-output",
        },
        "formula": [
            "OhmsSpecificLaw", "get_I",
        ],
    },
    "ohms-specific-law-R-button": {
        "input": {
            "ohms-specific-law-U-input": {
                "name": "U",
                "mode": "scalar",
            },
            "ohms-specific-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "ohms-specific-law-answer-output",
        },
        "formula": [
            "OhmsSpecificLaw", "get_R",
        ],
    },
    "ohms-full-law-E-button": {
        "input": {
            "ohms-full-law-U-input": {
                "name": "U",
                "mode": "scalar",
            },
            "ohms-full-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
            "ohms-full-law-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "ohms-full-law-answer-output",
        },
        "formula": [
            "OhmsFullLaw", "get_E",
        ],
    },
    "ohms-full-law-U-button": {
        "input": {
            "ohms-full-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "ohms-full-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
            "ohms-full-law-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "ohms-full-law-answer-output",
        },
        "formula": [
            "OhmsFullLaw", "get_U",
        ],
    },
    "ohms-full-law-I-button": {
        "input": {
            "ohms-full-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "ohms-full-law-U-input": {
                "name": "U",
                "mode": "scalar",
            },
            "ohms-full-law-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "ohms-full-law-answer-output",
        },
        "formula": [
            "OhmsFullLaw", "get_I",
        ],
    },
    "ohms-full-law-r-button": {
        "input": {
            "ohms-full-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "ohms-full-law-U-input": {
                "name": "U",
                "mode": "scalar",
            },
            "ohms-full-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "ohms-full-law-answer-output",
        },
        "formula": [
            "OhmsFullLaw", "get_r",
        ],
    },
    "watts-law-P-button": {
        "input": {
            "watts-law-U-input": {
                "name": "U",
                "mode": "scalar",
            },
            "watts-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "watts-law-answer-output",
        },
        "formula": [
            "WattsLaw", "get_P",
        ],
    },
    "watts-law-U-button": {
        "input": {
            "watts-law-P-input": {
                "name": "P",
                "mode": "scalar",
            },
            "watts-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "watts-law-answer-output",
        },
        "formula": [
            "WattsLaw", "get_U",
        ],
    },
    "watts-law-I-button": {
        "input": {
            "watts-law-P-input": {
                "name": "P",
                "mode": "scalar",
            },
            "watts-law-U-input": {
                "name": "U",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "watts-law-answer-output",
        },
        "formula": [
            "WattsLaw", "get_I",
        ],
    },
    "joule-lenz-law-Q-button": {
        "input": {
            "joule-lenz-law-P-input": {
                "name": "P",
                "mode": "scalar",
            },
            "joule-lenz-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "joule-lenz-law-answer-output",
        },
        "formula": [
            "JouleLenzLaw", "get_Q",
        ],
    },
    "joule-lenz-law-P-button": {
        "input": {
            "joule-lenz-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "joule-lenz-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "joule-lenz-law-answer-output",
        },
        "formula": [
            "JouleLenzLaw", "get_P",
        ],
    },
    "joule-lenz-law-t-button": {
        "input": {
            "joule-lenz-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "joule-lenz-law-P-input": {
                "name": "P",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "joule-lenz-law-answer-output",
        },
        "formula": [
            "JouleLenzLaw", "get_t",
        ],
    },
    "coulombs-law-F-button": {
        "input": {
            "coulombs-law-k-input": {
                "name": "k",
                "mode": "scalar",
            },
            "coulombs-law-q1-input": {
                "name": "q1",
                "mode": "scalar",
            },
            "coulombs-law-q2-input": {
                "name": "q2",
                "mode": "scalar",
            },
            "coulombs-law-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "coulombs-law-answer-output",
        },
        "formula": [
            "CoulombsLaw", "get_F",
        ],
    },
    "coulombs-law-q1-button": {
        "input": {
            "coulombs-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "coulombs-law-k-input": {
                "name": "k",
                "mode": "scalar",
            },
            "coulombs-law-q2-input": {
                "name": "q2",
                "mode": "scalar",
            },
            "coulombs-law-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "coulombs-law-answer-output",
        },
        "formula": [
            "CoulombsLaw", "get_q1",
        ],
    },
    "coulombs-law-q2-button": {
        "input": {
            "coulombs-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "coulombs-law-k-input": {
                "name": "k",
                "mode": "scalar",
            },
            "coulombs-law-q1-input": {
                "name": "q1",
                "mode": "scalar",
            },
            "coulombs-law-r-input": {
                "name": "r",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "coulombs-law-answer-output",
        },
        "formula": [
            "CoulombsLaw", "get_q2",
        ],
    },
    "coulombs-law-r-button": {
        "input": {
            "coulombs-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "coulombs-law-k-input": {
                "name": "k",
                "mode": "scalar",
            },
            "coulombs-law-q1-input": {
                "name": "q1",
                "mode": "scalar",
            },
            "coulombs-law-q2-input": {
                "name": "q2",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "coulombs-law-answer-output",
        },
        "formula": [
            "CoulombsLaw", "get_r",
        ],
    },
    "conductor-resistance-law-R-button": {
        "input": {
            "conductor-resistance-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "conductor-resistance-law-l-input": {
                "name": "l",
                "mode": "scalar",
            },
            "conductor-resistance-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "conductor-resistance-law-answer-output",
        },
        "formula": [
            "ConductorResistanceLaw", "get_R",
        ],
    },
    "conductor-resistance-law-rho-button": {
        "input": {
            "conductor-resistance-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "conductor-resistance-law-l-input": {
                "name": "l",
                "mode": "scalar",
            },
            "conductor-resistance-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "conductor-resistance-law-answer-output",
        },
        "formula": [
            "ConductorResistanceLaw", "get_rho",
        ],
    },
    "conductor-resistance-law-l-button": {
        "input": {
            "conductor-resistance-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "conductor-resistance-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "conductor-resistance-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "conductor-resistance-law-answer-output",
        },
        "formula": [
            "ConductorResistanceLaw", "get_l",
        ],
    },
    "conductor-resistance-law-S-button": {
        "input": {
            "conductor-resistance-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "conductor-resistance-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "conductor-resistance-law-l-input": {
                "name": "l",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "conductor-resistance-law-answer-output",
        },
        "formula": [
            "ConductorResistanceLaw", "get_S",
        ],
    },
    "amperes-law-F-button": {
        "input": {
            "amperes-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "amperes-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
            "amperes-law-L-input": {
                "name": "L",
                "mode": "scalar",
            },
            "amperes-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amperes-law-answer-output",
        },
        "formula": [
            "AmperesLaw", "get_F",
        ],
    },
    "amperes-law-B-button": {
        "input": {
            "amperes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "amperes-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
            "amperes-law-L-input": {
                "name": "L",
                "mode": "scalar",
            },
            "amperes-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amperes-law-answer-output",
        },
        "formula": [
            "AmperesLaw", "get_B",
        ],
    },
    "amperes-law-I-button": {
        "input": {
            "amperes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "amperes-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "amperes-law-L-input": {
                "name": "L",
                "mode": "scalar",
            },
            "amperes-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amperes-law-answer-output",
        },
        "formula": [
            "AmperesLaw", "get_I",
        ],
    },
    "amperes-law-L-button": {
        "input": {
            "amperes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "amperes-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "amperes-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
            "amperes-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amperes-law-answer-output",
        },
        "formula": [
            "AmperesLaw", "get_L",
        ],
    },
    "amperes-law-sina-button": {
        "input": {
            "amperes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "amperes-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "amperes-law-I-input": {
                "name": "I",
                "mode": "scalar",
            },
            "amperes-law-L-input": {
                "name": "L",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amperes-law-answer-output",
        },
        "formula": [
            "AmperesLaw", "get_sina",
        ],
    },
    "lorentz-law-F-button": {
        "input": {
            "lorentz-law-q-input": {
                "name": "q",
                "mode": "scalar",
            },
            "lorentz-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "lorentz-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "lorentz-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "lorentz-law-answer-output",
        },
        "formula": [
            "LorentzLaw", "get_F",
        ],
    },
    "lorentz-law-q-button": {
        "input": {
            "lorentz-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "lorentz-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "lorentz-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "lorentz-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "lorentz-law-answer-output",
        },
        "formula": [
            "LorentzLaw", "get_q",
        ],
    },
    "lorentz-law-v-button": {
        "input": {
            "lorentz-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "lorentz-law-q-input": {
                "name": "q",
                "mode": "scalar",
            },
            "lorentz-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "lorentz-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "lorentz-law-answer-output",
        },
        "formula": [
            "LorentzLaw", "get_v",
        ],
    },
    "lorentz-law-B-button": {
        "input": {
            "lorentz-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "lorentz-law-q-input": {
                "name": "q",
                "mode": "scalar",
            },
            "lorentz-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "lorentz-law-sina-input": {
                "name": "sina",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "lorentz-law-answer-output",
        },
        "formula": [
            "LorentzLaw", "get_B",
        ],
    },
    "lorentz-law-sina-button": {
        "input": {
            "lorentz-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "lorentz-law-q-input": {
                "name": "q",
                "mode": "scalar",
            },
            "lorentz-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "lorentz-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "lorentz-law-answer-output",
        },
        "formula": [
            "LorentzLaw", "get_sina",
        ],
    },
    "faradays-law-E-button": {
        "input": {
            "faradays-law-Dphi-input": {
                "name": "Dphi",
                "mode": "scalar",
            },
            "faradays-law-Dt-input": {
                "name": "Dt",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "faradays-law-answer-output",
        },
        "formula": [
            "FaradaysLaw", "get_E",
        ],
    },
    "faradays-law-Dphi-button": {
        "input": {
            "faradays-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "faradays-law-Dt-input": {
                "name": "Dt",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "faradays-law-answer-output",
        },
        "formula": [
            "FaradaysLaw", "get_Dphi",
        ],
    },
    "faradays-law-Dt-button": {
        "input": {
            "faradays-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "faradays-law-Dphi-input": {
                "name": "Dphi",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "faradays-law-answer-output",
        },
        "formula": [
            "FaradaysLaw", "get_Dt",
        ],
    },
    "magnetic-flux-to-contour-law-phi-button": {
        "input": {
            "magnetic-flux-to-contour-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "magnetic-flux-to-contour-law-answer-output",
        },
        "formula": [
            "MagneticFluxToContourLaw", "get_phi",
        ],
    },
    "magnetic-flux-to-contour-law-B-button": {
        "input": {
            "magnetic-flux-to-contour-law-phi-input": {
                "name": "phi",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "magnetic-flux-to-contour-law-answer-output",
        },
        "formula": [
            "MagneticFluxToContourLaw", "get_B",
        ],
    },
    "magnetic-flux-to-contour-law-S-button": {
        "input": {
            "magnetic-flux-to-contour-law-phi-input": {
                "name": "phi",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "magnetic-flux-to-contour-law-answer-output",
        },
        "formula": [
            "MagneticFluxToContourLaw", "get_S",
        ],
    },
    "magnetic-flux-to-contour-law-cosa-button": {
        "input": {
            "magnetic-flux-to-contour-law-phi-input": {
                "name": "phi",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-B-input": {
                "name": "B",
                "mode": "scalar",
            },
            "magnetic-flux-to-contour-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "magnetic-flux-to-contour-law-answer-output",
        },
        "formula": [
            "MagneticFluxToContourLaw", "get_cosa",
        ],
    },
    "newtons-second-law-F-button": {
        "input": {
            "newtons-second-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "newtons-second-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "newtons-second-law-answer-output",
        },
        "formula": [
            "NewtonsSecondLaw", "get_F",
        ],
    },
    "newtons-second-law-m-button": {
        "input": {
            "newtons-second-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "newtons-second-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "newtons-second-law-answer-output",
        },
        "formula": [
            "NewtonsSecondLaw", "get_m",
        ],
    },
    "newtons-second-law-a-button": {
        "input": {
            "newtons-second-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "newtons-second-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "newtons-second-law-answer-output",
        },
        "formula": [
            "NewtonsSecondLaw", "get_a",
        ],
    },
    "hookes-law-F-button": {
        "input": {
            "hookes-law-k-input": {
                "name": "k",
                "mode": "scalar",
            },
            "hookes-law-Dx-input": {
                "name": "Dx",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "hookes-law-answer-output",
        },
        "formula": [
            "HookesLaw", "get_F",
        ],
    },
    "hookes-law-k-button": {
        "input": {
            "hookes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "hookes-law-Dx-input": {
                "name": "Dx",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "hookes-law-answer-output",
        },
        "formula": [
            "HookesLaw", "get_k",
        ],
    },
    "hookes-law-Dx-button": {
        "input": {
            "hookes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "hookes-law-k-input": {
                "name": "k",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "hookes-law-answer-output",
        },
        "formula": [
            "HookesLaw", "get_Dx",
        ],
    },
    "amontons-coulomb-law-F-button": {
        "input": {
            "amontons-coulomb-law-mu-input": {
                "name": "mu",
                "mode": "scalar",
            },
            "amontons-coulomb-law-N-input": {
                "name": "N",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amontons-coulomb-law-answer-output",
        },
        "formula": [
            "AmontonsCoulombLaw", "get_F",
        ],
    },
    "amontons-coulomb-law-mu-button": {
        "input": {
            "amontons-coulomb-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "amontons-coulomb-law-N-input": {
                "name": "N",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amontons-coulomb-law-answer-output",
        },
        "formula": [
            "AmontonsCoulombLaw", "get_mu",
        ],
    },
    "amontons-coulomb-law-N-button": {
        "input": {
            "amontons-coulomb-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "amontons-coulomb-law-mu-input": {
                "name": "mu",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "amontons-coulomb-law-answer-output",
        },
        "formula": [
            "AmontonsCoulombLaw", "get_N",
        ],
    },
    "normal-reaction-law-N-button": {
        "input": {
            "normal-reaction-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "normal-reaction-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "normal-reaction-law-answer-output",
        },
        "formula": [
            "NormalReactionLaw", "get_N",
        ],
    },
    "normal-reaction-law-F-button": {
        "input": {
            "normal-reaction-law-N-input": {
                "name": "N",
                "mode": "scalar",
            },
            "normal-reaction-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "normal-reaction-law-answer-output",
        },
        "formula": [
            "NormalReactionLaw", "get_F",
        ],
    },
    "normal-reaction-law-cosa-button": {
        "input": {
            "normal-reaction-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "normal-reaction-law-N-input": {
                "name": "N",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "normal-reaction-law-answer-output",
        },
        "formula": [
            "NormalReactionLaw", "get_cosa",
        ],
    },
    "momentum-law-p-button": {
        "input": {
            "momentum-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "momentum-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "momentum-law-answer-output",
        },
        "formula": [
            "MomentumLaw", "get_p",
        ],
    },
    "momentum-law-m-button": {
        "input": {
            "momentum-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "momentum-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "momentum-law-answer-output",
        },
        "formula": [
            "MomentumLaw", "get_m",
        ],
    },
    "momentum-law-v-button": {
        "input": {
            "momentum-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "momentum-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "momentum-law-answer-output",
        },
        "formula": [
            "MomentumLaw", "get_v",
        ],
    },
    "kinetic-energy-law-E-button": {
        "input": {
            "kinetic-energy-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "kinetic-energy-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "kinetic-energy-law-answer-output",
        },
        "formula": [
            "KineticEnergyLaw", "get_E",
        ],
    },
    "kinetic-energy-law-m-button": {
        "input": {
            "kinetic-energy-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "kinetic-energy-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "kinetic-energy-law-answer-output",
        },
        "formula": [
            "KineticEnergyLaw", "get_m",
        ],
    },
    "kinetic-energy-law-v-button": {
        "input": {
            "kinetic-energy-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "kinetic-energy-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "kinetic-energy-law-answer-output",
        },
        "formula": [
            "KineticEnergyLaw", "get_v",
        ],
    },
    "potential-energy-law-E-button": {
        "input": {
            "potential-energy-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "potential-energy-law-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "potential-energy-law-answer-output",
        },
        "formula": [
            "PotentialEnergyLaw", "get_E",
        ],
    },
    "potential-energy-law-F-button": {
        "input": {
            "potential-energy-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "potential-energy-law-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "potential-energy-law-answer-output",
        },
        "formula": [
            "PotentialEnergyLaw", "get_F",
        ],
    },
    "potential-energy-law-h-button": {
        "input": {
            "potential-energy-law-E-input": {
                "name": "E",
                "mode": "scalar",
            },
            "potential-energy-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "potential-energy-law-answer-output",
        },
        "formula": [
            "PotentialEnergyLaw", "get_h",
        ],
    },
    "mechanical-work-law-A-button": {
        "input": {
            "mechanical-work-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "mechanical-work-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "mechanical-work-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-work-law-answer-output",
        },
        "formula": [
            "MechanicalWorkLaw", "get_A",
        ],
    },
    "mechanical-work-law-F-button": {
        "input": {
            "mechanical-work-law-A-input": {
                "name": "A",
                "mode": "scalar",
            },
            "mechanical-work-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "mechanical-work-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-work-law-answer-output",
        },
        "formula": [
            "MechanicalWorkLaw", "get_F",
        ],
    },
    "mechanical-work-law-S-button": {
        "input": {
            "mechanical-work-law-A-input": {
                "name": "A",
                "mode": "scalar",
            },
            "mechanical-work-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "mechanical-work-law-cosa-input": {
                "name": "cosa",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-work-law-answer-output",
        },
        "formula": [
            "MechanicalWorkLaw", "get_S",
        ],
    },
    "mechanical-work-law-cosa-button": {
        "input": {
            "mechanical-work-law-A-input": {
                "name": "A",
                "mode": "scalar",
            },
            "mechanical-work-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "mechanical-work-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-work-law-answer-output",
        },
        "formula": [
            "MechanicalWorkLaw", "get_cosa",
        ],
    },
    "mechanical-power-law-P-button": {
        "input": {
            "mechanical-power-law-A-input": {
                "name": "A",
                "mode": "scalar",
            },
            "mechanical-power-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-power-law-answer-output",
        },
        "formula": [
            "MechanicalPowerLaw", "get_P",
        ],
    },
    "mechanical-power-law-A-button": {
        "input": {
            "mechanical-power-law-P-input": {
                "name": "P",
                "mode": "scalar",
            },
            "mechanical-power-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-power-law-answer-output",
        },
        "formula": [
            "MechanicalPowerLaw", "get_A",
        ],
    },
    "mechanical-power-law-t-button": {
        "input": {
            "mechanical-power-law-P-input": {
                "name": "P",
                "mode": "scalar",
            },
            "mechanical-power-law-A-input": {
                "name": "A",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-power-law-answer-output",
        },
        "formula": [
            "MechanicalPowerLaw", "get_t",
        ],
    },
    "mechanical-efficiency-law-eta-button": {
        "input": {
            "mechanical-efficiency-law-Au-input": {
                "name": "Au",
                "mode": "scalar",
            },
            "mechanical-efficiency-law-At-input": {
                "name": "At",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-efficiency-law-answer-output",
        },
        "formula": [
            "MechanicalEfficiencyLaw", "get_eta",
        ],
    },
    "mechanical-efficiency-law-Au-button": {
        "input": {
            "mechanical-efficiency-law-eta-input": {
                "name": "eta",
                "mode": "scalar",
            },
            "mechanical-efficiency-law-At-input": {
                "name": "At",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-efficiency-law-answer-output",
        },
        "formula": [
            "MechanicalEfficiencyLaw", "get_Au",
        ],
    },
    "mechanical-efficiency-law-At-button": {
        "input": {
            "mechanical-efficiency-law-eta-input": {
                "name": "eta",
                "mode": "scalar",
            },
            "mechanical-efficiency-law-Au-input": {
                "name": "Au",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mechanical-efficiency-law-answer-output",
        },
        "formula": [
            "MechanicalEfficiencyLaw", "get_At",
        ],
    },
    "linear-acceleration-law-a-button": {
        "input": {
            "linear-acceleration-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "linear-acceleration-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "linear-acceleration-law-answer-output",
        },
        "formula": [
            "LinearAccelerationLaw", "get_a",
        ],
    },
    "linear-acceleration-law-v-button": {
        "input": {
            "linear-acceleration-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "linear-acceleration-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "linear-acceleration-law-answer-output",
        },
        "formula": [
            "LinearAccelerationLaw", "get_v",
        ],
    },
    "linear-acceleration-law-t-button": {
        "input": {
            "linear-acceleration-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "linear-acceleration-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "linear-acceleration-law-answer-output",
        },
        "formula": [
            "LinearAccelerationLaw", "get_t",
        ],
    },
    "uniform-accelerated-rectilinear-motion-law-S-button": {
        "input": {
            "uniform-accelerated-rectilinear-motion-law-v0-input": {
                "name": "v0",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "uniform-accelerated-rectilinear-motion-law-answer-output",
        },
        "formula": [
            "UniformlyAcceleratedRectilinearMotionLaw", "get_S",
        ],
    },
    "uniform-accelerated-rectilinear-motion-law-v0-button": {
        "input": {
            "uniform-accelerated-rectilinear-motion-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "uniform-accelerated-rectilinear-motion-law-answer-output",
        },
        "formula": [
            "UniformlyAcceleratedRectilinearMotionLaw", "get_v0",
        ],
    },
    "uniform-accelerated-rectilinear-motion-law-a-button": {
        "input": {
            "uniform-accelerated-rectilinear-motion-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-v0-input": {
                "name": "v0",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-t-input": {
                "name": "t",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "uniform-accelerated-rectilinear-motion-law-answer-output",
        },
        "formula": [
            "UniformlyAcceleratedRectilinearMotionLaw", "get_a",
        ],
    },
    "uniform-accelerated-rectilinear-motion-law-t-button": {
        "input": {
            "uniform-accelerated-rectilinear-motion-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-v0-input": {
                "name": "v0",
                "mode": "scalar",
            },
            "uniform-accelerated-rectilinear-motion-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "uniform-accelerated-rectilinear-motion-law-answer-output",
        },
        "formula": [
            "UniformlyAcceleratedRectilinearMotionLaw", "get_t",
        ],
    },
    "centripetal-acceleration-law-a-button": {
        "input": {
            "centripetal-acceleration-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "centripetal-acceleration-law-w-input": {
                "name": "w",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "centripetal-acceleration-law-answer-output",
        },
        "formula": [
            "CentripetalAccelerationLaw", "get_a",
        ],
    },
    "centripetal-acceleration-law-v-button": {
        "input": {
            "centripetal-acceleration-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "centripetal-acceleration-law-w-input": {
                "name": "w",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "centripetal-acceleration-law-answer-output",
        },
        "formula": [
            "CentripetalAccelerationLaw", "get_v",
        ],
    },
    "centripetal-acceleration-law-w-button": {
        "input": {
            "centripetal-acceleration-law-a-input": {
                "name": "a",
                "mode": "scalar",
            },
            "centripetal-acceleration-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "centripetal-acceleration-law-answer-output",
        },
        "formula": [
            "CentripetalAccelerationLaw", "get_w",
        ],
    },
    "trajectory-radius-law-R-button": {
        "input": {
            "trajectory-radius-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "trajectory-radius-law-w-input": {
                "name": "w",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trajectory-radius-law-answer-output",
        },
        "formula": [
            "TrajectoryRadiusLaw", "get_R",
        ],
    },
    "trajectory-radius-law-v-button": {
        "input": {
            "trajectory-radius-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "trajectory-radius-law-w-input": {
                "name": "w",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trajectory-radius-law-answer-output",
        },
        "formula": [
            "TrajectoryRadiusLaw", "get_v",
        ],
    },
    "trajectory-radius-law-w-button": {
        "input": {
            "trajectory-radius-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "trajectory-radius-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "trajectory-radius-law-answer-output",
        },
        "formula": [
            "TrajectoryRadiusLaw", "get_w",
        ],
    },
    "pascals-law-p-button": {
        "input": {
            "pascals-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "pascals-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "pascals-law-answer-output",
        },
        "formula": [
            "PascalsLaw", "get_p",
        ],
    },
    "pascals-law-F-button": {
        "input": {
            "pascals-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "pascals-law-S-input": {
                "name": "S",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "pascals-law-answer-output",
        },
        "formula": [
            "PascalsLaw", "get_F",
        ],
    },
    "pascals-law-S-button": {
        "input": {
            "pascals-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "pascals-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "pascals-law-answer-output",
        },
        "formula": [
            "PascalsLaw", "get_S",
        ],
    },
    "archimedes-law-F-button": {
        "input": {
            "archimedes-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "archimedes-law-V-input": {
                "name": "V",
                "mode": "scalar",
            },
            "archimedes-law-g-input": {
                "name": "g",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "archimedes-law-answer-output",
        },
        "formula": [
            "ArchimedesLaw", "get_F",
        ],
    },
    "archimedes-law-rho-button": {
        "input": {
            "archimedes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "archimedes-law-V-input": {
                "name": "V",
                "mode": "scalar",
            },
            "archimedes-law-g-input": {
                "name": "g",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "archimedes-law-answer-output",
        },
        "formula": [
            "ArchimedesLaw", "get_rho",
        ],
    },
    "archimedes-law-V-button": {
        "input": {
            "archimedes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "archimedes-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "archimedes-law-g-input": {
                "name": "g",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "archimedes-law-answer-output",
        },
        "formula": [
            "ArchimedesLaw", "get_V",
        ],
    },
    "archimedes-law-g-button": {
        "input": {
            "archimedes-law-F-input": {
                "name": "F",
                "mode": "scalar",
            },
            "archimedes-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "archimedes-law-V-input": {
                "name": "V",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "archimedes-law-answer-output",
        },
        "formula": [
            "ArchimedesLaw", "get_g",
        ],
    },
    "hydrostatic-pressure-law-p-button": {
        "input": {
            "hydrostatic-pressure-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-g-input": {
                "name": "g",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "hydrostatic-pressure-law-answer-output",
        },
        "formula": [
            "HydrostaticPressureLaw", "get_p",
        ],
    },
    "hydrostatic-pressure-law-rho-button": {
        "input": {
            "hydrostatic-pressure-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-g-input": {
                "name": "g",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "hydrostatic-pressure-law-answer-output",
        },
        "formula": [
            "HydrostaticPressureLaw", "get_rho",
        ],
    },
    "hydrostatic-pressure-law-g-button": {
        "input": {
            "hydrostatic-pressure-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-h-input": {
                "name": "h",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "hydrostatic-pressure-law-answer-output",
        },
        "formula": [
            "HydrostaticPressureLaw", "get_g",
        ],
    },
    "hydrostatic-pressure-law-h-button": {
        "input": {
            "hydrostatic-pressure-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-rho-input": {
                "name": "rho",
                "mode": "scalar",
            },
            "hydrostatic-pressure-law-g-input": {
                "name": "g",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "hydrostatic-pressure-law-answer-output",
        },
        "formula": [
            "HydrostaticPressureLaw", "get_h",
        ],
    },
    "sensible-heat-law-Q-button": {
        "input": {
            "sensible-heat-law-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "sensible-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "sensible-heat-law-Dt-input": {
                "name": "Dt",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "sensible-heat-law-answer-output",
        },
        "formula": [
            "SensibleHeatLaw", "get_Q",
        ],
    },
    "sensible-heat-law-c-button": {
        "input": {
            "sensible-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "sensible-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "sensible-heat-law-Dt-input": {
                "name": "Dt",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "sensible-heat-law-answer-output",
        },
        "formula": [
            "SensibleHeatLaw", "get_c",
        ],
    },
    "sensible-heat-law-m-button": {
        "input": {
            "sensible-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "sensible-heat-law-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "sensible-heat-law-Dt-input": {
                "name": "Dt",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "sensible-heat-law-answer-output",
        },
        "formula": [
            "SensibleHeatLaw", "get_m",
        ],
    },
    "sensible-heat-law-Dt-button": {
        "input": {
            "sensible-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "sensible-heat-law-c-input": {
                "name": "c",
                "mode": "scalar",
            },
            "sensible-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "sensible-heat-law-answer-output",
        },
        "formula": [
            "SensibleHeatLaw", "get_Dt",
        ],
    },
    "combustion-heat-law-Q-button": {
        "input": {
            "combustion-heat-law-q-input": {
                "name": "q",
                "mode": "scalar",
            },
            "combustion-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "combustion-heat-law-answer-output",
        },
        "formula": [
            "CombustionHeatLaw", "get_Q",
        ],
    },
    "combustion-heat-law-q-button": {
        "input": {
            "combustion-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "combustion-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "combustion-heat-law-answer-output",
        },
        "formula": [
            "CombustionHeatLaw", "get_q",
        ],
    },
    "combustion-heat-law-m-button": {
        "input": {
            "combustion-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "combustion-heat-law-q-input": {
                "name": "q",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "combustion-heat-law-answer-output",
        },
        "formula": [
            "CombustionHeatLaw", "get_m",
        ],
    },
    "fusion-heat-law-Q-button": {
        "input": {
            "fusion-heat-law-lmb-input": {
                "name": "lmb",
                "mode": "scalar",
            },
            "fusion-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "fusion-heat-law-answer-output",
        },
        "formula": [
            "FusionHeatLaw", "get_Q",
        ],
    },
    "fusion-heat-law-lmb-button": {
        "input": {
            "fusion-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "fusion-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "fusion-heat-law-answer-output",
        },
        "formula": [
            "FusionHeatLaw", "get_lmb",
        ],
    },
    "fusion-heat-law-m-button": {
        "input": {
            "fusion-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "fusion-heat-law-lmb-input": {
                "name": "lmb",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "fusion-heat-law-answer-output",
        },
        "formula": [
            "FusionHeatLaw", "get_m",
        ],
    },
    "vaporization-heat-law-Q-button": {
        "input": {
            "vaporization-heat-law-L-input": {
                "name": "L",
                "mode": "scalar",
            },
            "vaporization-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vaporization-heat-law-answer-output",
        },
        "formula": [
            "VaporizationHeatLaw", "get_Q",
        ],
    },
    "vaporization-heat-law-L-button": {
        "input": {
            "vaporization-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "vaporization-heat-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vaporization-heat-law-answer-output",
        },
        "formula": [
            "VaporizationHeatLaw", "get_L",
        ],
    },
    "vaporization-heat-law-m-button": {
        "input": {
            "vaporization-heat-law-Q-input": {
                "name": "Q",
                "mode": "scalar",
            },
            "vaporization-heat-law-L-input": {
                "name": "L",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "vaporization-heat-law-answer-output",
        },
        "formula": [
            "VaporizationHeatLaw", "get_m",
        ],
    },
    "mendeleev-clapeyron-law-p-button": {
        "input": {
            "mendeleev-clapeyron-law-V-input": {
                "name": "V",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-T-input": {
                "name": "T",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mendeleev-clapeyron-law-answer-output",
        },
        "formula": [
            "MendeleevClapeyronLaw", "get_p",
        ],
    },
    "mendeleev-clapeyron-law-V-button": {
        "input": {
            "mendeleev-clapeyron-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-T-input": {
                "name": "T",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mendeleev-clapeyron-law-answer-output",
        },
        "formula": [
            "MendeleevClapeyronLaw", "get_V",
        ],
    },
    "mendeleev-clapeyron-law-v-button": {
        "input": {
            "mendeleev-clapeyron-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-V-input": {
                "name": "V",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-T-input": {
                "name": "T",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mendeleev-clapeyron-law-answer-output",
        },
        "formula": [
            "MendeleevClapeyronLaw", "get_v",
        ],
    },
    "mendeleev-clapeyron-law-T-button": {
        "input": {
            "mendeleev-clapeyron-law-p-input": {
                "name": "p",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-V-input": {
                "name": "V",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "mendeleev-clapeyron-law-R-input": {
                "name": "R",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "mendeleev-clapeyron-law-answer-output",
        },
        "formula": [
            "MendeleevClapeyronLaw", "get_T",
        ],
    },
    "molar-mass-law-v-button": {
        "input": {
            "molar-mass-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
            "molar-mass-law-M-input": {
                "name": "M",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "molar-mass-law-answer-output",
        },
        "formula": [
            "MolarMassLaw", "get_v",
        ],
    },
    "molar-mass-law-m-button": {
        "input": {
            "molar-mass-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "molar-mass-law-M-input": {
                "name": "M",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "molar-mass-law-answer-output",
        },
        "formula": [
            "MolarMassLaw", "get_m",
        ],
    },
    "molar-mass-law-M-button": {
        "input": {
            "molar-mass-law-v-input": {
                "name": "v",
                "mode": "scalar",
            },
            "molar-mass-law-m-input": {
                "name": "m",
                "mode": "scalar",
            },
        },
        "output": {
            "id": "molar-mass-law-answer-output",
        },
        "formula": [
            "MolarMassLaw", "get_M",
        ],
    },
};
