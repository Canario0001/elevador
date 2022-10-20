#!/usr/bin/env python3
from logic import s1, s2, s3, s4, s5, err
def header(num):
        print('┅'*num)

def lista():
    print('\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
    print('n: Força Normal (força de reação do elevador) (em N)\nm: Massa (em kg)\na: Aceleração (em m/s²)\np: Força Peso (em N)')
    print('g: Gravidade (se não for colocada será considerada como 10 m/s²)\n')

def anotar(nome, resultado):
    texto = f'Resultados\n\nForça Normal: {resultado["n"]} N\nMassa: {resultado["m"]} kg\nAceleração: {resultado["a"]} m/s²\nForça Peso: {resultado["p"]} N\nGravidade: {resultado["g"]} m/s²\n'
    with open(f'{nome}.txt', 'w') as f: f.write(texto)

def main():
    header(30)
    print('  Calculadora de Elevador!')
    header(30)
    print('\nDeseja ver a lista de abreviações ou quer começar agora?\n')
    print('[0] - Ver a lista de abreviações\n[1] - Começar sem ver a lista\n')
    choice = int(input('>>> '))
    if choice == 0: lista()
    elif choice == 1: pass
    else:
        print('Insira um valor válido. Tente novamente.')
        exit()

    m = None
    a = None
    p = None
    n = None
    g = 10
    print('Digite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.\n')
    while True:
        # comp → composto
        comp = input('>>> ').strip().lower()
        if comp == 'q': break

        if comp.startswith('m'):
            _, m = comp.split(':')
            m = float(m)

        elif comp.startswith('a'):
            _, a = comp.split(':')
            a = float(a)

        elif comp.startswith('p'):
            _, p = comp.split(':')
            p = float(p)

        elif comp.startswith('n'):
            _, n = comp.split(':')
            n = float(n)

        elif comp.startswith('g'):
            _, g = comp.split(':')
            g = float(g)

        else: print('Digite uma informação válida!')

    print('\nDigite o número correspondente a situação que você quer aplicar.')
    print('\n[1] - Elevador em repouso ou em MRU\n[2] - Elevador acelerando na subida')
    print('[3] - Subida desacelerando ou descida acelerando\n[4] - Descida desacelerando\n[5] - Sensação de gravidade zero\n')
    s = int(input('>>> '))
    if s == 1:
        resultado = s1(m, a, p, n, g)

    elif s == 2:
        resultado = s2(m, a, p, n, g)
    
    elif s == 3:
        resultado = s3(m, a, p, n, g)

    elif s == 4:
        resultado = s4(m, a, p, n, g)
    
    elif s == 5:
        resultado = s5(m, a, p, n, g)

    else: 
        print('Insira um valor. Tente novamente.')
        exit()
    print('\n')
    header(35)
    print('  Resultados')
    header(35)
    print('')
    print(f'  Força Normal: {resultado["n"]} N')
    print(f'  Força Peso: {resultado["p"]} N')
    print(f'  Massa: {resultado["m"]} kg')
    print(f'  Aceleração: {resultado["a"]} m/s²')
    print(f'  Gravidade: {resultado["g"]} m/s²')
    print('\n\nVocê quer escrever os resultados num arquivo de texto?\n\n[0] - Sim\n[1] - Não\n')
    choice = int(input('>>> ').strip())
    if choice == 0:
        print('\nQual será o nome do arquivo?\n')
        nome = input('>>> ').strip()
        anotar(nome, resultado)
        print(f'\nResultados salvos no arquivo {nome}.txt!')
    elif choice == 1: pass
    else: print('Opção inválida. Operação cancelada.')

    print('\nObrigado por usar!\nFeito por: Canário')

if __name__ == '__main__':
    main()
