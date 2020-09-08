from time import time, sleep
from aux_func_matriz import media_matriz

start = time()
especies = {}
indice = 0


def main(start,especies,indice):
    while True:
        try:
            linha = input()
            #print(linha)
            if indice == 0:
                cabecalho = linha.upper().replace('\n','').split(';')
                indice = 1
            else:
                dados = linha.upper().replace('\n','').split(';')
                if dados[-1] not in especies:
                    especies[dados[-1]] = []
                valores = list(map(lambda x: float(x), dados[:-1]))
                especies[dados[-1]].append(valores)
        except EOFError:
            nomes_arquivos = especies.keys()
            cabecalho_final = cabecalho[1:-1] 
            cabecalho_final = "|".join(cabecalho_final)
            arq_geral = open('geral.csv','a+')
            arq_geral.write(cabecalho_final + '|' + 'ESPECIES' + '\n' )
            geral = []

            for i in nomes_arquivos:
                resultado = media_matriz(especies[i])[1:]
                file = open(i + '.csv' ,'a+')
                file.write(cabecalho_final + '\n')
                file.write("|".join(list(map(lambda x: str(x),resultado))))
                arq_geral.write("|".join(list(map(lambda x: str(x),resultado))) + '|' + i + '\n')
                file.close()
                
            arq_geral.close()
            sleep(3)
            print('Arquivo gerado com sucesso com tempo de execução de %.2f segundos' %(time()-start))
            break
            
if __name__ == '__main__':
    main(start,especies,indice)