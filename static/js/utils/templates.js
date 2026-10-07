import { WidgetsIdRegistry, SolverTemplatesData } from "../config/templates.js"


export function pageSetup() {
    const SolverHeaderId = WidgetsIdRegistry["SolverHeader"];
    const solverFooterId = WidgetsIdRegistry["SolverFooter"];

    const SolverHeaderHTML = SolverTemplatesData["SolverHeader"];
    const solverFooterHTML = SolverTemplatesData["SolverFooter"];

    document.addEventListener("DOMContentLoaded", () => {
        const solverHeaderWidget = document.getElementById(SolverHeaderId);
        const solverFooterWidget = document.getElementById(solverFooterId);

        solverHeaderWidget.innerHTML = SolverHeaderHTML;
        solverFooterWidget.innerHTML = solverFooterHTML;
    });
};
