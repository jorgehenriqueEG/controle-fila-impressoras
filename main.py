impressoras = [{'id': 'IMP01', 'fila': 2, 'prio': 1}, {'id': 'IMP02', 'fila': 1, 'prio': 2}, {'id': 'IMP03', 'fila': 3, 'prio': 1}, {'id': 'IMP04', 'fila': 1, 'prio': 1}]

ordenadas = sorted(impressoras, key=lambda x: (x['prio'], x['fila']))

resultado = []

for imp in ordenadas:
    resultado.append(imp['id'])

for i in range(3):
    print(resultado[i])