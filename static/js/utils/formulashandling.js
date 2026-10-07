import { calculateEndpoint, FormulasData } from "../config/formulasdata.js";


export function calculateFormula() {
    for (const [buttonId, buttonData] of Object.entries(FormulasData)) {
        const formulaButtonWidget = document.getElementById(buttonId);
        const formulaButtonDoesNotExist = formulaButtonWidget === null;

        if (formulaButtonDoesNotExist) {
            continue;
        };

        formulaButtonWidget.addEventListener("click", () => {
            const request = {};
            const quantitiesInputData = buttonData["input"];
            const quantitiesOutputData = buttonData["output"];
            const formula = buttonData["formula"];

            request["formula"] = formula;
            request["quantities"] = {};

            for (const [inputId, inputData] of Object.entries(quantitiesInputData)) {
                const quantityInputWidget = document.getElementById(inputId);
                const quantityInputValue = quantityInputWidget.value;
                const quantityInputName = inputData["name"];
                const quantityInputMode = inputData["mode"];

                request["quantities"][quantityInputName] = {
                    "value": quantityInputValue,
                    "mode": quantityInputMode,
                };
            }

            fetch(calculateEndpoint, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(request)
            })
            .then(responce => responce.json())
            .then(data => {
                const formulaAnswer = data.answer;
                const formulaAnswerId = quantitiesOutputData["id"];
                const formulaAnswerWidget = document.getElementById(formulaAnswerId);

                formulaAnswerWidget.textContent = formulaAnswer;
            });
        });
    };
};
