import { WidgetsIdRegistry, SolverData } from "./config.js";


export function pageSetup() {
    const solverTitleId = WidgetsIdRegistry["SolverTitle"];
    const solverSloganId = WidgetsIdRegistry["SolverSlogan"];
    const solverFooterId = WidgetsIdRegistry["SolverFooter"];

    const solverTitleText = SolverData["SolverTitle"];
    const solverSloganText = SolverData["SolverSlogan"];
    const solverFooterHTML = SolverData["SolverFooter"];

    document.addEventListener("DOMContentLoaded", () => {
        const solverTitleWidget = document.getElementById(solverTitleId);
        const solverSloganWidget = document.getElementById(solverSloganId);
        const solverFooterWidget = document.getElementById(solverFooterId);

        solverTitleWidget.textContent = solverTitleText;
        solverSloganWidget.textContent = solverSloganText;
        solverFooterWidget.innerHTML = solverFooterHTML;
    });
};
