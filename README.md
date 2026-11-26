# 🎰 Cassino DGRV

Projeto desenvolvido para a disciplina de **Estrutura de Dados**, com o objetivo de aplicar na prática os conceitos e estruturas estudados em sala por meio de uma aplicação interativa em **Python** rodando no terminal.

## 📌 Sobre o Projeto

O **Cassino DGRV** é uma central de jogos de cassino modularizada. A aplicação conta com um **Hub Principal** (`Hub.py`) que reúne e executa diferentes jogos independentes desenvolvidos pelos integrantes da equipe, cada um explorando estruturas de dados específicas para resolver problemas reais da sua mecânica (como controle de turnos, histórico de sorteios, sistema de desfazer apostas, validação de entradas e tabelas de pagamentos).


## 🧠 Resumo das Estruturas de Dados Utilizadas

| Jogo | Integrante | Estruturas e recursos |
|---|---|---|
| Blackjack (21) | Grazielli | Fila (`Queue`), pilha (`Stack`), dicionários, tuplas, conjunto (`set`) e listas |
| Roleta | Ricardo | Fila (`Queue`), tuplas, conjuntos (`set`) e listas |
| Bac Bo | Davi | Fila (`Fila`), pilha (`Pilha`), tuplas, dicionários e listas |
| Vini 1 | Vinícius | Fila (`Queue`), pilha (`Stack`), Max Heap, HeapSort, dicionários, tuplas e listas |

---

## 🎮 Jogos Disponíveis e Recursos Técnicos

### 1. ♠️ Blackjack (21) — *Grazielli*
Clássico jogo de cartas em que o objetivo é somar o mais próximo possível de 21 pontos sem ultrapassar esse limite, enfrentando o Dealer.
---

### 2. 🎡 Roleta — *Ricardo*
Simulação de uma mesa de roleta europeia (números de 0 a 36), permitindo apostar tanto na cor quanto no número exato sorteado.
---

### 3. 🎲 Bac Bo — *Davi*
Jogo de dados inspirado no Bacará, no qual o jogador aposta no duelo entre **Player (Azul)** e **Banker (Vermelho)** ou no **Tie (Empate)**, onde cada lado lança dois dados.
---

### 4. 🃏 Vini 1 — *Vinícius*
Jogo de cartas em que os participantes trocam cartas para alcançar a maior pontuação possível sem ultrapassar 21, utilizando estratégias de descarte e desempate. 
---

## 🧩 Hub Principal e Integração

O arquivo `Hub.py` atua como porta de entrada do **Cassino DGRV**, utilizando:
* **`logos.py`:** Módulo compartilhado responsável pelos banners em arte ASCII do Hub e dos jogos.
* **`subprocess` e `sys`:** Executam os jogos de cada integrante mantendo os scripts isolados em suas respectivas pastas.
* **`pathlib`:** Garante a resolução correta dos diretórios e importações entre a pasta raiz e as subpastas do projeto.

---

## ▶️ Como Executar

### Pré-requisitos
* **Python 3.12+** instalado.
* **Nenhuma biblioteca externa é necessária** — todo o projeto utiliza apenas módulos nativos do Python (`random`, `time`, `os`, `sys`, `subprocess`, `pathlib`).

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/junetheraven/cassinoDGRV
   ```
2. Acesse a pasta principal do projeto:
   ```bash
   cd cassinoDGRV
   ```
3. Execute o Hub do cassino:
   ```bash
   python Hub.py
   ```
4. Escolha o número do jogo desejado no menu e divirta-se!

---
