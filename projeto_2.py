import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL                 import Image
from io                  import BytesIO


# Set no tema do seaborn para melhorar o visual dos plots
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)
sns.set(context='talk', style='ticks')


# Função para ler os dados
@st.cache(show_spinner= True, allow_output_mutation=True)
def load_data(file_data):
    try:
        return pd.read_csv(file_data)
    except:
        return pd.read_excel(file_data)


def main():
     # Configuração inicial da página da aplicação
     st.set_page_config(
          page_title="Previsão de Renda",
          page_icon="https://travelpedia.com.br/wp-content/uploads/2018/09/dinheiro-icon.png",
          layout="wide",
          initial_sidebar_state='expanded'
     )

     # Título principal da aplicação
     st.write('# Analise Exploratória da Previsão de Renda')
     st.markdown("---")

     # Apresenta a imagem na barra lateral da aplicação
     image = Image.open("dinheiro.jpg")
     st.sidebar.image(image)

     # Botão para carregar arquivo na aplicação
     st.sidebar.write("## Suba o arquivo")
     data_file_1 = st.sidebar.file_uploader("Dados sobre a renda", type = ['csv','xlsx'])

     if (data_file_1 is not None):
          df = load_data(data_file_1)
          df_sem_nulos = df.dropna()

          # Médias GroupBy
          renda_educacao = df.groupby('educacao')[['renda']].mean().round(2)
          renda_sexo = df.groupby('sexo')[['renda']].mean().round(2)
          renda_veiculo = df.groupby('posse_de_veiculo')[['renda']].mean().round(2)
          renda_imovel = df.groupby('posse_de_imovel')[['renda']].mean().round(2)
          renda_tipo = df.groupby('tipo_renda')[['renda']].mean().round(2)
          renda_residencia = df.groupby('tipo_residencia')[['renda']].mean().round(2)

          st.write('## Visualizando o DataFrame')
          st.write(df.head())

          st.write("## Variáveis Categóricas")

          # Plots
          fig = plt.figure(figsize=(18,40))
          gs = fig.add_gridspec(3,3)
          ax0 = fig.add_subplot(gs[0,0])
          ax1 = fig.add_subplot(gs[0,1])
          ax2 = fig.add_subplot(gs[0,2])
          ax3 = fig.add_subplot(gs[1,0])
          ax4 = fig.add_subplot(gs[1,1])
          ax5 = fig.add_subplot(gs[1,2])
          ax6 = fig.add_subplot(gs[2,0])
          ax7 = fig.add_subplot(gs[2,1])
          ax8 = fig.add_subplot(gs[2,2])

          color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

          background_color = '#F8ECE0'
          fig.patch.set_facecolor(background_color) 
          ax0.set_facecolor(background_color) 
          ax1.set_facecolor(background_color) 
          ax2.set_facecolor(background_color) 
          ax3.set_facecolor(background_color) 
          ax4.set_facecolor(background_color) 
          ax5.set_facecolor(background_color) 
          ax6.set_facecolor(background_color) 
          ax7.set_facecolor(background_color) 
          ax8.set_facecolor(background_color) 


          ax0.spines["bottom"].set_visible(False)
          ax0.spines["left"].set_visible(False)
          ax0.spines["top"].set_visible(False)
          ax0.spines["right"].set_visible(False)
          ax0.tick_params(left=False, bottom=False)
          ax0.set_xticklabels([])
          ax0.set_yticklabels([])
          ax0.text(0.5,0.5,
          'Contagem das\nVariáveis Categóricas\n_________________',
          horizontalalignment='center',
          verticalalignment='center',
          fontsize=18, fontweight='bold',
          fontfamily='serif',
          color="#000000")


          # Sexo count
          ax1.text(0.43, 8100, 'Sexo', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax1,data=df_sem_nulos,x='sexo',palette=color_palette)
          ax1.set_xlabel("")
          ax1.set_ylabel("")

          # Posse de veiculo
          ax2.text(0.25, 7300, 'Posse de veiculo', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax2.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax2,data=df_sem_nulos,x='posse_de_veiculo',palette=color_palette)
          ax2.set_xlabel("")
          ax2.set_ylabel("")

          # Posse de imovel
          ax3.text(0, 8850, 'Posse de imovel', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax3.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax3,data=df_sem_nulos,x='posse_de_imovel',palette=color_palette)
          ax3.set_xlabel("")
          ax3.set_ylabel("")

          # Tipo de Renda
          ax4.text(1.3, 8300, 'Tipo de renda', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax4.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax4,data=df_sem_nulos,x='tipo_renda',palette=color_palette)
          ax4.set_xticklabels(labels=['Empresário', 'Assalariado', 'Servidor público', 'Bolsista',
               'Pensionista'], rotation = 45)
          ax4.set_xlabel("")
          ax4.set_ylabel("")

          # Educação
          ax5.text(1.4, 7400, 'Educação', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax5.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax5,data=df_sem_nulos,x='educacao',palette=color_palette)
          ax5.set_xticklabels(labels=['Secundário', 'Superior completo', 'Superior incompleto',
               'Primário', 'Pós graduação'], rotation = 45)
          ax5.set_xlabel("")
          ax5.set_ylabel("")

          # Estado Civil
          ax6.text(1.4, 9300, 'Estado Civil', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax6.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax6,data=df_sem_nulos,x='estado_civil',palette=color_palette)
          ax6.set_xlabel("")
          ax6.set_ylabel("")

          # Tipo de Residencia
          ax7.text(1.5, 11250, 'Tipo de Residencia', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax7.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax7,data=df_sem_nulos,x='tipo_residencia',palette=color_palette)
          ax7.set_xticklabels(labels=['Casa', 'Governamental', 'Com os pais', 'Aluguel', 'Estúdio',
               'Comunitário'], rotation = 45)
          ax7.set_xlabel("")
          ax7.set_ylabel("")

          # Quantidade de Pessoas na Residencia
          ax8.text(0, 6600, 'Quantidade de Pessoas na Residencia', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
          ax8.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.countplot(ax=ax8,data=df_sem_nulos,x='qt_pessoas_residencia',palette=color_palette)
          ax8.set_xlabel("")
          ax8.set_ylabel("")

          lista = ["top","right","left"]
          ax1.spines[lista].set_visible(False)
          ax2.spines[lista].set_visible(False)
          ax3.spines[lista].set_visible(False)
          ax4.spines[lista].set_visible(False)
          ax5.spines[lista].set_visible(False)
          ax6.spines[lista].set_visible(False)
          ax7.spines[lista].set_visible(False)
          ax8.spines[lista].set_visible(False)

          st.pyplot(plt)


          st.write("## Variáveis Contínuas")

          fig = plt.figure(figsize=(18,16))
          gs = fig.add_gridspec(2,2)
          ax0 = fig.add_subplot(gs[0,0])
          ax1 = fig.add_subplot(gs[0,1])
          ax2 = fig.add_subplot(gs[1,0])
          ax3 = fig.add_subplot(gs[1,1])

          color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

          background_color = '#F8ECE0'
          fig.patch.set_facecolor(background_color) 
          ax0.set_facecolor(background_color) 
          ax1.set_facecolor(background_color) 
          ax2.set_facecolor(background_color) 
          ax3.set_facecolor(background_color) 
          ax4.set_facecolor(background_color) 
          ax5.set_facecolor(background_color) 

          ax0.spines["bottom"].set_visible(False)
          ax0.spines["left"].set_visible(False)
          ax0.spines["top"].set_visible(False)
          ax0.spines["right"].set_visible(False)
          ax0.tick_params(left=False, bottom=False)
          ax0.set_xticklabels([])
          ax0.set_yticklabels([])
          ax0.text(0.5,0.5,
               'Contagem das\nVariáveis Categóricas\n_________________',
               horizontalalignment='center',
               verticalalignment='center',
               fontsize=18, fontweight='bold',
               fontfamily='serif',
               color="#000000")

          # Boxen Plot Idade
          ax1.text(-0.045, 69, 'Idade', fontsize=13, fontweight='bold', fontfamily='serif', color='#000000')
          ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.boxenplot(ax=ax1, y=df['idade'], palette=['#FA5858'])
          ax1.set_xlabel('')
          ax1.set_ylabel('')

          # Boxen Plot 
          ax2.text(-0.15, 15, 'Quantidade de Filhos', fontsize=13, fontweight='bold', fontfamily='serif', color='#000000')
          ax2.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.boxenplot(ax=ax2, y=df['qtd_filhos'], palette=['#29088A'])
          ax2.set_xlabel('')
          ax2.set_ylabel('')

          # Boxen Plot Tempo Emprego
          ax3.text(-0.15, 45, 'Tempo Emprego', fontsize=13, fontweight='bold', fontfamily='serif', color='#000000')
          ax3.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
          sns.boxenplot(ax=ax3, y=df['tempo_emprego'], palette=['#0B3B24'])
          ax3.set_xlabel('')
          ax3.set_ylabel('')

          lista = ["top","right","left"]
          ax1.spines[lista].set_visible(False)
          ax2.spines[lista].set_visible(False)
          ax3.spines[lista].set_visible(False)
          ax4.spines[lista].set_visible(False)
          ax5.spines[lista].set_visible(False)

          st.pyplot(plt)

          st.markdown("---")

          st.write('## Média da Renda Conforme:')

          with st.sidebar.form(key='my_form'):
               
               graph_type = st.radio('Média da Renda Conforme::', ('Sexo', 'Posse de Veiculo', 'Posse de Imovel'
                                     , 'Escolaridade', 'Tipo de Renda', 'Tipo de Residencia'))

               submit_button = st.form_submit_button(label='Aplicar')

          if graph_type == 'Escolaridade':
               fig = plt.figure(figsize=(18,8))
               gs = fig.add_gridspec(1,2)
               ax0 = fig.add_subplot(gs[0,0])
               ax1 = fig.add_subplot(gs[0,1])

               color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

               background_color = '#F8ECE0'
               fig.patch.set_facecolor(background_color) 
               ax0.set_facecolor(background_color) 
               ax1.set_facecolor(background_color) 

               ax0.spines["bottom"].set_visible(False)
               ax0.spines["left"].set_visible(False)
               ax0.spines["top"].set_visible(False)
               ax0.spines["right"].set_visible(False)
               ax0.tick_params(left=False, bottom=False)
               ax0.set_xticklabels([])
               ax0.set_yticklabels([])
               ax0.text(0.5,0.5,
                    'Media da Renda\n de acordo com a Escolaridade\n_________________',
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=18, fontweight='bold',
                    fontfamily='serif',
                    color="#000000")

               ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
               sns.barplot(ax=ax1, x=renda_educacao.index, y=renda_educacao.renda)
               ax1.set_xticklabels(labels=['Secundário', 'Superior completo', 'Superior incompleto',
               'Primário', 'Pós graduação'], rotation = 45)
               ax1.set_xlabel('')
               ax1.set_ylabel('')
               lista = ["top","right","left"]
               ax1.spines[lista].set_visible(False)
          
          elif graph_type == 'Sexo':
               fig = plt.figure(figsize=(18,8))
               gs = fig.add_gridspec(1,2)
               ax0 = fig.add_subplot(gs[0,0])
               ax1 = fig.add_subplot(gs[0,1])

               color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

               background_color = '#F8ECE0'
               fig.patch.set_facecolor(background_color) 
               ax0.set_facecolor(background_color) 
               ax1.set_facecolor(background_color) 

               ax0.spines["bottom"].set_visible(False)
               ax0.spines["left"].set_visible(False)
               ax0.spines["top"].set_visible(False)
               ax0.spines["right"].set_visible(False)
               ax0.tick_params(left=False, bottom=False)
               ax0.set_xticklabels([])
               ax0.set_yticklabels([])
               ax0.text(0.5,0.5,
                    'Media da Renda\n de acordo com o Sexo\n_________________',
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=18, fontweight='bold',
                    fontfamily='serif',
                    color="#000000")

               ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
               sns.barplot(ax=ax1, x=renda_sexo.index, y=renda_sexo.renda)
               ax1.set_xlabel('')
               ax1.set_ylabel('')
               lista = ["top","right","left"]
               ax1.spines[lista].set_visible(False)
          
          elif graph_type == 'Posse de Veiculo':
               fig = plt.figure(figsize=(18,8))
               gs = fig.add_gridspec(1,2)
               ax0 = fig.add_subplot(gs[0,0])
               ax1 = fig.add_subplot(gs[0,1])

               color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

               background_color = '#F8ECE0'
               fig.patch.set_facecolor(background_color) 
               ax0.set_facecolor(background_color) 
               ax1.set_facecolor(background_color) 

               ax0.spines["bottom"].set_visible(False)
               ax0.spines["left"].set_visible(False)
               ax0.spines["top"].set_visible(False)
               ax0.spines["right"].set_visible(False)
               ax0.tick_params(left=False, bottom=False)
               ax0.set_xticklabels([])
               ax0.set_yticklabels([])
               ax0.text(0.5,0.5,
                    'Media da Renda\n de acordo com a Posse de Veiculo\n_________________',
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=18, fontweight='bold',
                    fontfamily='serif',
                    color="#000000")

               ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
               sns.barplot(ax=ax1, x=renda_veiculo.index, y=renda_veiculo.renda)
               ax1.set_xlabel('')
               ax1.set_ylabel('')
               lista = ["top","right","left"]
               ax1.spines[lista].set_visible(False)

          elif graph_type == 'Posse de Imovel':
               fig = plt.figure(figsize=(18,8))
               gs = fig.add_gridspec(1,2)
               ax0 = fig.add_subplot(gs[0,0])
               ax1 = fig.add_subplot(gs[0,1])

               color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

               background_color = '#F8ECE0'
               fig.patch.set_facecolor(background_color) 
               ax0.set_facecolor(background_color) 
               ax1.set_facecolor(background_color) 

               ax0.spines["bottom"].set_visible(False)
               ax0.spines["left"].set_visible(False)
               ax0.spines["top"].set_visible(False)
               ax0.spines["right"].set_visible(False)
               ax0.tick_params(left=False, bottom=False)
               ax0.set_xticklabels([])
               ax0.set_yticklabels([])
               ax0.text(0.5,0.5,
                    'Media da Renda\n de acordo com a Posse de Imovel\n_________________',
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=18, fontweight='bold',
                    fontfamily='serif',
                    color="#000000")

               ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
               sns.barplot(ax=ax1, x=renda_imovel.index, y=renda_imovel.renda)
               ax1.set_xlabel('')
               ax1.set_ylabel('')
               lista = ["top","right","left"]
               ax1.spines[lista].set_visible(False)
          
          elif graph_type == 'Tipo de Renda':
               fig = plt.figure(figsize=(18,8))
               gs = fig.add_gridspec(1,2)
               ax0 = fig.add_subplot(gs[0,0])
               ax1 = fig.add_subplot(gs[0,1])

               color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

               background_color = '#F8ECE0'
               fig.patch.set_facecolor(background_color) 
               ax0.set_facecolor(background_color) 
               ax1.set_facecolor(background_color) 

               ax0.spines["bottom"].set_visible(False)
               ax0.spines["left"].set_visible(False)
               ax0.spines["top"].set_visible(False)
               ax0.spines["right"].set_visible(False)
               ax0.tick_params(left=False, bottom=False)
               ax0.set_xticklabels([])
               ax0.set_yticklabels([])
               ax0.text(0.5,0.5,
                    'Media da Renda\n de acordo com o Tipo de Renda\n_________________',
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=18, fontweight='bold',
                    fontfamily='serif',
                    color="#000000")

               ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
               sns.barplot(ax=ax1, x=renda_tipo.index, y=renda_tipo.renda)
               ax1.set_xticklabels(labels=['Empresário', 'Assalariado', 'Servidor público', 'Bolsista',
               'Pensionista'], rotation = 45)
               ax1.set_xlabel('')
               ax1.set_ylabel('')
               lista = ["top","right","left"]
               ax1.spines[lista].set_visible(False)

          elif graph_type == 'Tipo de Residencia':
               fig = plt.figure(figsize=(18,8))
               gs = fig.add_gridspec(1,2)
               ax0 = fig.add_subplot(gs[0,0])
               ax1 = fig.add_subplot(gs[0,1])

               color_palette = ["#800000","#8000ff","#6aac90","#5833ff","#da8829"]

               background_color = '#F8ECE0'
               fig.patch.set_facecolor(background_color) 
               ax0.set_facecolor(background_color) 
               ax1.set_facecolor(background_color) 

               ax0.spines["bottom"].set_visible(False)
               ax0.spines["left"].set_visible(False)
               ax0.spines["top"].set_visible(False)
               ax0.spines["right"].set_visible(False)
               ax0.tick_params(left=False, bottom=False)
               ax0.set_xticklabels([])
               ax0.set_yticklabels([])
               ax0.text(0.5,0.5,
                    'Media da Renda\n de acordo com o Tipo de Residência\n_________________',
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=18, fontweight='bold',
                    fontfamily='serif',
                    color="#000000")

               ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
               sns.barplot(ax=ax1, x=renda_residencia.index, y=renda_residencia.renda)
               ax1.set_xticklabels(labels=['Casa', 'Governamental', 'Com os pais', 'Aluguel', 'Estúdio',
               'Comunitário'], rotation = 45)
               ax1.set_xlabel('')
               ax1.set_ylabel('')
               lista = ["top","right","left"]
               ax1.spines[lista].set_visible(False)
          
          
          st.pyplot(plt)

     
if __name__ == '__main__':
	main()



