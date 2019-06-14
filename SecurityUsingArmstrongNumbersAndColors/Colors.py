class ColorManager:
    #constructor
    def __init__(self, xorkey):

        #first 12 digits of xorkey set as portionA
        portionA = xorkey[0:12]

        # rest digits of xorkey set as portionB
        portionB = xorkey[12:]

        self.red = int(portionB) + int(portionA[0:4])
        self.red %= 256

        self.green = int(portionB) + int(portionA[4:8])
        self.green %= 256

        self.blue = int(portionB) + int(portionA[8:12])
        self.blue %= 256

    def colorEnode(self, data, cFlag):

        basenumber = 0
        if cFlag == 1:
                basenumber = self.red
        elif cFlag == 2:
            basenumber = self.green
        elif cFlag == 3:
            basenumber = self.blue

        nibble1 = data & 240  # 11110000
        nibble1 = nibble1 >> 4  # 00000010

        nibble2 = data & 15  # 00001111

        encData = basenumber + nibble1 * 16 +nibble2
        encData %=256

        return  encData

    def colorDecode(self, encData, cFlag):

        basenumber = 0
        if cFlag == 1:
            basenumber = self.red
        elif cFlag == 2:
            basenumber = self.green
        elif cFlag == 3:
            basenumber = self.blue

        temp = encData - basenumber + 256
        temp %= 256

        nibble1 = temp //16
        nibble2 = temp % 16


        data = nibble1 << 4 | nibble2

        return  data