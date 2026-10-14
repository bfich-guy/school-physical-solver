import { calculateEndpoint, FormulasData } from "../config/formulasdata.js";
import { areObjectsNull } from "./helpers.js";


export function calculateFormula() {
    for (const [buttonId, buttonData] of Object.entries(FormulasData)) {
        const formulaButtonWidget = document.getElementById(buttonId);
        const formulaButtonDoesNotExist = areObjectsNull({objects: [formulaButtonWidget]});

        if (formulaButtonDoesNotExist) {
            continue;
        };

        formulaButtonWidget.addEventListener("click", () => {
            const request = {};
            const quantitiesInputData = buttonData["input"];
            const quantitiesOutputData = buttonData["output"];
            const formula = buttonData["formula"];

            const buttonDataIsNull = areObjectsNull({objects: [quantitiesInputData, quantitiesOutputData, formula]});

            if (buttonDataIsNull) {
                console.log(buttonId);
                return null;
            };

            request["formula"] = formula;
            request["quantities"] = {};

            for (const [inputId, inputData] of Object.entries(quantitiesInputData)) {
                const quantityInputWidget = document.getElementById(inputId);
                const quantityInputValue = quantityInputWidget.value;
                const quantityInputName = inputData["name"];
                const quantityInputMode = inputData["mode"];

                const quantityDataIsNull = areObjectsNull({objects: [quantityInputWidget, quantityInputValue, quantityInputName, quantityInputMode]});

                if (quantityDataIsNull) {
                    return null;
                };

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
            .then(response => {
                const responseDoesNotExist = !response.ok;

                if (responseDoesNotExist) {
                    return null;
                } else {
                    return response.json();
                };
            })
            .then(data => {
                const formulaAnswer = data.answer;
                const formulaAnswerId = quantitiesOutputData["id"];

                const formulaDataIsNull = areObjectsNull({objects: [formulaAnswer, formulaAnswerId]});

                if (formulaDataIsNull) {
                    return null;
                };

                const formulaAnswerWidget = document.getElementById(formulaAnswerId);
                formulaAnswerWidget.textContent = formulaAnswer;
            })
        });
    };
};
