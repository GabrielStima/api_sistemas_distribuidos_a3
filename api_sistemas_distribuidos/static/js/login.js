const url = "http://localhost:8000/login"

function handleUnexpectedError(error) {
    document.getElementById("error-info").innerHTML = "Um erro aconteceu por favor contate o suporte";
    document.getElementById("error-container").classList.add("error-container");
    setTimeout(() => {
        document.getElementById("error-container").classList.remove("error-container");
        document.getElementById("error-info").innerHTML = "";
    }, 1500)
    console.error(error);
}

function handleInvalidData(response) {
    document.getElementById("error-info").innerHTML = "Dados invalidos, confira se os dados usados estão corretos";
    document.getElementById("error-container").classList.add("error-container");
    setTimeout(() => {
        document.getElementById("error-container").classList.remove("error-container");
        document.getElementById("error-info").innerHTML = "";
    }, 1500)
    console.error(response);
}

function handleLoginSubmit(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

        window.location.href = "../home/";
}