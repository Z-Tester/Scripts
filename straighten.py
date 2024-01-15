#Straighten a sentence you type on the keyboard.
def straighten_sentence(sentence):
    reversed_sentence = sentence[::-1]
    return reversed_sentence


if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")

    straightened_sentence = straighten_sentence(input_sentence)

    print("\nOriginal Sentence:", input_sentence)
    print("Reversed Sentence:", straightened_sentence)
