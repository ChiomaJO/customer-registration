const form = document.querySelector("#customerForm");

if (form) {
    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        try {
            const response = await fetch("/register", {
                method: "POST",
                body: new FormData(form)
            });

            const data = await response.json();

            if (!response.ok) {
                alert(data.message || "Registration failed.");
                return;
            }

            alert(data.message || "Registration successful!");
            form.reset();

        } catch (error) {
            console.error(error);
            alert("Registration failed. Please try again.");
        }
    });
}