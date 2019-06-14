from Armstrong import ArmstrongManager
from Colors import ColorManager


class Decryption:
    # constructor
    def __init__(self, key):
        self.xorKey = ArmstrongManager.getXORKeY(key)
        self.c = ColorManager(self.xorKey)

    def decrypt(self, encFile, regainFile):
        ef = None
        rf = None
        try:
            # open the encrypted file for reading in binary mode
            ef = open(encFile, 'rb')
            # open the decrypted file for writing in binary mode
            rf = open(regainFile, 'wb')

            # decrypt
            ki = 0  # keyIndex
            kL = len(self.xorKey)
            table = 1

            flag = True

            decBuff = bytearray()
            while flag:
                # read 1024 or less number of bytes from the source file
                buff = ef.read(1024)
                if buff:
                    for eachByte in buff:

                        # level 2 encoding
                        dec2 = self.c.colorDecode(eachByte, table)
                        table = table % 3 + 1

                        # level 1 encoding
                        dec1 = dec2 ^ int(self.xorKey[ki])
                        ki += 1
                        ki = ki % kL


                        decBuff.append(dec1)

                    rf.write(decBuff)
                    decBuff.clear()

                else:
                    # buff is empty
                    # EOF encountered
                    flag = False



        except IOError:
            # this block executes when any IOError occurs
            status = 1
        except:
            # this block executes for any other error
            status = 2
        finally:
            # this block executes everytime
            if ef is not None:
                ef.close()
            if rf is not None:
                rf.close()
