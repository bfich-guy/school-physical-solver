import { WidgetsIdRegistry, SolverData } from "./config.js";


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
