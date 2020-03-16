import sys


class Huffman():
    def encoding(self, data):
        if not isinstance(data, str):
            print('Unsupported format, please pass in a string')
            return None, None

        if len(data) < 1:
            print('Empty string')
            return None, None

        dict, tree, string, encoded_str = {}, {}, '1', ''

        for character in data:
            dict[character] = dict.get(character, 0) + 1

        for num in sorted(dict.items(), key=lambda x: x[1]):
            tree[num[0]] = string
            string = '0' + string

        for item in data:
            encoded_str += tree[item]

        return encoded_str, tree

    def decoding(self, data, tree):
        dict, str, decoded_str = {},  '', ''

        for child in tree:
            dict[tree[child]] = child

        for item in data:
            if item == '1':
                decoded_str += dict[str + item]
                str = ''
            else:
                str += item

        return decoded_str


# Instance
huffman = Huffman()

print("Test 1 - Normal")
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman.encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

print("Test 2 - Edge Empty string")
if __name__ == "__main__":
    codes = {}

    a_great_sentence = ""

    encoded_data, tree = huffman.encoding(a_great_sentence)

print("Test 3 - Edge different datatype")
if __name__ == "__main__":
    codes = {}

    a_great_sentence = True

    encoded_data, tree = huffman.encoding(a_great_sentence)
