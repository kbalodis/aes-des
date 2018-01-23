# based on: https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf

import struct
import copy
import numpy

Nr = 10
Nk = 4

class AES(object):
    S = [ 0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
          0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
          0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
          0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
          0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
          0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
          0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
          0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
          0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
          0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
          0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
          0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
          0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
          0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
          0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
          0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 ]
    Si =[ 0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
          0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
          0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
          0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
          0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
          0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
          0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
          0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
          0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
          0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
          0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
          0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
          0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
          0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
          0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
          0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d ]
    
    Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36] 
    
    def __init__(self, key):
        if len(key) is not 16:
            raise ValueError("Invlaid key size")

        self.key = key

        self.key_unpacked = []

        for i in range(0, len(key), 4):
            word = []
            for j in range(i, i + 4):
                word.append(hex(ord(key[j])))
            self.key_unpacked.append(word)

        # self.key_unpacked = [['0x2b', '0x7e', '0x15', '0x16'],
        #                      ['0x28', '0xae', '0xd2', '0xa6'],
        #                      ['0xab', '0xf7', '0x15', '0x88'],
        #                      ['0x09', '0xcf', '0x4f', '0x3c']]

        # self.key_unpacked = [['0x00', '0x1', '0x2', '0x3'],
        #                      ['0x4', '0x5', '0x6', '0x7'],
        #                      ['0x8', '0x9', '0x1', '0xb'],
        #                      ['0xc', '0xd', '0xe', '0xf']]

        self.key_exp_encr = self.KeyExpansionEncrypt(self.key_unpacked)
        # print self.key_exp_encr

        self.plaintext_unpacked = []

        self.cyphertext = []
        # self.cyphertext = [['0x69', '0xc4', '0xe0', '0xd8'],
        #         ['0x6a', '0x7b', '0x04', '0x30'],
        #         ['0xd8', '0xcd', '0xb7', '0x80'],
        #         ['0x70', '0xb4', '0xc5', '0x5a']]

        self.decyphered = []

    def RowsToColumns(self, matrix):
        result = copy.deepcopy(matrix)
        for j in range(0, 4):
            for i in range(0, 4):
                result[j][i] = copy.deepcopy(matrix[i][j])

        return result

    def EncryptAES(self, plaintext):
        if len(plaintext) is not 16:
            raise ValueError("Invalid plaintext file!")

        for i in range(0, len(plaintext), 4):
            word = []
            for j in range(i, i + 4):
                word.append(hex(ord(plaintext[j])))
            self.plaintext_unpacked.append(word)

        # self.plaintext_unpacked = [['0x32', '0x43', '0xf6', '0xa8'],
        #                            ['0x88', '0x5a', '0x30', '0x8d'],
        #                            ['0x31', '0x31', '0x98', '0xa2'],
        #                            ['0xe0', '0x37', '0x07', '0x34']]
        
        self.result = copy.deepcopy(self.plaintext_unpacked)

        self.result = self.AddRoundKeyEnc(self.result, 0)
        self.result = self.RowsToColumns(self.result)

        for i in range (1, Nr):
            #substitute bytes
            for j in range (0, 4):
                self.result[j] = self.SubWord(self.result[j])
            #shift rows
            self.result = self.ShiftRows(self.result)
            #mix columns
            self.result = self.MixColumns(self.result)
            self.result = self.AddRoundKeyEnc(self.result, i)
            self.result = self.RowsToColumns(self.result)

        for i in range (0, 4):
            self.result[i] = self.SubWord(self.result[i])
        # print self.result
        self.result = self.ShiftRows(self.result)
        self.result = self.RowsToColumns(self.result)
        self.result = self.AddRoundKeyEnc(self.result, 10)
        self.result = self.RowsToColumns(self.result)

        # print self.result
        self.cyphertext = copy.deepcopy(self.result)

        return self.result

    def DecryptAES(self, cyphertext):
        # self.cyphertext = [['0x69', '0xc4', '0xe0', '0xd8'],
        #                ['0x6a', '0x7b', '0x04', '0x30'],
        #                ['0xd8', '0xcd', '0xb7', '0x80'],
        #                ['0x70', '0xb4', '0xc5', '0x5a']]
                
        self.result = copy.deepcopy(self.cyphertext)
        print self.result

        # print cyphertext
        # add first round key
        self.result = self.RowsToColumns(self.result)
        self.result = self.AddRoundKeyEnc(self.result, 10)
        print self.result
        self.result = self.RowsToColumns(self.result)

        j = Nr-1

        for i in range (0, Nr-1):
            # print j
            #shift rows
            self.result = self.InvShiftRows(self.result)
            #substitute bytes
            for k in range (0, 4):
                self.result[k] = self.InvSubBytes(self.result[k])
            self.result = self.AddRoundKeyEnc(self.result, j)
            self.result = self.RowsToColumns(self.result)
            #mix columns
            self.result = self.InvMixColumns(self.result)
            j = j - 1

        self.result = self.InvShiftRows(self.result)
        for i in range (0, 4):
            self.result[i] = self.InvSubBytes(self.result[i])
        # self.result = self.RowsToColumns(self.result)
        # self.result = self.RowsToColumns(self.result)
        self.result = self.AddRoundKeyEnc(self.result, 0)
        # self.result = self.RowsToColumns(self.result)

        self.decyphered = copy.deepcopy(self.result)

        return self.result
    
    def InvShiftRows(self, input_words):
        #second row
        temp = input_words[1][3]
        input_words[1][3] = input_words[1][2]
        input_words[1][2] = input_words[1][1]
        input_words[1][1] = input_words[1][0]
        input_words[1][0] = temp
        #third row
        temp = input_words[2][3]
        temp2 = input_words[2][2]
        input_words[2][3] = input_words[2][1]
        input_words[2][2] = input_words[2][0]
        input_words[2][1] = temp
        input_words[2][0] = temp2
        #fourth row
        temp = input_words[3][3]
        temp2 = input_words[3][2]
        temp3 = input_words[3][1]
        input_words[3][3] = input_words[3][0]
        input_words[3][2] = temp
        input_words[3][1] = temp2
        input_words[3][0] = temp3

        return input_words

    def InvSubBytes(self, word):
        for i in range(0, len(word)):
            word[i] = hex(self.Si[int(word[i], 0)])
        return word

    def InvMixColumns(self, input_words):
        result = []
        # print input_words
        for i in range(0, 4):
            temp = []
            temp.append(hex(self.GFXor('0x0e', int(input_words[0][i], 0)) ^\
                            self.GFXor('0x0b', int(input_words[1][i], 0)) ^\
                            self.GFXor('0x0d', int(input_words[2][i], 0)) ^\
                            self.GFXor('0x09', int(input_words[3][i], 0))
                            )
                        )
            temp.append(hex(self.GFXor('0x09', int(input_words[0][i], 0)) ^\
                            self.GFXor('0x0e', int(input_words[1][i], 0)) ^\
                            self.GFXor('0x0b', int(input_words[2][i], 0)) ^\
                            self.GFXor('0x0d', int(input_words[3][i], 0))
                            )
                        )
            temp.append(hex(self.GFXor('0x0d', int(input_words[0][i], 0)) ^\
                            self.GFXor('0x09', int(input_words[1][i], 0)) ^\
                            self.GFXor('0x0e', int(input_words[2][i], 0)) ^\
                            self.GFXor('0x0b', int(input_words[3][i], 0))
                            )
                        )
            temp.append(hex(self.GFXor('0x0b', int(input_words[0][i], 0)) ^\
                            self.GFXor('0x0d', int(input_words[1][i], 0)) ^\
                            self.GFXor('0x09', int(input_words[2][i], 0)) ^\
                            self.GFXor('0x0e', int(input_words[3][i], 0))
                            )
                        )
            result.append(temp)

        return result

    def AddRoundKeyEnc(self, input_array, round_no):
        result_array = []
        for i in range(0, 4):
            temp = []
            temp.append(hex(int(input_array[i][0], 0) ^
                            int(self.key_exp_encr[4 * round_no + i][0], 0)))
            temp.append(hex(int(input_array[i][1], 0) ^\
                            int(self.key_exp_encr[4 * round_no + i][1], 0)))
            temp.append(hex(int(input_array[i][2], 0) ^\
                            int(self.key_exp_encr[4 * round_no + i][2], 0)))
            temp.append(hex(int(input_array[i][3], 0) ^\
                            int(self.key_exp_encr[4 * round_no + i][3], 0)))
            result_array.append(copy.deepcopy(temp))
        
        print result_array
        return result_array

    def ShiftRows(self, input_words):
        #second row
        temp = input_words[1][0]
        input_words[1][0] = input_words[1][1]
        input_words[1][1] = input_words[1][2]
        input_words[1][2] = input_words[1][3]
        input_words[1][3] = temp
        #third row
        temp = input_words[2][0]
        temp2 = input_words[2][1]
        input_words[2][0] = input_words[2][2]
        input_words[2][1] = input_words[2][3]
        input_words[2][2] = temp
        input_words[2][3] = temp2
        #fourth row
        temp = input_words[3][0]
        temp2 = input_words[3][1]
        temp3 = input_words[3][2]
        input_words[3][0] = input_words[3][3]
        input_words[3][1] = temp
        input_words[3][2] = temp2
        input_words[3][3] = temp3

        return input_words

    def MixColumns(self, input_words):
        result = []
        # print input_words
        for i in range(0, 4):
            temp = []
            temp.append(hex(self.GFXor('0x02', int(input_words[0][i], 0)) ^\
                            self.GFXor('0x03', int(input_words[1][i], 0)) ^\
                            int(input_words[2][i], 0) ^\
                            int(input_words[3][i], 0)))
            temp.append(hex(int(input_words[0][i], 0)  ^\
                            self.GFXor('0x02', int(input_words[1][i], 0)) ^\
                            self.GFXor('0x03', int(input_words[2][i], 0)) ^\
                            int(input_words[3][i], 0)))
            temp.append(hex(int(input_words[0][i], 0)  ^\
                            int(input_words[1][i], 0) ^\
                            self.GFXor('0x02', int(input_words[2][i], 0)) ^\
                            self.GFXor('0x03', int(input_words[3][i], 0))))
            temp.append(hex(self.GFXor('0x03', int(input_words[0][i], 0)) ^\
                            int(input_words[1][i], 0) ^\
                            int(input_words[2][i], 0) ^\
                            self.GFXor('0x02', int(input_words[3][i], 0))))
            result.append(temp)

        return result

    def GFXor(self, first, second):
        result = 0
        a = int(first, 0)
        b = second
    
        while a and b:
            if b & 0x1:
                result = result ^ a

            if a & 0x80:
                a = (a << 1) ^ 0x11b
            else: 
                a = a << 1
            
            b = b >> 1

        return result

    def KeyExpansionEncrypt(self, key):
        key_exp = []

        i = 0
        while (i < Nk):
            key_exp.append(copy.deepcopy(key[i]))
            i = i + 1

        i = Nk
        while (i < 4 * (Nr + 1)):
            temp = []
            temp = copy.deepcopy(key_exp[i - 1])
            if i % Nk == 0:
                temp = self.RotWord(temp)
                temp = self.SubWord(temp)
                temp = self.xorRcon(temp, i / Nk - 1)
            result = self.xorBeforeAddToEncrKeys(temp, copy.deepcopy(key_exp[i - Nk]))
            key_exp.append(copy.deepcopy(result))
            i = i + 1

        return key_exp

    def RotWord(self, word):
        temp = word[0]
        word[0] = word[1]
        word[1] = word[2]
        word[2] = word[3]
        word[3] = temp
        return word

    def SubWord(self, word):
        for i in range(0, len(word)):
            word[i] = hex(self.S[int(word[i], 0)])
        return word

    def xorRcon(self, word, elem):
        word[0] = hex((int(word[0], 0) ^ (self.Rcon[elem]) & 0xFF))
        for i in range(1, len(word)):
            word[i] = hex((int(word[i], 0) ^ 0x00)  & 0xFF)
        return word

    def xorBeforeAddToEncrKeys(self, word, temp):
        result = []
        for i in range(0, len(word)):
            result.append((hex(int(word[i], 0) ^ int(temp[i], 0) & 0xFF)))
        return result

    def ASCIItoHex(self, string):
        return ''.join( [ "%02X " % ord( x ) for x in string ] ).strip()

    def HexToByte(self, hexStr):
        bytes = []

        hexStr = ''.join( hexStr.split(" ") )

        for i in range(0, len(hexStr), 2):
            bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

        return ''.join( bytes )

        