from dotenv import load_dotenv
from nubank_reader import read as nubank_read
from neon_reader import read as neon_read
from sheets import main as write

load_dotenv()

print('Olá, sejá bem vindo ao pReader!\n')

bills = list()

nubank_path = input('Inclua o caminho para o pdf do nubank (enter para ignorar): ')

neon_path = input('Inclua o caminho para o pdf do neon (enter para ignorar): ')

if nubank_path:
    nubank_bill = nubank_read(nubank_path)
    if nubank_bill is not False:
        bills.append(nubank_bill)

if neon_path:
    neon_bill = neon_read(neon_path)
    if neon_bill is not False:
        bills.append(neon_bill)

for bill in bills:
    write(bill)






