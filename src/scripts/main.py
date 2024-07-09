import pandas as pd
import os 
import glob

# caminho para ler os caminhos
folder_path  = './src/data/raw'

# lista todos os arquivos de excel
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Nenuhum arquivo compativel encontado")
else:
    # dataframe = tabela na memária para guardar os conteúdos  dos arquivos
    dfs = []

for excel_file in excel_files:

    try:
        # lê o camiho do excel 
        df_temp = pd.read_excel(excel_file)
        print(type(df_temp))
        # pegar o nome do arquivo
        file_name =  os.path.basename(excel_file)
        
        df_temp['filename'] = file_name

        # criaçã ode uma nova coluna location
        if 'brasil'  in file_name.lower():
            df_temp['location'] = 'br'
        elif 'france' in file_name.lower():
            df_temp['location'] = 'fr'
        elif 'italian' in file_name.lower():
            df_temp['location'] = 'it'

        #criação uma nova coluna chmada campaign
        df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
        
        # guarda dados tratados dentro de um dataframe comum
        dfs.append(df_temp)

    except Exception as e:
        print(f"erro ao ler o arquivo {excel_file}: {e}")

if dfs:

    #Concatena todas as tabels salvas  no dfs em uma unica tabela
    result = pd.concat(dfs, ignore_index=True)

    output_file = os.path.join('src','data', 'ready','clean.xlsx')

    #configurando o motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    # leva os dados do  resultado a serem escrtio no motor de excel configurado
    result.to_excel(writer , index=False)

    #salva o arquivo do excel
    writer._save()
    print("arquivo salvo!")
else:
    print("nehum dado para ser salvo ")