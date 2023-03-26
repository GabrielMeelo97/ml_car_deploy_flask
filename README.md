# Desenvolvimento de Modelo de Machine Learning e deploy

Este projeto consiste em um modelo de machine learning desenvolvido no arquivo "notebook/desenvolvendo_modelo.ipynb". O modelo resultante é salvo em um arquivo pickle na pasta "modelo" e pode ser utilizado para fazer predições através de uma interface web construída com Flask.

## Descrição do modelo

O modelo foi desenvolvido utilizando um dataset público de carros disponível em "https://archive.ics.uci.edu/ml/datasets/auto+mpg". O objetivo do modelo é prever o valor estimado do carro com base em atributos como consumo de combustível, cilindros, deslocamento, potência, peso e aceleração.

## Como executar o projeto

Para executar o projeto, siga estas etapas:

1. Clone o repositório para o seu computador
2. Instale as dependências necessárias executando `pip install -r requirements.txt`
3. Certifique-se de que o arquivo pickle do modelo está presente na pasta "modelo"
4. Execute o teste unitário usando o comando `pytest`
5. Execute o arquivo "app.py" usando o comando `python app.py`
6. Abra um navegador da web e navegue até "http://localhost:5000"

## Descrição dos arquivos

- `notebook/desenvolvendo_modelo.ipynb`: este arquivo contém o código usado para treinar e salvar o modelo
- `modelo/modelo.pickle`: este arquivo contém o modelo salvo em formato pickle
- `app.py`: este arquivo contém o código usado para criar a interface web usando Flask e disponibilizar o modelo para fazer predições
- `tests/pickle_test': este arquivo contém um pequeno teste unitário que faz a comparação do modelo gerado pelo jupyter com o resultado modelo pickle.

## Como contribuir

Se você quiser contribuir para este projeto, siga estas etapas:

1. Fork este repositório
2. Crie uma nova branch para suas alterações usando `git checkout -b minha-branch`
3. Faça as alterações necessárias e faça commit das mesmas usando `git commit -am 'Adicionando minha contribuição'`
4. Envie suas alterações usando `git push origin minha-branch`
5. Abra um pull request no repositório original
