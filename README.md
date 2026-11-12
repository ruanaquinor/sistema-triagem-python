# Sistema de Triagem Hospitalar: Fila com Prioridade

## Sobre o Projeto
Este projeto implementa uma **Lista Encadeada Simples** em Python para gerenciar a fila de atendimento de um hospital. O sistema classifica os pacientes por cores e números de cartão, garantindo que casos urgentes sejam atendidos primeiro.

## Funcionalidades e Regras de Negócio
O sistema foi desenvolvido seguindo regras estritas de prioridade:
**Cartões Amarelos (A):** Alta prioridade. São alocados no início da fila, logo após os outros cartões amarelos já existentes. A numeração inicia em 201.
**Cartões Verdes (V):** Baixa prioridade. São inseridos no final da fila (sem prioridade). A numeração inicia em 1.
**Menu Interativo:** Permite adicionar pacientes, imprimir a fila de espera atual, chamar o próximo paciente para atendimento e encerrar o programa.

## Tecnologias Utilizadas
* Python
* Estrutura de Dados: Lista Encadeada Simples

##  Como Executar
1. Execute o arquivo principal via terminal: `python triagem_hospital.py`
2. Utilize o menu numérico (1 a 4) para interagir com o sistema.
3. Ao adicionar um paciente (opção 1), digite `A` para Amarelo ou `V` para Verde.
