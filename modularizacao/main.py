#import minha_lib - traz tudo para o arquivo principal
#from minha_lib import * # Traz tudo o que tem na biblioteca
#from minha_lib import x # Traz somente a variavel x da minha_lib
#from minha_lib import x as x_importado # Traz a variavel e muda o nome dela
from minha_lib import soma_numero # Traz a função soma_numero
#from minhas_funcoes.minha_lib import soma_numero #Trazendo a função de outra pasta


x = soma_numero(2,8)

print(x)
