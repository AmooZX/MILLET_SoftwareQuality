def sentenceVerification(sentence):
    errors = 0

    if not sentence[0].isupper():
        errors += 1

    if len(sentence.split()) < 3:
        errors += 1

    if len(sentence.split()) > 9:
        errors += 1

    if sentence[len(sentence) - 1] != '.':
        errors += 1

    if errors > 0:
        return False
    else:
        return True


def main():
    sentence = str(input("Veuillez rentrer une phrase : "))

    if sentenceVerification(sentence):
        print("La phrase est correcte")
    else:
        print("La phrase n'est pas correcte")


if __name__ == '__main__':
    main()
