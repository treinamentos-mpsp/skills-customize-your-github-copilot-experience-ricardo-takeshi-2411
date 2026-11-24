
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo de adivinhar palavras, onde os jogadores tentam revelar uma palavra oculta letra por letra antes de esgotar as tentativas. Nesta atividade você vai praticar manipulação de strings, loops, condicionais e seleção aleatória, usando entrada de dados do usuário em Python.

## 📝 Tarefas

### 🛠️ Seleção de Palavra e Exibição do Progresso

#### Descrição
Escolha uma palavra aleatória de uma lista predefinida e mostre ao jogador o progresso da palavra, com as letras ainda não descobertas representadas por `_`.

#### Requisitos
O programa concluído deve:

- Selecionar palavras aleatoriamente de uma lista predefinida
- Exibir o progresso atual no formato `_ _ _`, mostrando apenas as letras já adivinhadas


### 🛠️ Palpites e Controle de Tentativas

#### Descrição
Aceite os palpites de letras do jogador, atualize o progresso e controle quantas tentativas incorretas ainda restam.

#### Requisitos
O programa concluído deve:

- Aceitar palpites de letras usando `input()`
- Atualizar o progresso da palavra sempre que a letra estiver correta
- Rastrear o número de tentativas incorretas restantes


### 🛠️ Fim de Jogo

#### Descrição
Defina quando a partida termina e informe o resultado ao jogador.

#### Requisitos
O programa concluído deve:

- Encerrar quando a palavra for totalmente adivinhada ou quando as tentativas se esgotarem
- Exibir uma mensagem de vitória ou de derrota ao final da partida