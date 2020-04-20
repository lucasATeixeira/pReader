from pdfreader import SimplePDFViewer

def read(path):
    try:
        print('\n=> Nubank Robot: In Progress...')
        with open(path, 'rb') as file:
            viewer = SimplePDFViewer(file)

            viewer.navigate(1)

            while True:
                try:
                    viewer.render()
                    if 'TRANSAÇÕES' in viewer.canvas.strings:
                        break
                    viewer.next()
                except:
                    print('Nubank Robot: Não foi achado dados de transações na fatura do nubank')

            content = list(filter(lambda s: len(s.strip()), viewer.canvas.strings))[3:-6]

            result = [[value, content[index * 3 + 1], content[index * 3 + 2]] for index, value in enumerate(content[::3])]

            result.insert(0, ['Fatura Nubank'])

            print('     * Nubank Robot: Done\n')

            return result
    except:
        print('Nubank Robot: Tivemos um erro ao ler a fatura do nubank\n')
        return False

if __name__ == '__main__':
    read('./nubank.pdf')
