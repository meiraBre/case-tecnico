document.addEventListener("DOMContentLoaded", async () => {
    const token = localStorage.getItem("token");
    const user = localStorage.getItem("user");

    if (!token) {
        alert("Você precisa estar logado!");
        window.location.href = "login.html";
        return;
    }

    document.getElementById("username").textContent = user;

    try {
        const res = await fetch("http://127.0.0.1:8000/metrics?limit=10", {
            headers: { "Authorization": `Bearer ${token}` }
        });

        if (!res.ok) throw new Error("Erro ao buscar dados");

        const data = await res.json();

        const thead = document.getElementById("thead");
        const tbody = document.getElementById("tbody");

        // Monta cabeçalho
        const cols = Object.keys(data.items[0]);
        thead.innerHTML = "<tr>" + cols.map(c => `<th>${c}</th>`).join("") + "</tr>";

        // Monta linhas
        tbody.innerHTML = data.items.map(row =>
            "<tr>" + cols.map(c => `<td>${row[c]}</td>`).join("") + "</tr>"
        ).join("");

    } catch (err) {
        alert(err.message);
    }
});
