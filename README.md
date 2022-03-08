# Previsão da Evolução do vírus Covid-19

Algoritmo para prever a evolução do contágio do Covid-19 no mundo utilizando regressão linear, mais especificamente o cálculo de [Ordinary Least Squares](https://en.wikipedia.org/wiki/Ordinary_least_squares). Esse método basicamente encontra uma maneira de encaixar uma reta no dataset bidimensional, quando encontramos essa reta somos capazes de montar sua fórmula para calcular os valores na reta, com esses valores podemos basicamente "prever" o futuro porque são valores próximos. Para fazer esse algoritmo, tive o auxílio, sobretudo, da biblioteca `statsmodels` que facilitou o cálculo de `OLS`.

## Sumário
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Testes unitários](#testes-unitários)
- [Links](#links)

### Pré-requisitos

  1. Python3.8 ou mais recente em virtude da biblioteca `pandas` e `statsmodels`

### Instalação

  1. Crie um ambiente virtual (Passo opcional, caso queira instale os pacotes globalmente)

     ```bash
     python -m venv env && source env/bin/activate
     ```

  2. Instale todas as dependências necessárias
     ```
     pip install -r requirements.txt
 	   ```

### Uso

```bash
python forecaster.py
```

### Testes unitários

```bash
python forecaster_test.py
```

### Links

Aqui estão os links que me ajudaram no processo da criação do algoritmo:
   - [3.2: Linear Regression with Ordinary Least Squares Part 1 - Intelligence and Learning](https://www.youtube.com/watch?v=szXbuO3bVRk)
   - [Modeling Exponential Growth](https://towardsdatascience.com/modeling-exponential-growth-49a2b6f22e1f#_=) 
   - [Example Method of Least Squares](https://www.emathzone.com/tutorials/basic-statistics/example-method-of-least-squares.html)
