import string

# Membuat matriks 5x5 dari kunci
def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    
    for char in key:
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)
    
    for char in string.ascii_uppercase.replace("J", ""):
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    
    matrix_5x5 = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_5x5

# Memecah plaintext menjadi pasangan huruf
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

# Mencari posisi huruf di dalam matriks
def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

# Mengenkripsi pasangan huruf
def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)
    
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Mendekripsi pasangan huruf
def decrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)
    
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Fungsi enkripsi teks
def playfair_encrypt(plaintext, key):
    matrix = create_matrix(key)
    digraphs = prepare_text(plaintext)
    ciphertext = ""
    
    for digraph in digraphs:
        ciphertext += encrypt_pair(digraph, matrix)
    
    return ciphertext

# Fungsi dekripsi teks
def playfair_decrypt(ciphertext, key):
    matrix = create_matrix(key)
    digraphs = prepare_text(ciphertext)
    plaintext = ""
    
    for digraph in digraphs:
        plaintext += decrypt_pair(digraph, matrix)
    
    return plaintext

# Input kunci dan plaintext
key = "TEKNIK INFORMATIKA"
plaintexts = [
    "GOOD BROOM SWEEP CLEAN",
    "REDWOOD NATIONAL STATE PARK",
    "JUNK FOOD AND HEALTH PROBLEMS"
]

# Proses enkripsi dan dekripsi
for plaintext in plaintexts:
    ciphertext = playfair_encrypt(plaintext, key)
    decrypted_text = playfair_decrypt(ciphertext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted_text}")
    print("-" * 40)
