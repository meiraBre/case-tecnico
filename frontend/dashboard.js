document.addEventListener("DOMContentLoaded", () => {
    const user = localStorage.getItem("user");
    const role = localStorage.getItem("role");

    if (!user) {
        alert("Você precisa estar logado!");
        window.location.href = "login.html";
        return;
    }

    document.getElementById("username").textContent = user;

    const thead = document.getElementById("thead");
    const tbody = document.getElementById("tbody");
    const orderByEl = document.getElementById("orderBy");
    const startDateEl = document.getElementById("startDate");
    const endDateEl = document.getElementById("endDate");
    const applyBtn = document.getElementById("applyFilters");
    const statusEl = document.getElementById("status");
    const logoutBtn = document.getElementById("logoutBtn");

    // Botão de sair
    logoutBtn.addEventListener("click", () => {
        localStorage.clear();
        window.location.href = "login.html";
    });

    // Função para buscar e renderizar métricas
    async function loadMetrics({ order_by = "", start_date = "", end_date = "" } = {}) {
        try {
            statusEl.textContent = "Carregando...";
            tbody.innerHTML = "";
            thead.innerHTML = "";

            // Monta query string
            const params = new URLSearchParams();
            params.set("role", role);
            params.set("limit", 10);
            if (order_by) params.set("order_by", order_by);
            if (start_date) params.set("start_date", start_date);
            if (end_date) params.set("end_date", end_date);

            const res = await fetch(`http://127.0.0.1:8000/metrics?${params.toString()}`);
            if (!res.ok) throw new Error("Erro ao buscar dados");

            const data = await res.json();

            if (data.length === 0) {
                statusEl.textContent = "Nenhum dado encontrado.";
                return;
            }

            // Cabeçalho
            const cols = Object.keys(data[0]);
            thead.innerHTML = "<tr>" + cols.map(c => `<th>${c}</th>`).join("") + "</tr>";

            // Linhas
            tbody.innerHTML = data.map(row =>
                "<tr>" + cols.map(c => `<td>${row[c]}</td>`).join("") + "</tr>"
            ).join("");

            statusEl.textContent = `Exibindo ${data.length} registros`;
        } catch (err) {
            console.error(err);
            alert(err.message);
            statusEl.textContent = "Erro ao carregar dados.";
        }
    }

    // Clique no botão "Aplicar"
    applyBtn.addEventListener("click", () => {
        loadMetrics({
            order_by: orderByEl.value,
            start_date: startDateEl.value,
            end_date: endDateEl.value
        });
    });

    // Carrega na primeira vez
    loadMetrics();
});


