document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const email = form.email.value;
        const password = form.password.value;

        try {
            // Fazendo requisição à API
            const res = await fetch("http://127.0.0.1:8000/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email: email, password: password })
            });

            if (!res.ok) {
                throw new Error("Usuário ou senha inválidos");
            }

            const data = await res.json();

            // Salva email e role no localStorage
            localStorage.setItem("user", email);
            localStorage.setItem("role", data.role);

            // Redireciona para o dashboard
            window.location.href = "dashboard.html";

        } catch (err) {
            alert(err.message);
        }
    });
});

