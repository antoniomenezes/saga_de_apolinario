# Saga de Apolinário
A saga de apolinário é um jogo onde a história é gerada pelo Gemini e o jogador pode escolher como termina
<img src="app_logo.png" alt="A Saga de Apolinário"> 

### Requisitos

Python 3.6+

É preciso instalar as seguintes bibliotecas em python:
- Biblioteca CustomTkinter (UI) e tkinter-tooltip:
  - pip install customtkinter
  - pip install tkinter-tooltip
 
  Mais informações: https://customtkinter.tomschimansky.com/
  
- Também é necessário criar uma variável de ambiente GEMINI_API_KEY com a API_KEY:
  - No Linux, pode-se usar o comando export GEMINI_API_KEY=<API_KEY>
  - No Windows, basta criar a variável no painel de controle do Windows.
  
### Para executar o jogo
Para executar o jogo basta digitar o seguinte comando: 
- No Linux: python3 saga.py
- No Windows: python.exe saga.py

### Observações
Desculpem quaisquer transtornos e bugs durante a execução. É uma versão pouco testada e foi implementada exclusivamente para a imersão IA da Alura. Futuramente, é possível pensar numa versão web.

### Screenshots
<img src="screenshot.png" alt="Screenshot do jogo no Linux"> 
<img src="screenshot2.png" alt="Screenshot de uma outra história"> 

