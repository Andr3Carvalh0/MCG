from colorsys import hsv_to_rgb

class CorRGB:
   
    def __init__(self, red, green, blue):
        self.r = min(1.0, max(0.0, red))
        self.g = min(1.0, max(0.0, green))
        self.b = min(1.0, max(0.0, blue))

    def __str__(self):
        return str(int(self.r*255.0)) + " " + str(int(self.g*255.0)) + " " \
            + str(int(self.b*255.0))

    def soma(self, outra_cor):
        return CorRGB(self.r + outra_cor.r,self.g + outra_cor.g,self.b + outra_cor.b)

    def __add__(self, outra_cor):
        return self.soma(outra_cor)

    def set_hsv(self, hue, saturation, value):
        (red, green, blue) = hsv_to_rgb(hue/360.0, saturation, value)
        self.r = red
        self.g = green
        self.b = blue
        return self

    def multiplica(self, outra_cor):
        return CorRGB(self.r * outra_cor.r, self.g * outra_cor.g,self.b * outra_cor.b)

    def multiplica_escalar(self, escalar):
        return CorRGB(self.r * escalar, self.g * escalar, self.b * escalar)

    def __mul__(self, valor):
        if isinstance(valor, float):
            return self.multiplica_escalar(valor)
        else:
            return self.multiplica(valor)

if __name__ == "__main__":
    
    c1 = CorRGB(0.0, 0.0, 0.0)
    c1.set_hsv(360.0, 1.0, 1.0)
    print(c1)