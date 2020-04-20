from pdfreader import SimplePDFViewer
from re import sub

def read(path):
    print('=> Neon Robot: In Progress...')
    with open(path, 'rb') as file:
        viewer = SimplePDFViewer(file)

        viewer.navigate(2)
        viewer.render()

        full_string = ''.join(viewer.canvas.strings)
        re_pattern = '(.*R\$CartãoData)(.*)(Fique atento:Pagamento Mínimo:.*)'

        bill_string = sub(re_pattern, r'\2', full_string)
        after_date_spaces = sub('(.\d{2}\/\d{2}\/\d{4})(.)', r'\1--space--\2', bill_string)
        before_date_spaces = sub('(.)(\d{2}\/\d{2}\/\d{4})', r'\1--space--\2', after_date_spaces)
        currency_spaces = sub('(.)(R\$\d)', r'\1--space--\2', before_date_spaces)
        remove_card_column = sub('(Físico|Virtual)', '', currency_spaces)
        remove_currency_string = sub('R\$', '', remove_card_column)

        bill_list = remove_currency_string.split('--space--')

        content = list(filter(lambda s: len(s.strip()), bill_list))

        result = [[value, content[index * 3 + 1], content[index * 3 + 2]] for index, value in enumerate(content[::3])]

        result.insert(0, ['Fatura neon'])

        print('     * Neon Robot: Done\n')

        return result

if __name__ == '__main__':
    read("./neon.pdf")
