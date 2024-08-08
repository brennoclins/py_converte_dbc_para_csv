import readdbc

# Caminho do arquivo DBC
dbc_file = './DBC/PAPE2405.dbc'

# Caminho do arquivo CSV de saída
csv_file = './CSV/PA_Pernambuco_2024_05.csv'

# Converter DBC para CSV
readdbc.dbc2csv(dbc_file, csv_file)

print(f'Arquivo {dbc_file} convertido para {csv_file}')
