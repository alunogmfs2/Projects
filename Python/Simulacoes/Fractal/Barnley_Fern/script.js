"use script"


function submitForm() {
    let name = document.getElementById("name")
    let p = document.createElement("p")
    p.textContent = "Hallo, " + name.value + "!"
    document.body.appendChild(p)
}

