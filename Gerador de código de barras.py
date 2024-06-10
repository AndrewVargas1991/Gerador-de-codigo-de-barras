# pip install python-barcode
from barcode import EAN13
from barcode.writer import ImageWriter
import webbrowser

numero = '5901234123457'
codigo = EAN13(numero, writer=ImageWriter)
codigo.save('CODIGO')
webbrowser.open('CODIGO.svg', new=2)

# Para maiores informações sobre o padrão EAN de
# código de barras, acesse o site abaixo:
# https://pt.wikipedia.org/wiki/EAN-13