from PIL import Image

image = Image.open("./images/meteor_challenge_01.png").convert("RGB")
# image.show()
width, height = image.size

# Definindo cores
WHITE = (255, 255, 255)  # Estrelas
RED = (255, 0, 0)        # Meteoros
BLUE = (0, 0, 255)       # Água
BLACK = (0, 0, 0)        # Solo

# Variaveis de contagem
star_count = 0
meteor_count = 0
water_meteors = 0

# Contagem de estrelas, meteoros, solo e água
for sizex in range(width):
    for sizey in range(height):
        pixel = image.getpixel((sizex, sizey))
        if pixel == WHITE:
            star_count += 1
        elif pixel == RED:
            meteor_count += 1
        # import pdb; pdb.set_trace()

# Identificar meteoros que caem na água
for sizex in range(width):
    meteor_in_column = False
    for sizey in range(height):
        pixel = image.getpixel((sizex, sizey))
        if pixel == RED:
            meteor_in_column = True  # Identifica um meteoro na coluna
        elif pixel == BLUE and meteor_in_column:
            water_meteors += 1  # Se encontrar água após um meteoro, é pq ele caiu na água
            break
        elif pixel == BLACK:
            break  # Se encontramos solo, pare de verificar esta coluna

print("Número de Estrelas:", star_count)
print("Número de Meteoros:", meteor_count)
print("Meteoros caindo na Água:", water_meteors)
