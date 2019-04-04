data = [
    'разработка',
    'администрирование',
    'protocol',
    'standard'
]

data_encode = []
data_decode = []

for word in data:
    data_encode = data_encode + [word.encode()]

for print_encode in data_encode:
    print(print_encode)

for word_byte in data_encode:
    data_decode = data_decode + [word_byte.decode()]


for print_decode in data_decode:
    print(print_decode)