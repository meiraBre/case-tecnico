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
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams({
                    username: email,   // OAuth2 usa 'username' no lugar de email
                    password: password
                })
            });

            if (!res.ok) {
                throw new Error("Usuário ou senha inválidos");
            }

            const data = await res.json();

            // Exemplo: salvando token no localStorage
            localStorage.setItem("token", data.access_token);
            localStorage.setItem("user", email);

            // Redireciona para o dashboard
            window.location.href = "dashboard.html";

        } catch (err) {
            alert(err.message);
        }
    });
});
