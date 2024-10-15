import string

# Fungsi untuk membuat matriks 5x5 dari kunci
def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    
    # Memasukkan huruf dari kunci ke matriks
    for char in key:
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)
    
    # Memasukkan sisa huruf abjad ke matriks
    for char in string.ascii_uppercase.replace("J", ""):
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    
    # Ubah menjadi matriks 5x5
    matrix_5x5 = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_5x5

# Fungsi untuk memecah plaintext menjadi pasangan huruf
def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    digraphs = []
    
    i = 0
    while i < len(plaintext):
        digraph = plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i] != plaintext[i+1]:
            digraph += plaintext[i+1]
            i += 2
        else:
            digraph += 'X'
            i += 1
        digraphs.append(digraph)
    
    return digraphs

# Fungsi untuk mencari lokasi huruf dalam matriks
def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

# Fungsi untuk mengenkripsi sepasang huruf
def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)
    
    if row1 == row2:  # Jika dalam baris yang sama
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Jika dalam kolom yang sama
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # Bentuk persegi panjang
        return matrix[row1][col2] + matrix[row2][col1]

# Fungsi untuk mengenkripsi teks
def playfair_encrypt(plaintext, key):
    matrix = create_matrix(key)
    digraphs = prepare_text(plaintext)
    ciphertext = ""
    
    for digraph in digraphs:
        ciphertext += encrypt_pair(digraph, matrix)
    
    return ciphertext

# Input dan kunci
key = "TEKNIK INFORMATIKA"
plaintexts = [
    "GOOD BROOM SWEEP CLEAN",
    "REDWOOD NATIONAL STATE PARK",
    "JUNK FOOD AND HEALTH PROBLEMS"
]

# Proses enkripsi
for plaintext in plaintexts:
    ciphertext = playfair_encrypt(plaintext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print("-" * 40)
