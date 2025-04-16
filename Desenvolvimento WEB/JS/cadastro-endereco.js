const url = "https://go-wash-api.onrender.com/api/auth/address"

async function cadastroEndereco() { 
    let title = document.getElementById('title').value;
    let cep = document.getElementById('cep').value;
    let address = document.getElementById('address').value;
    let number = document.getElementById('number').value;
    let complement = document.getElementById('complement').value || "-"

    document.getElementById('title').style.border = "";
    document.getElementById('cep').style.border = "";
    document.getElementById('address').style.border = "";
    document.getElementById('number').style.border = "";
    

    if (title==="") {
        alert("Por favor, preencha o campo Título.");
        document.getElementById('title').style.border = "2px solid red";
        return false;
    }

    if (cep==="") {
        alert("Por favor, preencha o campo CEP.");
        document.getElementById('cep').style.border = "2px solid red";
        return false;
    }

    if (address==="") {
        alert("Por favor, preencha o campo Endereço.");
        document.getElementById('address').style.border = "2px solid red";
        return false;
    }

    if (number==="") {
        alert("Por favor, preencha o campo Número.");
        document.getElementById('number').style.border = "2px solid red";
        return false;
    }

    
    try {
        let token = JSON.parse(localStorage.getItem('user'));
        let api = await fetch(url, { 
            method:"POST",
            body:JSON.stringify(
                {
                    "title": title,
                    "cep": cep,
                    "address": address,
                    "number": number,
                    "complement": complement,
                }
            ),
            headers: {
                'Content-Type':'application/json',
                'Authorization': 'Bearer ' + token.access_token
            } 
        }) 

        if (api.ok) {
            let response = await api.json(); 
            alert('Cadastro de endereço com sucesso')
            window.location="listagem-endereco.html";

        } else {
            alert("Erro ao cadastrar endereço");
        }

    } catch (error) { 
        console.error("Erro", error); 
        alert("Erro:" + error);
    }    
}