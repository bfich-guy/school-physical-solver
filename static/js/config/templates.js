export const WidgetsIdRegistry = {
    "SolverHeader": "solver-header",
    "SolverFooter": "solver-footer",
};


export const SolverTemplatesData = {
    "SolverHeader": `
        <p class="solver-header-text">
            Физмат-калькулятор — все расчёты верны
        </p>
        <div class="solver-header-links">
            <a href="/" class="solver-header-link">
                Главная
            </a>
            <a href="/aboutus" class="solver-header-link">
                О нас
            </a>
        </div>
    `,
    "SolverFooter": `
        <div class="solver-footer-card">
            <p class="solver-footer-card-title">
                Основные страницы
            </p>
            <div class="solver-footer-card-links">
                <a class="solver-footer-link" href="/">
                    Главная
                </a>
                <a class="solver-footer-link" href="/aboutus">
                    О нас
                </a>
            </div>
        </div>
        <div class="solver-footer-card">
            <p class="solver-footer-card-title">
                Школьные предметы
            </p>
            <div class="solver-footer-card-links">
                <a class="solver-footer-link" href="/math/algebra">
                    Алгебра
                </a>
                <a class="solver-footer-link" href="/math/geometry">
                    Геометрия
                </a>
                <a class="solver-footer-link" href="/physics/electromagnetics">
                    Электромагнетизм
                </a>
                <a class="solver-footer-link" href="/physics/mechanics">
                    Механика
                </a>
                <a class="solver-footer-link" href="/physics/thermodynamics">
                    Термодинамика
                </a>
            </div>
        </div>
    `,
};