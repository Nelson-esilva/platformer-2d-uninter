# 🕹️ Platformer 2D - UNINTER

Um jogo de plataforma 2D desenvolvido em Python com a biblioteca [Pygame](https://www.pygame.org/). Este projeto é parte de um exercício acadêmico e possui suporte para **modo singleplayer e cooperativo** (2 jogadores).

---

## 📸 Captura de Tela

> *(adicione aqui uma imagem do jogo, como um GIF ou screenshot)*

---

## 🎮 Como Jogar

### Objetivo
- Derrotar inimigos antes que o tempo acabe
- Evitar ser atingido
- Jogar cooperativamente no modo para 2 jogadores

### Controles

**Player 1**
- `↑ ↓ ← →` — Movimento
- `Ctrl Direito` — Atirar

**Player 2**
- `W A S D` — Movimento
- `Ctrl Esquerdo` — Atirar

### Modos de jogo

- `NEW GAME`: Iniciar uma nova partida (Player 1)
- `COOPERATIVE MODE`: Dois jogadores simultâneos
- `HOW TO PLAY`: Exibe instruções de jogo
- `SCORE`: (Em desenvolvimento)
- `EXIT`: Sai do jogo

---

## 🚀 Executando o Projeto

### Pré-requisitos

- Python 3.10 ou superior
- Pygame

### Opção 1: Executável pronto (recomendado)

Se você está no Windows, basta rodar o executável gerado que está na pasta `dist/`:

bash
./dist/main.py

### Opção 2: Clone o repositório:

bash
git clone -b feature_level https://github.com/Nelson-esilva/platformer-2d-uninter.git
cd platformer-2d-uninter
pip install pygame
python code/Game.py
