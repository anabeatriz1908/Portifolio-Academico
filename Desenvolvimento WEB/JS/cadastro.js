const url = "https://go-wash-api.onrender.com/api/user"

async function cadastroUsuario() {
    let name =  document.getElementById('name').value;
    let email =  document.getElementById('email').value;
    let birthday =  document.getElementById('birthday').value;
    let terms =  document.getElementById('terms').checked;  
    let password = document.getElementById('password').value;
    let cpf_cnpj = document.getElementById('cpf_cnpj').value;

    document.getElementById('name').style.border = "";
    document.getElementById('email').style.border = "";
    document.getElementById('birthday').style.border = "";
    document.getElementById('terms').style.border = "";
    document.getElementById('password').style.border = "";
    document.getElementById('cpf_cnpj').style.border = "";

    if (name==="") {
        alert("Por favor, preencha o campo Nome.");
        document.getElementById('name').style.border = "2px solid red";
        return false;
    }

    if (email==="") {
        alert("Por favor, preencha o campo E-mail.");
        document.getElementById('email').style.border = "2px solid red";
        return false;
    }

    if (birthday==="") {
        alert("Por favor, preencha o campo Data de Nascimento.");
        document.getElementById('birthday').style.border = "2px solid red";
        return false;
    }

    if (!terms) {
        alert("Você não concordou com o Termo de Uso.");
        document.getElementById('terms').style.border = "2px solid red";
        return false;
    }
    
    if (password==="") {
        alert("Por favor, preencha o campo Senha.");
        document.getElementById('password').style.border = "2px solid red";
        return false;
    } 

    if (password.length < 6) {
        alert("Sua senha precisa ter pelo menos 6 dígitos.");
        document.getElementById('password').style.border = "2px solid red";
        return false;
    } 

    if (cpf_cnpj===""){
        alert("Por favor, preencha o campo CPF ou CNPJ");
        document.getElementById('cpf_cnpj').style.border = "2px solid red";
        return false;
    }

    console.log("Nome: " + name);
    console.log("Email: " + email);
    console.log("Data de Nascimento: " + birthday);
    console.log("Termos aceitos: " + terms);

    try { 
        let api = await fetch(url, { 
            method:"POST",
            body:JSON.stringify(
                {
                    "name": name,
                    "email": email,
                    "user_type_id":1,
                    "password": password,
                    "cpf_cnpj": cpf_cnpj,
                    "terms": terms,
                    "birthday":birthday
                }
            ),
            headers: {
                'Content-Type':'application/json'
            } 
        }) 

        if (api.ok) {
            let response = await api.json();
            console.log(response);
            alert("Cadastro realizado com sucesso!")
            alert("Enviamos um link de ativação para o seu e-mail!");
            window.location="home-site.html";
            return;

        } else {
            let responseErro = await api.json();
            console.log("Resposta de erro da API:", responseErro);
            if (responseErro.data && responseErro.data.errors) {
                if (responseErro.data.errors.cpf_cnpj) {
                    console.log("Esse CPF ou CNPJ já foi cadastrado!");
                    alert("Esse CPF ou CNPJ já foi cadastrado!")
                }
                if (responseErro.data.errors.email) {
                    console.log("Esse email já foi cadastrado!");
                    alert("Esse email já foi cadastrado!");
                }
            } else {
                console.error("Erro na resposta da API:", responseErro);
                alert("Erro ao realizar o cadastro: " + (responseErro.message || "Erro desconhecido"));
            }
        }

    } catch (error) {
        console.error("Erro na requisição:", error);
        alert("Erro ao conectar com o servidor. Por favor, tente novamente.");
    }    

}