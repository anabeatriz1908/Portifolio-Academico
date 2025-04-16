function cadastro() {
    window.location.href = "cadastro-endereco.html"
}

function retorno() {
    window.location.href = "home-site.html"
}

async function listagemEndereco() {
    let url = 'https://go-wash-api.onrender.com/api/auth/address'
    let token = JSON.parse(localStorage.getItem('user'))
    console.log(token);

    try {
        let api = await fetch(url, {
            method: "GET",
            headers: {
                'Authorization': 'Bearer ' + token.access_token
            }
        });

        let resposta = await api.json()
        let tbody = document.querySelector('tbody')
        let row = ""

        resposta.data.forEach((endereco) => {
            row += `<tr>
                        <th>${endereco.id}</th>
                        <th>${endereco.title}</th>
                        <th>${endereco.cep}</th>
                        <th>${endereco.address}</th>
                        <th>${endereco.number}</th>
                        <th>${endereco.complement}</th>
                        <th>
                        <input type="button" value="Atualizar" onclick="update(${endereco.id})"/>
                        <input type="button" value="Deletar" onclick="deletar(${endereco.id})"/>
                        </th>
                    </tr>`
        });

        tbody.innerHTML = row

    } catch (error) {
        console.log(error)
        alert('Algo deu errado. Informações do Erro: ' + error)
    }

}

listagemEndereco()


function update(id) {
    window.location.href = "update-endereco.html?id=" + id
}

async function deletar(id) {
    let url = 'https://go-wash-api.onrender.com/api/auth/address/' + id
    let token = JSON.parse(localStorage.getItem('user'));
    console.log(token);
    try {
        let api = await fetch(url, {
            method: "DELETE",
            headers: {
                'Authorization': 'Bearer ' + token.access_token
            }
        });

        if (api.ok) {
            alert('Endereço excluido com sucesso')
            window.location = "listagem-endereco.html"

        } else {
            let responseErro = await api.text();
            console.log("Resposta de erro da API:", responseErro);
            alert("Erro ao excluir endereço");
        }
    }

    catch (error) {
        console.error('Erro inesperado: ', error);
        alert('Algo deu errado. Informações do Erro: ' + error)
    }
}

async function logout() {
    let url = 'https://go-wash-api.onrender.com/api/auth/logout'
    let token = localStorage.getItem('access_token');
    console.log(token);

    try {
        let api = await fetch(url, {
            method: "POST",
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            }
        });

        if (api.ok) {
            let response = await api.json();
            console.log('Resposta da API:', response);

            localStorage.removeItem("access_token");
            localStorage.removeItem("user");
            
            window.location = "login.html";

        } else {
            console.error('Erro na conexão:', error);
            alert("Erro ao fazer logout");
        }
    }

    catch (error) {
        console.error("Erro", error);
        alert("Erro:" + error);
    }
}