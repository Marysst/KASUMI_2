S7 = [54, 50, 62, 56, 22, 34, 94, 96, 38, 6, 63, 93, 2, 18, 123, 33, 
55, 113, 39, 114, 21, 67, 65, 12, 47, 73, 46, 27, 25, 111, 124, 81, 
53, 9, 121, 79, 52, 60, 58, 48, 101, 127, 40, 120, 104, 70, 71, 43, 
20, 122, 72, 61, 23, 109, 13, 100, 77, 1, 16, 7, 82, 10, 105, 98, 
117, 116, 76, 11, 89, 106, 0, 125, 118, 99, 86, 69, 30, 57, 126, 87, 
112, 51, 17, 5, 95, 14, 90, 84, 91, 8, 35, 103, 32, 97, 28, 66, 
102, 31, 26, 45, 75, 4, 85, 92, 37, 74, 80, 49, 68, 29, 115, 44, 
64, 107, 108, 24, 110, 83, 36, 78, 42, 19, 15, 41, 88, 119, 59, 3]

S9 = [167, 239, 161, 379, 391, 334, 9, 338, 38, 226, 48, 358, 452, 385, 90, 397, 
183, 253, 147, 331, 415, 340, 51, 362, 306, 500, 262, 82, 216, 159, 356, 177, 
175, 241, 489, 37, 206, 17, 0, 333, 44, 254, 378, 58, 143, 220, 81, 400, 
95, 3, 315, 245, 54, 235, 218, 405, 472, 264, 172, 494, 371, 290, 399, 76, 
165, 197, 395, 121, 257, 480, 423, 212, 240, 28, 462, 176, 406, 507, 288, 223, 
501, 407, 249, 265, 89, 186, 221, 428, 164, 74, 440, 196, 458, 421, 350, 163, 
232, 158, 134, 354, 13, 250, 491, 142, 191, 69, 193, 425, 152, 227, 366, 135, 
344, 300, 276, 242, 437, 320, 113, 278, 11, 243, 87, 317, 36, 93, 496, 27, 
487, 446, 482, 41, 68, 156, 457, 131, 326, 403, 339, 20, 39, 115, 442, 124, 
475, 384, 508, 53, 112, 170, 479, 151, 126, 169, 73, 268, 279, 321, 168, 364, 
363, 292, 46, 499, 393, 327, 324, 24, 456, 267, 157, 460, 488, 426, 309, 229, 
439, 506, 208, 271, 349, 401, 434, 236, 16, 209, 359, 52, 56, 120, 199, 277, 
465, 416, 252, 287, 246, 6, 83, 305, 420, 345, 153, 502, 65, 61, 244, 282, 
173, 222, 418, 67, 386, 368, 261, 101, 476, 291, 195, 430, 49, 79, 166, 330, 
280, 383, 373, 128, 382, 408, 155, 495, 367, 388, 274, 107, 459, 417, 62, 454, 
132, 225, 203, 316, 234, 14, 301, 91, 503, 286, 424, 211, 347, 307, 140, 374, 
35, 103, 125, 427, 19, 214, 453, 146, 498, 314, 444, 230, 256, 329, 198, 285, 
50, 116, 78, 410, 10, 205, 510, 171, 231, 45, 139, 467, 29, 86, 505, 32, 
72, 26, 342, 150, 313, 490, 431, 238, 411, 325, 149, 473, 40, 119, 174, 355, 
185, 233, 389, 71, 448, 273, 372, 55, 110, 178, 322, 12, 469, 392, 369, 190, 
1, 109, 375, 137, 181, 88, 75, 308, 260, 484, 98, 272, 370, 275, 412, 111, 
336, 318, 4, 504, 492, 259, 304, 77, 337, 435, 21, 357, 303, 332, 483, 18, 
47, 85, 25, 497, 474, 289, 100, 269, 296, 478, 270, 106, 31, 104, 433, 84, 
414, 486, 394, 96, 99, 154, 511, 148, 413, 361, 409, 255, 162, 215, 302, 201, 
266, 351, 343, 144, 441, 365, 108, 298, 251, 34, 182, 509, 138, 210, 335, 133, 
311, 352, 328, 141, 396, 346, 123, 319, 450, 281, 429, 228, 443, 481, 92, 404, 
485, 422, 248, 297, 23, 213, 130, 466, 22, 217, 283, 70, 294, 360, 419, 127, 
312, 377, 7, 468, 194, 2, 117, 295, 463, 258, 224, 447, 247, 187, 80, 398, 
284, 353, 105, 390, 299, 471, 470, 184, 57, 200, 348, 63, 204, 188, 33, 451, 
97, 30, 310, 219, 94, 160, 129, 493, 64, 179, 263, 102, 189, 207, 114, 402, 
438, 477, 387, 122, 192, 42, 381, 5, 145, 118, 180, 449, 293, 323, 136, 380, 
43, 66, 60, 455, 341, 445, 202, 432, 8, 237, 15, 376, 436, 464, 59, 461]

def ZE(x):
    return x & 0x7F

def TR(x):
    return x & 0x7F

def FI(I, KI):
    L0 = I >> 7
    R0 = I & 0x7F

    KI1 = KI >> 9
    KI2 = KI & 0x1FF

    L1 = R0

    R1 = S9[L0] ^ ZE(R0)
    L2 = R1 ^ KI2
    R2 = S7[L1] ^ TR(R1) ^ KI1

    L3 = R2
    R3 = S9[L2] ^ (R2)

    L4 = S7[L3] ^ TR(R3)
    R4 = R3
    
    return (L4 << 9) | R4

def FO(I, KO, KI):
  L0 = I >> 16
  R0 = I & 0xFFFF

  Lj, Rj = L0, R0
  for j in range(0, 3):
    Rj, Lj = FI(Lj ^ KO[j] , KI[j] ) ^ Rj, Rj
    
  return (Lj << 16) | Rj

def FL(I, KL):
  KL1 = KL[0]
  KL2 = KL[1]

  L = I >> 16
  R = I & 0xFFFF

  Rnew = R ^ ROL(L & KL1)
  Lnew = L ^ ROL(Rnew | KL2)
  
  return (Lnew << 16) | Rnew

def ROL(x, n=1):
    return ((x << n) | (x >> (16 - n))) & 0xFFFF

def fi(I, RKi, round_num):
  if round_num % 2 == 1:
    return FO(FL(I, RKi["KL"]), RKi["KO"], RKi["KI"])
  else:
    return FL(FO(I, RKi["KO"], RKi["KI"]), RKi["KL"])

def KeySchedule(K):
  K1 = K >> 16*7
  K2 = (K >> 16*6) & 0xFFFF
  K3 = (K >> 16*5) & 0xFFFF
  K4 = (K >> 16*4) & 0xFFFF
  K5 = (K >> 16*3) & 0xFFFF
  K6 = (K >> 16*2) & 0xFFFF
  K7 = (K >> 16) & 0xFFFF
  K8 = K & 0xFFFF
  Ks = [K1, K2, K3, K4, K5, K6, K7, K8]

  C = [0x0123, 0x4567, 0x89AB, 0xCDEF, 0xFEDC, 0xBA98, 0x7654, 0x3210]

  Knew = [0] * 8
  for i in range(0, 8):
    Knew[i] = Ks[i] ^ C[i]

  keys = {}
  for i in range(0, 8):
    KL = [0] * 2
    KO = [0] * 3
    KI = [0] * 3

    KL[0] = ROL(Ks[i])
    KL[1] = Knew[i+2 if i+2 <= 7 else i+2-8]

    KO[0] = ROL(Ks[i+1 if i+1 <= 7 else i+1-8], 5)
    KO[1] = ROL(Ks[i+5 if i+5 <= 7 else i+5-8], 8)
    KO[2] = ROL(Ks[i+6 if i+6 <= 7 else i+6-8], 13)

    KI[0] = Knew[i+4 if i+4 <= 7 else i+4-8]
    KI[1] = Knew[i+3 if i+3 <= 7 else i+3-8]
    KI[2] = Knew[i+7 if i+7 <= 7 else i+7-8]

    keys[i+1] = {"KL": KL, "KO": KO, "KI": KI}
  return keys

def KASUMI_EncryptBlock(I, K):
  L0 = I >> 32
  R0 = I & 0xFFFFFFFF

  RK = KeySchedule(K)

  R, L = R0, L0
  for i in range(0, 8):
    R, L = L, R ^ fi(L, RK[i+1], i+1)

  return (L << 32) | R

def KASUMI_DecryptBlock(I, K):
  L0 = I >> 32
  R0 = I & 0xFFFFFFFF

  RK = KeySchedule(K)

  R, L = R0, L0
  for i in reversed(range(0, 8)):
    L, R = R, L ^ fi(R, RK[i+1], i+1)

  return (L << 32) | R

def KASUMI_EncryptData(I, K):
    block_size = 8
    output = bytearray()

    try:
        key_bytes = bytes.fromhex(K)
        if len(key_bytes) != 16:
            raise ValueError
    except ValueError:
        return False, "Key must be exactly 16 bytes (32 hex characters)"

    K_int = int(K, 16)

    # Вирівнювання: додаємо 0-байти до кратності 8
    if len(I) % block_size != 0:
        padding = block_size - (len(I) % block_size)
        I += b'\x00' * padding

    for i in range(0, len(I), block_size):
        block = I[i:i+block_size]
        block_int = int.from_bytes(block, 'big')
        encrypted_block = KASUMI_EncryptBlock(block_int, K_int)
        output.extend(encrypted_block.to_bytes(block_size, 'big'))

    return True, bytes(output)

def KASUMI_DecryptData(I, K):
    block_size = 8
    output = bytearray()

    try:
        key_bytes = bytes.fromhex(K)
        if len(key_bytes) != 16:
            raise ValueError
    except ValueError:
        return False, "Key must be exactly 16 bytes (32 hex characters)"

    K_int = int(K, 16)

    try:
        if len(I) % block_size != 0:
          raise ValueError
    except ValueError:
        return False, "The file is corrupted. Data length is not a multiple of 8 bytes"

    for i in range(0, len(I), block_size):
        block = I[i:i+block_size]
        block_int = int.from_bytes(block, 'big')
        decrypted_block = KASUMI_DecryptBlock(block_int, K_int)
        output.extend(decrypted_block.to_bytes(block_size, 'big'))

    return True, bytes(output)
