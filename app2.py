import openpyxl
book = openpyxl.load_workbook ('Planilha Produtos.xlsx')
produtos_page = book['Produtos']

#Importar dados de cada linha 

for rows in produtos_page.iter_rows(min_row=2, max_row=6):
    for cell in rows:
        if cell.value == 'Computador 1':
            cell.value = 'Notebook Lenovo'

book.save('Planilha Produtos V2.xlsx')

        