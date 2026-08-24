const API_URL = "https://aiojaavvc9.execute-api.us-east-1.amazonaws.com/register";

const form = document.getElementById("customerForm");
const message = document.getElementById("message");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const customer = {
        fullName: document.getElementById("fullName").value.trim(),
        email: document.getElementById("email").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        dateOfBirth: document.getElementById("dateOfBirth").value,
        gender: document.getElementById("gender").value,
        address: document.getElementById("address").value.trim()
    };

    if (
        !customer.fullName ||
        !customer.email ||
        !customer.phone ||
        !customer.dateOfBirth ||
        !customer.gender ||
        !customer.address
    ) {
        message.textContent = "Please complete all fields.";
        return;
    }

    message.textContent = "Sending registration...";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(customer)
        });

        const data = await response.json();

        if (!response.ok) {
            message.textContent =
                data.message || "Registration failed.";
            return;
        }

        message.textContent =
            data.message || "Registration successful!";

        form.reset();

    } catch (error) {
        console.error("AWS ERROR:", error);

        message.textContent =
            "AWS ERROR: " + error.message;
    }
});