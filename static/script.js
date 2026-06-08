document
.getElementById("summarizeBtn")
.addEventListener("click", async () => {

    const text =
    document.getElementById("inputText").value;
    const ratio =
document.getElementById("summaryLevel").value;

    if (!text.trim()) {
        alert("Please enter some content.");
        return;
    }

    document.getElementById("loading").innerText =
    "Generating Summary...";

    const response =
    await fetch("/summarize", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

       body: JSON.stringify({
    text: text,
    ratio: ratio
})

    });

    const data = await response.json();

    document.getElementById("summaryText").value =
    data.summary;

    document.getElementById("loading").innerText = "";

    // Word Count
    const originalWords =
    text.trim().split(/\s+/).length;

    const summaryWords =
    data.summary.trim().split(/\s+/).length;

    // Compression %
    const compression =
    (
        ((originalWords - summaryWords) /
        originalWords) * 100
    ).toFixed(2);

    document.getElementById("originalCount").innerText =
    originalWords;

    document.getElementById("summaryCount").innerText =
    summaryWords;

    document.getElementById("compression").innerText =
    compression + "%";

});

document
.getElementById("copyBtn")
.addEventListener("click", () => {

    const summary =
    document.getElementById("summaryText").value;

    navigator.clipboard.writeText(summary);

    alert("Summary copied successfully!");

});
document
.getElementById("clearBtn")
.addEventListener("click", () => {

    document.getElementById("inputText").value = "";

    document.getElementById("summaryText").value = "";

    document.getElementById("originalCount").innerText = "0";

    document.getElementById("summaryCount").innerText = "0";

    document.getElementById("compression").innerText = "0%";

    document.getElementById("loading").innerText = "";

});