async function generateText() {
    const prompt = document.getElementById("prompt").value;
    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    document.getElementById("result").innerText = data.response;
}