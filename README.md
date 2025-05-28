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


Feito por Carlos Batista e Luan Marcos<br>Sistema de Informação - UFRPE
