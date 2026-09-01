usuarios = {
    "ana": 5,
    "bruno": 0,
    "carla": 3
}

for usuario, acessos in usuarios.items():

    if acessos == 0:
        del usuarios[usuario]

print(usuarios)