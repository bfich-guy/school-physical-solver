import { WidgetsIdRegistry, SolverData, calculateEndpoint, ButtonsIdlist, inputsIdMap, inputsQuantitiesMap, formulasMap, answersMap } from "./config.js";


export function pageSetup() {
    const SolverHeaderId = WidgetsIdRegistry["SolverHeader"];
    const solverFooterId = WidgetsIdRegistry["SolverFooter"];

    const SolverHeaderHTML = SolverData["SolverHeader"];
    const solverFooterHTML = SolverData["SolverFooter"];

    document.addEventListener("DOMContentLoaded", () => {
        const solverHeaderWidget = document.getElementById(SolverHeaderId);
        const solverFooterWidget = document.getElementById(solverFooterId);

        solverHeaderWidget.innerHTML = SolverHeaderHTML;
        solverFooterWidget.innerHTML = solverFooterHTML;
    });
};

export function calculateFormula() {
    for (const buttonId of ButtonsIdlist) {
        const buttonWidget = document.getElementById(buttonId);

        buttonWidget.addEventListener("click", () => {
            const inputsIdList = inputsIdMap[buttonId];
            const formula = formulasMap[buttonId];
            const quantities = {};

            for (const inputId of inputsIdList) {
                const inputWidget = document.getElementById(inputId);

                const inputKey = inputsQuantitiesMap[inputId];
                const inputValue = inputWidget.value;

                quantities[inputKey] = inputValue;
            }

            fetch(calculateEndpoint, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "formula": formula,
                    "quantities": quantities,
                })
            })
            .then(responce => responce.json())
            .then(data => {
                const answer = data.answer;

                const answerOutputId = answersMap[buttonId];
                const answerOutputWidget = document.getElementById(answerOutputId);

                answerOutputWidget.textContent = answer;
            });
        });
    };
}
