from PIL import Image
import os


class ImageAnalyzer:
    """Caminho imagem"""
    INPUT_FOLDER = "src/imagens"
    """Definindo cores para os objetos, Estrelas, Meteoros, Agua, solo"""
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    """Variáveis de Contagem de Obj"""
    star_count = 0
    meteor_count = 0
    water_meteors = 0

    def in_path(self, filename):
        """Retorna endereço relativo dentro da pasta imagens"""
        return os.path.join(self.INPUT_FOLDER, filename)

    def _obtem_pixel_image(self):
        """Obtendo os objetos. E utilizando o .load() para acessar os pixels de forma mais rápida"""
        im = Image.open(self.in_path("meteor_challenge_01.png"))
        image = im.convert("RGB")
        pixels = image.load()
        width, height = image.size
        for sizex in range(width):
            for sizey in range(height):
                pixel = pixels[sizex, sizey]
                if pixel == self.WHITE:
                    self.star_count += 1
                elif pixel == self.RED:
                    self.meteor_count += 1
                # import pdb; pdb.set_trace()
        """Identificando meteoros que caem na água"""
        for sizex in range(width):
            meteor_in_colum = False #setando todos os valores de x(horizontal) como False. Flake8 está pegando essa linha =)
            for sizey in range(height):
                pixel = pixels[sizex, sizey]
                if pixel == self.RED:
                    meteor_in_colum = True
                elif pixel == self.BLUE and meteor_in_colum:
                    self.water_meteors += 1
                    break
                elif pixel == self.BLACK:
                    break

    def exibi_resultado(self):
        self._obtem_pixel_image()
        print(f"Estrelas: {self.star_count}")
        print(f"Meteoros: {self.meteor_count}")
        print(f"Meteoros Caindo na água: {self.water_meteors}")
