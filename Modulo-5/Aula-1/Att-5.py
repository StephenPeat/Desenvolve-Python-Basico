print("Não estou conseguindo")

emojis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print("Emojis disponíveis:\n")
for codigo, emoji_char in emojis.items():
    print(f"{emoji_char} - {codigo}")

frase = input("\nDigite uma frase usando os códigos dos emojis:\n")

for codigo, emoji_char in emojis.items():
    frase = frase.replace(codigo, emoji_char)

print("\nFrase emojizada:\n")
print(frase)