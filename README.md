# Previsão e Análise de Renda

<p>A partir de uma base de dados, retirada do <a href='www.kaggle.com'>Kaggle</a>, o projeto contém análises sobre Renda familiar. Após as análises é feito dois modelos de regressão, para prever a Renda.</p>

## Descrição do projeto

<p><font size=3>Criar estimativas e elaborar um planejamento financeiro, de acordo com sua renda, faz parte de qualquer pessoa, seja física ou jurídica. Essas tarefas são importantes para definir os objetivos e as ações que devem ser tomadas.</font></p>
<p><font size=3>Ações como prever a renda de um cliente, e assim basear uma campanha de marketing, para ofecer um produto/serviço que ele tenha condições e seja mais propenso a aceitar, ou estimular um limite de concessão de crédito. Existem diversas formas de fazer uso da previsão, e como consequência, aumentar seu lucro, evitar perdas, entre outros benefícios.</font></p>


## Utilização

### Dependencias

Bibliotecas utilizadas no projeto:

matplotlib==3.5.2
matplotlib-inline==0.1.3
numpy==1.22.3
pandas==1.4.2
seaborn==0.11.2
streamlit==1.9.0

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error


### Executando o projeto


O link para o projeto no Heroku: https://previsao-renda.herokuapp.com/

## Ajuda

É de suma importância que durante a execução do projeto, via Heroku, quando for fazer o <code>upload</code> da base de dados, buscar neste mesmo repositória na pasta <b>input</b>, nesse <a hrfe='https://github.com/caioandre182/previsao-analise-venda/blob/main/input/previsao_de_renda.csv'>caminho</a>. 


## Autores
 
ex. [@CaioAndré](https://github.com/caioandre182)

