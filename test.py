import time

def declaration_amour():
    message = "Orane, tu es la lumière de ma vie, celle qui fait battre mon cœur."
    for i in range(1, 6):  # Change 6 pour faire plus de répétitions
        print(f"{i}. {message}")
        time.sleep(1)

    print("\nOrane, je t'aime plus que tout !")

# Lancer la déclaration
declaration_amour()