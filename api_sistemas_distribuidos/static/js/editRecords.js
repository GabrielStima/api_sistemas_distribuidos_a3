const url = "http://localhost:8000/editRecords"
const params = new URLSearchParams(document.location.search);
const type = params.get("type");
const id = params.get("id");


function editRecord() {
    const fields = document.querySelectorAll(".form-group input");
    fields.forEach(element => element.disabled = false);
    actionButtons(true);
}

function cancelEdit() {
    const fields = document.querySelectorAll(".form-group input");
    fields.forEach(element => element.disabled = true);
    actionButtons(false);
}

function updateRecord(token) {
    const fields = document.querySelectorAll(".form-group input");
    let update = {};
    fields.forEach(element => {
        update[element.id] = element.value
    });

    if (type === 'customer') {
        fetch(`${url}/customer/${id}`, {
            method: "PATCH",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({ ...update })
        }).then(async res => {
            if (!res.ok) {
                if (res.status === 401) {
                    window.location.pathname = '../login/';
                }
                console.error('asdasdasdasdasdas', res);
            } else {
                window.location.pathname = '../customers';
            }
        })
    }
    if (type === 'product') {
        fetch(`${url}/product/${id}`, {
            method: "PATCH",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({ ...update })
        }).then(async res => {
            if (!res.ok) {
                console.error('Error', res);
            } else {
                window.location.pathname = '../products';
            }
        })
    }
    if (type === 'store') {
        fetch(`${url}/store/${id}`, {
            method: "PATCH",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({ ...update })
        }).then(async res => {
            if (!res.ok) {
                console.error('Error', res);
            } else {
                window.location.pathname = '../stores';
            }
        })
    }
    if (type === 'user') {
        fetch(`${url}/user/${id}`, {
            method: "PATCH",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({ ...update })
        }).then(async res => {
            if (!res.ok) {
                console.error('Error', res);
            } else {
                window.location.pathname = '../users';
            }
        })
    }
}

function createRecord() {
    const fields = document.querySelectorAll(".form-group input");
    let record = {};
    fields.forEach(element => {
        record[element.id] = element.value
    });

    if (type === 'customer') {
        fetch(`${url}/customer`, {
            method: "POST",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ ...record })
        }).then(async res => {
            if (!res.ok) {
                if (res.status === 401) {
                    window.location.pathname = '../login/';
                }
                console.error('Error', res);
            } else {
                const customer = await res.json();
                window.location.href += `&id=${customer.id}`;
            }
        })
    }
    if (type === 'product') {
        fetch(`${url}/product/${id}`, {
            method: "POST",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ ...record })
        }).then(async res => {
            if (!res.ok) {
                if (res.status === 401) {
                    window.location.pathname = '../login/';
                }
                console.error('Error', res);
            } else {
                const product = await res.json();
                window.location.href += `&id=${product.id}`;
            }
        })
    }
    if (type === 'store') {
        fetch(`${url}/store/${id}`, {
            method: "POST",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ ...record })
        }).then(async res => {
            if (!res.ok) {
                if (res.status === 401) {
                    window.location.pathname = '../login/';
                }
                console.error('Error', res);
            } else {
                const store = await res.json();
                window.location.href += `&id=${store.id}`;
            }
        })
    }
    if (type === 'user') {
        fetch(`${url}/user/${id}`, {
            method: "POST",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ ...update })
        }).then(async res => {
            if (!res.ok) {
                if (res.status === 401) {
                    window.location.pathname = '../login/';
                }
                console.error('Error', res);
            } else {
                const user = await res.json();
                window.location.href += `&id=${user.id}`;
            }
        })
    }
}

function actionButtons(toggle) {
    const actions = document.querySelector("#actions");
    if (!toggle) {
        if (document.querySelector("#cancelAction")) {
            document.querySelector("#cancelAction").style ="display:none";
            document.querySelector("#updateAction").style ="display:none";
            document.querySelector("#editAction").style ="display:block";
        }
        // actions.insertAdjacentHTML('beforeend', `<button id="editAction" onclick="editRecord()">Editar Registro</button>`);
    } else {
        if (document.querySelector("#editAction")) {
            document.querySelector("#editAction").style ="display:none";
            document.querySelector("#cancelAction").style ="display:block";
            document.querySelector("#updateAction").style ="display:block";
        }
        // actions.insertAdjacentHTML('beforeend', 
        // `
        // <button id="cancelAction" onclick="cancelEdit()">Cancelar</button>
        // <button id="updateAction">Atualizar Registro</button>
        // `);
    }
}