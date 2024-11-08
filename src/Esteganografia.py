from stegano import lsb
"""Fazendo um teste com a lib stegano"""
# secret = lsb.hide("./meteor_challenge_01.png", "Teste ThiagoLuz")
# secret.save("./meteor_challenge_01_th.png")

# message = lsb.reveal("./src/imagens/meteor_challenge_01_th.png")
# print(message)
"""Pelo jeito a frase oculta não foi adicionada com a lib stegano. :/ """
message = lsb.reveal("./meteor_challenge.png")
print(message)
