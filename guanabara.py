"""
def info(titulo):
    print('-' * 60)
    print(titulo)
    print('-' * 60)

info('                           Othumba')
info('                  Autor: Luiz Henrique Silva')
info('                       Editora: Uiclap')
"""
"""def area(largura, comprimento):
    resultado = largura * comprimento
    print (f'A área de um terreno {largura}x{comprimento} é de {resultado}m²')

area(4.5, 8)"""

def escreva(texto):
    qtd = len(texto) + 8
    print('=' * qtd)
    print(f'    {texto}')
    print('=' * qtd)

escreva('Othumba')
escreva('Autor: Luiz Henrique Silva')
escreva('Ano: 2020')
escreva('Uiclap')

