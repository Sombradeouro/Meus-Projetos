class Conversor:
    def int_para_romano(self, num):
        val_int = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        val_rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        numero_romano = ''

        i = 0
        while num > 0:
            for _ in range(num // val_int[i]):
                numero_romano += val_rom[i]
                num -= val_int[i]
            i += 1

        return numero_romano

# Uso
num = int(input('Digite um número a ser convertido: '))
print(Conversor().int_para_romano(num))
