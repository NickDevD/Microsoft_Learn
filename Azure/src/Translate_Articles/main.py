import translator
import config

def main():
    while True:
        text = input("Digite o texto a ser traduzido: ")
        source_language = input("Digite o código do idioma de origem: ")
        target_language = input("Digite o código do idioma de destino: ")

        translation = translator.translate_text(text, source_language, target_language, config.endpoint, config.key)

        if translation:
            print(translation)
        else:
            print("Ocorreu um erro durante a tradução.")

if __name__ == "__main__":
    main()