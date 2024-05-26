import random

nato_alphabet = {
    'a': 'Alpha',   'b': 'Bravo',    'c': 'Charlie', 'd': 'Delta',
    'e': 'Echo',    'f': 'Foxtrot',  'g': 'Golf',    'h': 'Hotel',
    'i': 'India',   'j': 'Juliet',   'k': 'Kilo',    'l': 'Lima',
    'm': 'Mike',    'n': 'November', 'o': 'Oscar',   'p': 'Papa',
    'q': 'Quebec',  'r': 'Romeo',    's': 'Sierra',  't': 'Tango',
    'u': 'Uniform', 'v': 'Victor',   'w': 'Whiskey', 'x': 'X-ray',
    'y': 'Yankee',  'z': 'Zulu'
}

def konversi_ke_nato(char):
    return nato_alphabet.get(char, char)

def rot13(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        return char

def string_ke_heksadesimal(char):
    nilai_ascii = ord(char)
    if nilai_ascii < 16:
        return '0' + hex(nilai_ascii)[2:]
    else:
        return hex(nilai_ascii)[2:]

def acak_konversi(input_string):
    hasil = []
    for char in input_string:
        metode = random.choice(['nato', 'rot13', 'hex'])
        if metode == 'nato':
            hasil.append(konversi_ke_nato(char.lower()))
        elif metode == 'rot13':
            hasil.append(rot13(char))
        elif metode == 'hex':
            hasil.append(string_ke_heksadesimal(char))
    return ''.join(hasil)

def main():
    print("Selamat datang di program acak kriptografi!")
    while True:
        user_input = input("Masukkan teks untuk diproses (atau ketik 'keluar' untuk keluar): ")
        if user_input.lower() == 'keluar':
            print("Terima kasih telah menggunakan program acak kriptografi. Sampai jumpa!")
            break
        output = acak_konversi(user_input)
        print("Hasil konversi acak:")
        print(output)

if __name__ == "__main__":
    main()