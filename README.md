# Dash Titanic - Análise de Dados e Previsão de Sobrevivência

## Descrição do Projeto
Este projeto é um dashboard interativo desenvolvido com a biblioteca Dash, que permite a visualização e análise de dados do famoso dataset do Titanic, além de oferecer um formulário para prever a probabilidade de sobrevivência de passageiros com base em suas características. O projeto é dividido em duas páginas principais: uma com gráficos que analisam o dataset e outra com um formulário de previsão de sobrevivência.

## Funcionalidades
- Gráficos Interativos: Análise de dados do Titanic com gráficos interativos, como histograma de idades, boxplot de idades por sobrevivência, taxa de sobrevivência por classe e por sexo.
- Previsão de Sobrevivência: Um formulário onde o usuário pode inserir informações de um passageiro, como idade, sexo, classe, tarifa, número de irmãos/cônjuges e pais/filhos a bordo, e obter uma previsão se o passageiro sobreviveria ao naufrágio.

## Tecnologias Utilizadas

- **Dash**: Framework utilizado para construção de aplicações web interativas e analíticas.
- **Python**: Linguagem de programação utilizada para manipulação de dados e construção da aplicação.
- **Plotly Express**: Biblioteca utilizada para criar gráficos interativos.
- **Pandas**: Utilizada para manipulação de dados e agrupamento de informações.
- **Dash Bootstrap Components (DBC)**: Utilizado para adicionar elementos visuais e estilizar o layout com Bootstrap.
- **Joblib**: Utilizada para carregar o modelo de machine learning previamente treinado.
- **JSON**: Utilizado para carregar o conjunto de dados inicial.

## Como Configurar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:

- Usando HTTPS:
```bash
git clone https://github.com/htadmg/dataset_titanic.git
```
- Usando SSH:
```bash
git clone git@github.com:htadmg/dataset_titanic.git
```
- Navegue até o diretório do projeto:
```bash
cd .\dataset_titanic
```

2. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
- **Para Linux/MacOS:**
```bash
python -m venv .venv
source venv/bin/activate
```
 
- **Para Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```   
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
### Iniciar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento com o comando:

```bash
python .\main.py
```
### Acessar o Projeto
Abra um navegador e vá para http://127.0.0.1:8050/ para ver o aplicativo em funcionamento.

