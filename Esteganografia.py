from stegano import lsb

# secret = lsb.hide("./meteor_challenge_01.png", "Teste ThiagoLuz")
# secret.save("./meteor_challenge_01_th.png")

# message = lsb.reveal("./meteor_challenge_01_th.png")
# print(message)

message = lsb.reveal("./meteor_challenge.png")
print(message)