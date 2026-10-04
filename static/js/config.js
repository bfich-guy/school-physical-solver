export const WidgetsIdRegistry = {
    "SolverHeader": "solver-header",
    "SolverFooter": "solver-footer",
};


export const SolverData = {
    "SolverTitle": "Физмат-калькулятор",
    "SolverSlogan": "Все расчёты верны!",
    "SolverHeader": `
        <p class="solver-header-text">
            Физмат-калькулятор
        </p>
    `,
    "SolverFooter": `
        <div class="solver-footer-card">
            <p class="solver-footer-card-title">
                Навигация
            </p>
            <div>
                <a class="solver-footer-redirect-button" href="/">
                    Главная
                </a>
                <a class="solver-footer-redirect-button" href="/math/algebra">
                    Алгебра
                </a>
                <a class="solver-footer-redirect-button" href="/math/geometry">
                    Геометрия
                </a>
                <a class="solver-footer-redirect-button" href="/physics/electromagnetics">
                    Электромагнетизм
                </a>
                <a class="solver-footer-redirect-button" href="/physics/mechanics">
                    Механика
                </a>
                <a class="solver-footer-redirect-button" href="/physics/thermodynamics">
                    Термодинамика
                </a>
            </div>
        </div>
        <div class="solver-footer-card">
            <p class="solver-footer-card-title">
                Поддержка
            </p>
            <div>
                <a class="solver-footer-redirect-button" href="/usagepolicy">
                    Политика пользования
                </a>
                <a class="solver-footer-redirect-button" href="/faq">
                    Помощь в использовании
                </a>
                <a class="solver-footer-redirect-button" href="/extrainfo">
                    Дополнительная информация
                </a>
            </div>
        </div>
    `,
};

export const ButtonsIdlist = [
    "linear-equation-solving-button",
    "quadratic-equation-solving-button",
    "linear-function-y-button",
    "linear-function-k-button",
    "linear-function-b-button",
    "quadratic-function-y-button",
    "quadratic-function-a-button",
    "quadratic-function-b-button",
    "quadratic-function-c-button",
    "arithmetic-progression-sum-theorem-s-button",
    "arithmetic-progression-sum-theorem-a1-button",
    "arithmetic-progression-sum-theorem-an-button",
    "arithmetic-progression-sum-theorem-n-button",
    "geometric-progression-sum-theorem-s-button",
    "geometric-progression-sum-theorem-b1-button",
    "geometric-progression-sum-theorem-bn-button",
    "geometric-progression-sum-theorem-q-button",
    "arithmetic-progression-term-theorem-an-button",
    "arithmetic-progression-term-theorem-a1-button",
    "arithmetic-progression-term-theorem-d-button",
    "arithmetic-progression-term-theorem-n-button",
    "geometric-progression-term-theorem-bn-button",
    "geometric-progression-term-theorem-b1-button",
    "geometric-progression-term-theorem-q-button",
    "geometric-progression-term-theorem-n-button",
];

export const inputsIdMap = {
    "linear-equation-solving-button": [
        "linear-equation-a-input", 
        "linear-equation-b-input",
    ],
    "quadratic-equation-solving-button": [
        "quadratic-equation-a-input",
        "quadratic-equation-b-input",
        "quadratic-equation-c-input",
    ],
    "linear-function-y-button": [
        "linear-function-x-input",
        "linear-function-k-input",
        "linear-function-b-input",
    ],
    "linear-function-k-button": [
        "linear-function-y-input",
        "linear-function-x-input",
        "linear-function-b-input",
    ],
    "linear-function-b-button": [
        "linear-function-y-input",
        "linear-function-k-input",
        "linear-function-x-input",
    ],
    "quadratic-function-y-button": [
        "quadratic-function-x-input",
        "quadratic-function-a-input",
        "quadratic-function-b-input",
        "quadratic-function-c-input",
    ],
    "quadratic-function-a-button": [
        "quadratic-function-y-input",
        "quadratic-function-x-input",
        "quadratic-function-b-input",
        "quadratic-function-c-input",
    ],
    "quadratic-function-b-button": [
        "quadratic-function-y-input",
        "quadratic-function-x-input",
        "quadratic-function-a-input",
        "quadratic-function-c-input",
    ],
    "quadratic-function-c-button": [
        "quadratic-function-y-input",
        "quadratic-function-x-input",
        "quadratic-function-a-input",
        "quadratic-function-b-input",
    ],
    "arithmetic-progression-sum-theorem-s-button": [
        "arithmetic-progression-sum-theorem-a1-input",
        "arithmetic-progression-sum-theorem-an-input",
        "arithmetic-progression-sum-theorem-n-input",
    ],
    "arithmetic-progression-sum-theorem-a1-button": [
        "arithmetic-progression-sum-theorem-s-input",
        "arithmetic-progression-sum-theorem-an-input",
        "arithmetic-progression-sum-theorem-n-input",
    ],
    "arithmetic-progression-sum-theorem-an-button": [
        "arithmetic-progression-sum-theorem-s-input",
        "arithmetic-progression-sum-theorem-a1-input",
        "arithmetic-progression-sum-theorem-n-input",
    ],
    "arithmetic-progression-sum-theorem-n-button": [
        "arithmetic-progression-sum-theorem-s-input",
        "arithmetic-progression-sum-theorem-a1-input",
        "arithmetic-progression-sum-theorem-an-input",
    ],
    "geometric-progression-sum-theorem-s-button": [
        "geometric-progression-sum-theorem-b1-input",
        "geometric-progression-sum-theorem-bn-input",
        "geometric-progression-sum-theorem-q-input",
    ],
    "geometric-progression-sum-theorem-b1-button": [
        "geometric-progression-sum-theorem-s-input",
        "geometric-progression-sum-theorem-bn-input",
        "geometric-progression-sum-theorem-q-input",
    ],
    "geometric-progression-sum-theorem-bn-button": [
        "geometric-progression-sum-theorem-s-input",
        "geometric-progression-sum-theorem-b1-input",
        "geometric-progression-sum-theorem-q-input",
    ],
    "geometric-progression-sum-theorem-q-button": [
        "geometric-progression-sum-theorem-s-input",
        "geometric-progression-sum-theorem-b1-input",
        "geometric-progression-sum-theorem-bn-input",
    ],
    "arithmetic-progression-term-theorem-an-button": [
        "arithmetic-progression-term-theorem-a1-input",
        "arithmetic-progression-term-theorem-d-input",
        "arithmetic-progression-term-theorem-n-input",
    ],
    "arithmetic-progression-term-theorem-a1-button": [
        "arithmetic-progression-term-theorem-an-input",
        "arithmetic-progression-term-theorem-d-input",
        "arithmetic-progression-term-theorem-n-input",
    ],
    "arithmetic-progression-term-theorem-d-button": [
        "arithmetic-progression-term-theorem-an-input",
        "arithmetic-progression-term-theorem-a1-input",
        "arithmetic-progression-term-theorem-n-input",
    ],
    "arithmetic-progression-term-theorem-n-button": [
        "arithmetic-progression-term-theorem-a1-input",
        "arithmetic-progression-term-theorem-an-input",
        "arithmetic-progression-term-theorem-d-input",
    ],
    "geometric-progression-term-theorem-bn-button": [
        "geometric-progression-term-theorem-b1-input",
        "geometric-progression-term-theorem-q-input",
        "geometric-progression-term-theorem-n-input",
    ],
    "geometric-progression-term-theorem-b1-button": [
        "geometric-progression-term-theorem-bn-input",
        "geometric-progression-term-theorem-q-input",
        "geometric-progression-term-theorem-n-input",
    ],
    "geometric-progression-term-theorem-q-button": [
        "geometric-progression-term-theorem-bn-input",
        "geometric-progression-term-theorem-b1-input",
        "geometric-progression-term-theorem-n-input",
    ],
    "geometric-progression-term-theorem-n-button": [
        "geometric-progression-term-theorem-bn-input",
        "geometric-progression-term-theorem-bq-input",
        "geometric-progression-term-theorem-q-input",
    ],
};

export const inputsQuantitiesMap = {
    "linear-equation-a-input": "a",
    "linear-equation-b-input": "b",
    "quadratic-equation-a-input": "a",
    "quadratic-equation-b-input": "b",
    "quadratic-equation-c-input": "c",
    "linear-function-x-input": "x",
    "linear-function-y-input": "y",
    "linear-function-k-input": "k",
    "linear-function-b-input": "b",
    "quadratic-function-x-input": "x",
    "quadratic-function-y-input": "y",
    "quadratic-function-a-input": "a",
    "quadratic-function-b-input": "b",
    "quadratic-function-c-input": "c",
    "arithmetic-progression-sum-theorem-s-input": "S",
    "arithmetic-progression-sum-theorem-a1-input": "a1",
    "arithmetic-progression-sum-theorem-an-input": "an",
    "arithmetic-progression-sum-theorem-n-input": "n",
    "geometric-progression-sum-theorem-s-input": "S",
    "geometric-progression-sum-theorem-b1-input": "b1",
    "geometric-progression-sum-theorem-bn-input": "bn",
    "geometric-progression-sum-theorem-q-input": "q",
    "arithmetic-progression-term-theorem-an-input": "an",
    "arithmetic-progression-term-theorem-a1-input": "a1",
    "arithmetic-progression-term-theorem-d-input": "d",
    "arithmetic-progression-term-theorem-n-input": "n",
    "geometric-progression-term-theorem-bn-input": "bn",
    "geometric-progression-term-theorem-b1-input": "b1",
    "geometric-progression-term-theorem-q-input": "q",
    "geometric-progression-term-theorem-n-input": "n",
};

export const formulasMap = {
    "linear-equation-solving-button": [
        "LinearEquation", "get_x",
    ],
    "quadratic-equation-solving-button": [
        "QuadraticEquation", "get_x",
    ],
    "linear-function-y-button": [
        "LinearFunction", "get_y",
    ],
    "linear-function-k-button": [
        "LinearFunction", "get_k",
    ],
    "linear-function-b-button": [
        "LinearFunction", "get_b",
    ],
    "quadratic-function-y-button": [
        "QuadraticFunction", "get_y",
    ],
    "quadratic-function-a-button": [
        "QuadraticFunction", "get_a",
    ],
    "quadratic-function-b-button": [
        "QuadraticFunction", "get_b",
    ],
    "quadratic-function-c-button": [
        "QuadraticFunction", "get_c",
    ],
    "arithmetic-progression-sum-theorem-s-button": [
        "ArithmeticProgressionSumTheorem", "get_S",
    ],
    "arithmetic-progression-sum-theorem-a1-button": [
        "ArithmeticProgressionSumTheorem", "get_a1",
    ],
    "arithmetic-progression-sum-theorem-an-button": [
        "ArithmeticProgressionSumTheorem", "get_an",
    ],
    "arithmetic-progression-sum-theorem-n-button": [
        "ArithmeticProgressionSumTheorem", "get_n",
    ],
    "geometric-progression-sum-theorem-s-button": [
        "GeometricProgressionSumTheorem", "get_S",
    ],
    "geometric-progression-sum-theorem-b1-button": [
        "GeometricProgressionSumTheorem", "get_b1",
    ],
    "geometric-progression-sum-theorem-bn-button": [
        "GeometricProgressionSumTheorem", "get_bn",
    ],
    "geometric-progression-sum-theorem-q-button": [
        "GeometricProgressionSumTheorem", "get_q",
    ],
    "arithmetic-progression-term-theorem-an-button": [
        "ArithmeticProgressionTermTheorem", "get_an",
    ],
    "arithmetic-progression-term-theorem-a1-button": [
        "ArithmeticProgressionTermTheorem", "get_a1",
    ],
    "arithmetic-progression-term-theorem-d-button": [
        "ArithmeticProgressionTermTheorem", "get_d",
    ],
    "arithmetic-progression-term-theorem-n-button": [
        "ArithmeticProgressionTermTheorem", "get_n",
    ],
    "geometric-progression-term-theorem-bn-button": [
        "GeometricProgressionTermTheorem", "get_bn",
    ],
    "geometric-progression-term-theorem-b1-button": [
        "GeometricProgressionTermTheorem", "get_b1",
    ],
    "geometric-progression-term-theorem-q-button": [
        "GeometricProgressionTermTheorem", "get_q",
    ],
    "geometric-progression-term-theorem-n-button": [
        "GeometricProgressionTermTheorem", "get_n",
    ],
};

export const answersMap = {
    "linear-equation-solving-button": "linear-equation-answer-output",
    "quadratic-equation-solving-button": "quadratic-equation-answer-output",
    "linear-function-y-button": "linear-function-answer-output",
    "linear-function-k-button": "linear-function-answer-output",
    "linear-function-b-button": "linear-function-answer-output",
    "quadratic-function-y-button": "quadratic-function-answer-output",
    "quadratic-function-a-button": "quadratic-function-answer-output",
    "quadratic-function-b-button": "quadratic-function-answer-output",
    "quadratic-function-c-button": "quadratic-function-answer-output",
    "arithmetic-progression-sum-theorem-s-button": "arithmetic-progression-sum-theorem-answer-output",
    "arithmetic-progression-sum-theorem-a1-button": "arithmetic-progression-sum-theorem-answer-output",
    "arithmetic-progression-sum-theorem-an-button": "arithmetic-progression-sum-theorem-answer-output",
    "arithmetic-progression-sum-theorem-n-button": "arithmetic-progression-sum-theorem-answer-output",
    "geometric-progression-sum-theorem-s-button": "geometric-progression-sum-theorem-answer-output",
    "geometric-progression-sum-theorem-b1-button": "geometric-progression-sum-theorem-answer-output",
    "geometric-progression-sum-theorem-bn-button": "geometric-progression-sum-theorem-answer-output",
    "geometric-progression-sum-theorem-q-button": "geometric-progression-sum-theorem-answer-output",
    "arithmetic-progression-term-theorem-an-button": "arithmetic-progression-term-theorem-answer-output",
    "arithmetic-progression-term-theorem-a1-button": "arithmetic-progression-term-theorem-answer-output",
    "arithmetic-progression-term-theorem-d-button": "arithmetic-progression-term-theorem-answer-output",
    "arithmetic-progression-term-theorem-n-button": "arithmetic-progression-term-theorem-answer-output",
    "geometric-progression-term-theorem-s-button": "geometric-progression-term-theorem-answer-output",
    "geometric-progression-term-theorem-b1-button": "geometric-progression-term-theorem-answer-output",
    "geometric-progression-term-theorem-bn-button": "geometric-progression-term-theorem-answer-output",
    "geometric-progression-term-theorem-q-button": "geometric-progression-term-theorem-answer-output",
};

export const calculateEndpoint = "/calculate";
