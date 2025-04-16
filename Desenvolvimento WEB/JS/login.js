const url = "https://go-wash-api.onrender.com/api/login"

async function loginUsuario() { 
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    document.getElementById('email').style.border = "";
    document.getElementById('password').style.border = "";

    if (email==="") {
        alert("Por favor, preencha o campo E-mail.");
        document.getElementById('email').style.border = "2px solid red";
        return false;
    }
    
    if (password==="") {
        alert("Por favor, preencha o campo Senha.");
        document.getElementById('password').style.border = "2px solid red";
        return false;
    } 

    try {         
        let api = await fetch(url, { 
            method:"POST",
            body:JSON.stringify(
                {
                    "email": email,
                    "password": password,
                    "user_type_id": 1,
                }
            ),
            headers: {
                'Content-Type':'application/json',
            } 
        }) 

        if (api.ok) {
            let response = await api.json(); 

            localStorage.setItem('user', JSON.stringify(response));

            window.location="listagem-endereco.html";

        } else {
            let responseErro = await api.json();
            alert(responseErro.data.errors);
        }

    } catch (error) { 
        console.error("Erro", error); 
        alert("Erro:" + error);
    }    
}