# AllerGenie

AllerGenie é um aplicativo voltado para pessoas com restrições alimentares, como alergias ou intolerâncias. O objetivo é proporcionar uma experiência segura e personalizada, conectando clientes a restaurantes que oferecem opções de pratos adequados para suas necessidades.

---

## 🌟 Funcionalidades

### 💼 Clientes

* Sistema completo de CRUD (Criar, Ler, Atualizar e Deletar conta)
* Pesquisa por:

  * Palavras-chave
  * Pratos
  * Localização
  * Restaurantes
* Opção de "Editar perfil" com os seguintes campos:

  * Alergias
  * Cidade

### 🏡 Restaurantes/Empresas

* Sistema completo de CRUD
* Opções no menu para:

  * Adicionar prato (nome, descrição, palavras-chave, preço)
  * Adicionar dados do restaurante (cidade, descrição, palavras-chave)

---

## 📄 Estrutura do Projeto

O sistema é desenvolvido em Python e armazena os dados dos usuários (clientes e restaurantes) em arquivos `.json`. Isso inclui informações de perfil, cardápios e filtros de pesquisa.

---

## 📖 Bibliotecas

### 🔐 `pwinput`

* **Descrição:**
  Biblioteca para capturar senhas ou entradas de forma oculta no terminal. Excelente para proteção de dados sensíveis.

* **Instalação:**

  ```bash
  py -m pip install pwinput
  ```

* **Exemplo:**

  ```python
  import pwinput
  senha = pwinput.pwinput("Digite sua senha: ")
  ```

---

### 🧮 `hashlib`

* **Descrição:**
  Biblioteca usada para criptografar dados (como senhas) usando algoritmos de hash como SHA-256. Ajuda a proteger informações sensíveis.

* **Instalação (caso necessário):**

  ```bash
  py -m pip install hashlib
  ```

  Obs: `hashlib` já está incluído por padrão no Python.

* **Exemplo:**

  ```python
  import hashlib
  senha = "minha_senha123"
  hash_senha = hashlib.sha256(senha.encode()).hexdigest()
  print(hash_senha)
  ```

# 📊 Fluxogramas do Projeto

Este projeto possui diversos fluxogramas criados para ilustrar e organizar o fluxo de funcionalidades principais. Abaixo estão os links para acesso rápido a cada um deles no Miro:

## ✅ Página Inicial
🔗 [Acessar fluxograma](https://miro.com/app/board/uXjVI1VTWdY=/?share_link_id=363574602305)

## ✅ Create Empresa
🔗 [Acessar fluxograma](https://miro.com/app/board/uXjVI1VAO8I=/?share_link_id=41309087508)

## ✅ Create Cliente
🔗 [Acessar fluxograma](https://miro.com/app/board/uXjVI0UP6_A=/?share_link_id=73213188831)

## ✅ Login
🔗 [Acessar fluxograma](https://miro.com/app/board/uXjVIvukS1k=/?share_link_id=246721087919)

## ✅ Menu Restaurante
🔗 [Acessar fluxograma](https://miro.com/app/board/uXjVIvG45zE=/?share_link_id=148354674661)

## ✅ Menu Cliente
🔗 [Acessar fluxograma](https://miro.com/app/board/uXjVIvu0y1g=/?share_link_id=842835422224)

## ✅ Pesquisa
🔗 [Acessar fluxograma](https://miro.com/app/board/uXjVIvGquwY=/?share_link_id=880846900225)


## 📂 Link Alternativo: Fluxogramas no Google Drive

Se preferir, você também pode acessar todos os fluxogramas diretamente pelo Google Drive:

🔗 [Acessar pasta com os fluxogramas no Drive](https://drive.google.com/drive/folders/1v_Ecn46yD4etBd9W9wpEXHmRZ9VWXDsR?usp=sharing)

## ℹ️ Observação
Todos os fluxogramas são de visualização pública via Miro e Google Drive, garantindo fácil acesso para consulta e colaboração.


Feito por Carlos Batista e Luan Marcos<br>Sistema de Informação - UFRPE
