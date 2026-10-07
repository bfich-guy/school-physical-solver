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
};
