qualidades_legendado = [
    'Legendado 720p',
    'Legendado 1080p',
    'Legendado 4K'
]

qualidades_dublado = [
    'Dublado 720p',
    'Dublado 1080p',
    'Dublado 4K'
]

if len(qualidades_legendado) > 2:
    print()
    print('Várias opções de download legendado')
    for i in range(len(qualidades_legendado)):
        print(qualidades_legendado[i])
else:
    print('Única opção de download dublada selecionada:')
    print(f'    {qualidades_legendado[0]}')

print()

if len(qualidades_dublado) > 2:
    print('Várias opções de download dublado')
    for i in range(len(qualidades_dublado)):
        print(qualidades_dublado[i])
else:
    print('Única opção de download legendada selecionada:')
    print(qualidades_dublado[0])