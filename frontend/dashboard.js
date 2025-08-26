document.addEventListener("DOMContentLoaded", () => {
  const role = localStorage.getItem("role") || "user";

  const orderByEl = document.getElementById("orderBy");
  const startDateEl = document.getElementById("startDate");
  const endDateEl   = document.getElementById("endDate");
  const applyBtn    = document.getElementById("applyFilters"); 
  const statusEl    = document.getElementById("status");
  const thead       = document.getElementById("thead");
  const tbody       = document.getElementById("tbody");      

  async function fetchMetrics() {
    try {
      statusEl.textContent = "Carregando...";
      thead.innerHTML = "";
      tbody.innerHTML = "";

      let url = `http://127.0.0.1:8000/metrics/?role=${encodeURIComponent(role)}&limit=30`;

      const startDate = startDateEl.value; // <input type="date"> → yyyy-mm-dd
      const endDate   = endDateEl.value;

      // Envia separadamente (funciona com só início, só fim ou ambos)
      if (startDate) url += `&start_date=${encodeURIComponent(startDate)}`;
      if (endDate)   url += `&end_date=${encodeURIComponent(endDate)}`;

      const orderBy = orderByEl.value;
      if (orderBy)  url += `&order_by=${encodeURIComponent(orderBy)}`;

      const res = await fetch(url);
      if (!res.ok) throw new Error("Erro ao buscar métricas");

      const data = await res.json();

      if (!Array.isArray(data) || data.length === 0) {
        statusEl.textContent = "⚠ Nenhum dado encontrado para o período selecionado.";
        return;
      }

      // Cabeçalho dinâmico
      const cols = Object.keys(data[0]);
      thead.innerHTML = "<tr>" + cols.map(c => `<th>${c}</th>`).join("") + "</tr>";

      // Linhas (formatando a data)
      tbody.innerHTML = data.map(row =>
        "<tr>" + cols.map(c => {
          let value = row[c];
          if (c === "date" && value) {
            const [y, m, d] = value.split("T")[0].split("-");
            value = `${d}/${m}/${y}`;
          }
          return `<td>${value ?? ""}</td>`;
        }).join("") + "</tr>"
      ).join("");

      statusEl.textContent = `Exibindo ${data.length} registros`;
    } catch (err) {
      console.error(err);
      statusEl.textContent = "❌ Erro ao carregar dados. Tente novamente.";
    }
  }

  // Clique no botão "Aplicar"
  applyBtn.addEventListener("click", fetchMetrics);

  // Carrega na primeira vez
  fetchMetrics();
});





