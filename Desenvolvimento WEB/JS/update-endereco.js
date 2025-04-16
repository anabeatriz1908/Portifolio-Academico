const url = new URLSearchParams(location.search)

let id = url.get("id")

const link = 'https://go-wash-api.onrender.com/api/auth/address/' + id

let token = JSON.parse(localStorage.getItem('user'));
console.log(token);

async function exibir() {
    let api = await fetch(link, {
        method: "GET",
        headers: {
            'Authorization': 'Bearer ' + token.access_token
        }
    });

    let resposta = await api.json()

    document.getElementById('title').value = resposta.data.title;
    document.getElementById('cep').value = resposta.data.cep;
    document.getElementById('address').value = resposta.data.address;
    document.getElementById('number').value = resposta.data.number;
    document.getElementById('complement').value = resposta.data.complement;
}


async function update() {
    let title = document.getElementById('title').value;
    let cep = document.getElementById('cep').value;
    let address = document.getElementById('address').value;
    let number = document.getElementById('number').value;
    let complement = document.getElementById('complement').value || "-";

    try {
        let token = JSON.parse(localStorage.getItem('user'));
        let api = await fetch(link, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token.access_token
            },
            body: JSON.stringify(
                {
                    "title": title,
                    "cep": cep,
                    "address": address,
                    "number": number,
                    "complement": complement,
                }
            )
        })

        let resposta = await api.json()

        if (resposta.data = true) {
            alert('Endereço atualizado com sucesso')
            window.location = "listagem-endereco.html"


        } else {
            alert("Erro ao atualizar endereço");
            console.log(resposta)
        }
    } catch (error) {
        console.log(error)
        alert('Algo deu errado. Informações do Erro: ' + error)
    }
}

exibir()