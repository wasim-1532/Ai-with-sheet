const form = document.getElementById("leadForm");

const result = document.getElementById("result");


form.addEventListener("submit", async function(event) {

    event.preventDefault();


    result.style.display = "block";

    result.innerHTML = "Submitting...";


    const data = {

        name: document.getElementById("name").value,

        email: document.getElementById("email").value,

        phone: document.getElementById("phone").value,

        city: document.getElementById("city").value,

        interest: document.getElementById("interest").value,

        message: document.getElementById("message").value

    };


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/submit",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        const resultData = await response.json();


        if (resultData.success) {

            result.innerHTML = `
                <h3>✅ Submitted Successfully</h3>

                <p>
                    Category:
                    ${resultData.ai_analysis.category}
                </p>

                <p>
                    Priority:
                    ${resultData.ai_analysis.priority}
                </p>

                <p>
                    Summary:
                    ${resultData.ai_analysis.summary}
                </p>
            `;

            form.reset();

        } else {

            result.innerHTML =
                "❌ " + resultData.message;

        }

    } catch (error) {

        console.error(error);

        result.innerHTML =
            "❌ Server se connection nahi ho pa raha.";

    }

});