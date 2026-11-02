from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    huono = Varasto(-100.0)
    huono = Varasto(100.0, -50.7)
    olutta.lisaa_varastoon(1000.0)
    print(huono, "a")


if __name__ == "__main__":
    main()
