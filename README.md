
# Python Audio Effects 🎧

Este projeto aplica efeitos sonoros a arquivos de áudio, permitindo a criação de duas transformações principais:

1. **Efeito de Reverberação (Voz em Catedral)** 🏰: Simula a reverberação de uma catedral, adicionando profundidade e eco à gravação original.
2. **Efeito de Voz Robótica** 🤖: Modifica a altura da voz (pitch) e aplica uma distorção simples para criar um efeito de voz robótica.

## Funcionalidades

- Aplicar reverberação em áudio para simular um espaço amplo como o de uma catedral.
- Criar vozes robóticas ajustando o pitch e introduzindo distorção.

## Tecnologias Utilizadas

- **Python**
- **Librosa**: Para manipulação do áudio e ajuste de pitch.
- **Scipy**: Para aplicar a convolução na simulação de reverberação.
- **Soundfile**: Para ler e salvar os arquivos de áudio.

## Como Executar

### Pré-requisitos

- **Python 3.x**
- Instalar as dependências:

  ```bash
  pip install librosa scipy soundfile numpy
  ```

### Instruções de Execução por Sistema Operacional

#### Windows
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/thaleson/python_audio_effect.git
   cd python_audio_effect
   ```

2. **Adicione o arquivo de áudio** (ex.: `voz_original.wav`) na pasta do projeto.

3. **Execute o script**:
   - Para o efeito de reverberação (catedral):
     ```bash
     python catedralvoice.py
     ```
   - Para o efeito de voz robótica:
     ```bash
     python robotvoice.py
     ```

4. Os resultados serão salvos como `catedral.wav` (efeito de catedral) e `voz_robotica.wav` (efeito robótico).

#### Linux/macOS

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/thaleson/python_audio_effect.git
   cd python_audio_effect
   ```

2. **Adicione o arquivo de áudio** (ex.: `voz_original.wav`) na pasta do projeto.

3. **Garanta permissões de execução** (Linux/macOS):
   ```bash
   chmod +x *.py
   ```

4. **Execute o script**:
   - Para o efeito de reverberação (catedral):
     ```bash
     python3 catedralvoice.py
     ```
   - Para o efeito de voz robótica:
     ```bash
     python3 robotvoice.py
     ```

5. Os resultados serão salvos como `catedral.wav` (efeito de catedral) e `voz_robotica.wav` (efeito robótico).

### Exemplos de Uso

- **Áudio com reverberação**:
   Simula espaços amplos como catedrais ou salas grandes.
  
- **Áudio robótico**:
   Cria vozes mecânicas, futuristas e distorcidas para efeitos de ficção científica.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

