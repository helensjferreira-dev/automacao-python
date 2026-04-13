[🇧🇷 Portuguese](#-portuguese) | [🇺🇸 English](#-english)

---

## 🇧🇷 Português

Projeto de Iniciação (Junho/2025) - Revisado e Atualizado (Abril/2026)

# 🖥️ Automação de Cadastro de Produtos

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-v0.9.54-blue?style=for-the-badge)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

Este projeto automatiza o **cadastro massivo** de produtos em um sistema web. Utilizando a biblioteca **PyAutoGUI**, o script emula o comportamento humano para preencher formulários a partir de uma base de dados externa em CSV, otimizando tarefas repetitivas e eliminando erros de digitação manual.

### 🎯 O Desafio de Negócio

Muitas empresas utilizam sistemas que não possuem APIs de integração. Nestes cenários, a automação de interface (RPA) é a solução mais eficiente para transferir grandes volumes de dados de planilhas para o sistema de gestão de forma rápida.

---

### 🚀 Funcionalidades

- Leitura Dinâmica: Percorre todas as linhas do CSV utilizando o índice do DataFrame.

- Tratamento de Exceções: Verificação de valores nulos (NaN) no campo de observações.

- Mecanismo de Failsafe: Pausas estratégicas e interrupção de emergência movendo o mouse para o canto superior esquerdo.

- Navegação Inteligente: Uso de comandos `tab`, `enter` e rolagem automática (`scroll`).

---

### 📂 Estrutura do Projeto

```text
automacao-python/
│
├── inicial.py          # Script principal que executa a automação
├── auxiliar.py         # Script para captura de coordenadas (x, y)
│
├── static/             # Arquivos estáticos
│   ├── style.css       # Estilos da página
│   └── script.js       # Lógica dos formulários
│
├── templates/          # Páginas HTML
│   ├── index.html      # Tela de login
│   └── products.html   # Tela de cadastro de produtos
│
├── data/               # Dados para automação
    ├── products.csv            # Arquivo com 50 produtos
    └── products_sample.csv     # Arquivo com 9 produtos para teste
├── requirements.txt     # Bibliotecas necessárias para rodar o projeto
└── README.md            # Documentação completa 
```

---

## ⚙️ Como Executar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/helensjferreira-dev/automacao-python.git

   ```

2. Instale as dependências:

   ```bash
   pip install pyautogui

   ```

3. Execute o script principal:

   ```bash
   python inicial.py

   ```

4. O script abrirá a página `products.html` e começará a preencher os produtos automaticamente.

### 🧪 Testes

- Use o arquivo `products_sample.csv` para rodar testes rápidos com apenas 10 produtos.

- Para rodar a automação completa, utilize `products.csv` com 50 produtos.

  ⚠️ Observação Importante sobre Calibração:
  Este script de automação foi desenvolvido e calibrado sob as seguintes condições de hardware e software:
  - Resolução de Tela: 1366x768 (HD).
  - Escala do Windows: 100%.
  - Zoom do Navegador (Chrome): 100%.
  - Modo de Janela: Navegador maximizado.

  Como o PyAutoGUI utiliza coordenadas absolutas de pixels, se a sua configuração for diferente, o script poderá clicar fora dos campos do formulário.
  Caso precise recalibrar:
  1. Execute o script auxiliar.py incluído neste repositório.
  2. Posicione o mouse sobre os campos desejados para capturar as novas coordenadas $(x, y)$.
  3. Atualize os valores correspondentes no arquivo inicial.py.

   Após iniciar o script, certifique-se de que a janela do navegador esteja em primeiro plano para que as coordenadas de clique sejam aplicadas corretamente.

### 🌐 Demonstração Online (GitHub Pages)

Para facilitar a visualização da interface e a compreensão do fluxo de automação, a página inicial está disponível online:
🔗[Acesse o Formulário de Teste aqui]("https://helensjferreira-dev.github.io/automacao-python/templates/index.html")

    Nota: Esta página foi desenvolvida exclusivamente para exemplificar o funcionamento da automação. Após o preenchimento simulado do login, você será redirecionado para a tela de cadastro de produtos (products.html), onde a tabela dinâmica exibe os itens processados.

### 🛠️ Tecnologias e Ferramentas

- Python 3.10

- PyAutoGUI → automação de teclado e mouse

- OS / Webbrowser → manipulação de caminhos e abertura de páginas HTML

- HTML5 / CSS3 / JavaScript → interface de login e cadastro de produtos

- Pandas: Manipulação e leitura de arquivos csv de produtos.

### 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 🇺🇸 English

Initiation Project (June/2025) - Reviewed and Updated (April/2026)

# 🖥️ Product Registration Automation

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-v0.9.54-blue?style=for-the-badge)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

This project automates the **bulk registration** of products in a web system. Using the **PyAutoGUI** library, the script emulates human behavior to fill out forms from an external CSV database, optimizing repetitive tasks and eliminating manual typing errors.

### 🎯 Business Challenge

Many companies use systems that lack integration APIs. In these scenarios, Robotic Process Automation (RPA) is the most efficient solution for quickly transferring large volumes of data from spreadsheets to the management system.

---

### 🚀 Features

- Dynamic Reading: Iterates through all CSV rows using the DataFrame index.

- Exception Handling: Verification of null values (NaN) in the remarks field.

- Failsafe Mechanism: Strategic pauses and emergency interruption by moving the mouse to the top-left corner of the screen.

- Smart Navigation: Use of `tab`, `enter` commands and automatic scrolling (`scroll`).

---

### 📂 Project Structure

```text
automacao-python/
│
├── inicial.py          # Main script that executes the automation
├── auxiliar.py         # Script to capture (x, y) coordinates
│
├── static/             # Static files
│   ├── style.css       # Page styles
│   └── script.js       # Form logic
│
├── templates/          # HTML pages
│   ├── index.html      # Login screen
│   └── products.html   # Product registration screen
│
├── data/               # Data for automation
    ├── products.csv            # File with 50 products
    └── products_sample.csv     # File with 9 products for testing
├── requirements.txt     # Required libraries to run the project
└── README.md            # Full documentation
```

---

## ⚙️ How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/helensjferreira-dev/automacao-python.git

   ```

2. Install dependencies:

   ```bash
   pip install pyautogui

   ```

3. Run the main script:

   ```bash
   python inicial.py

   ```

4. The script will open the `products.html` page and begin filling in the products automatically.

### 🧪 Testing

- Use the `products_sample.csv` file to run quick tests with only 10 products.

- To run the full automation, use `products.csv` with 50 products.

  ⚠️ Important Note on Calibration:
  This automation script was developed and calibrated under the following hardware and software conditions:
  - Screen Resolution: 1366x768 (HD).
  - Windows Scaling: 100%.
  - Browser Zoom (Chrome): 100%.
  - Window Mode: Maximized browser.

  Since PyAutoGUI uses absolute pixel coordinates, if your settings differ, the script may click outside the form fields.
  If you need to recalibrate:
  1. Run the auxiliar.py script included in this repository.
  2. Position the mouse over the desired fields to capture the new $(x, y)$ coordinates.
  3. Update the corresponding values in the inicial.py file.

   After running the script, ensure the browser window is in the foreground. If the focus remains on VS CODE, the automation may fail. You can click on the browser icon in the taskbar during the initial `time.sleep` period to guarantee the correct window is active before the clicks begin. 

### 🌐 Online Demo (GitHub Pages)

To facilitate the visualization of the interface and the understanding of the automation flow, the home page is available online:
🔗[Access the Test Form here]("https://helensjferreira-dev.github.io/automacao-python/templates/index.html")

    Nota: This page was developed exclusively to demonstrate the automation functionality. After the simulated login, you will be redirected to the product registration screen (products.html), where the dynamic table displays the processed items.

### 🛠️ Technologies and Tools

- Python 3.10

- PyAutoGUI → keyboard and mouse automation

- OS / Webbrowser → path manipulation and opening HTML pages

- HTML5 / CSS3 / JavaScript → login and product registration interface

- Pandas: Manipulation and reading of product CSV files.

### 📄 License

This project is under the MIT license. See the LICENSE file for more details.

---

👤 Author / Autora  
Hélen Ferreira – Developer  
📸 [Linkedin](https://www.linkedin.com/in/helensjferreira-dev/)  
💬 [WhatsApp](https://wa.me/5548988183720)  
🔗 [GitHub](https://github.com/helensjferreira-dev/)
