from Armstrong import ArmstrongManager
from Colors import  ColorManager

class Encryption:
    #constructor
    def __init__(self, key):
        self.xorKey = ArmstrongManager.getXORKeY(key)
        self.c = ColorManager(self.xorKey)

    def encrypt(self, srcFile, trgtFile):
        sf = None
        tf = None
        try:
            #open the source file for reading in binary mode
            sf = open(srcFile, 'rb')
            #open the target file for writing in binary mode
            tf = open(trgtFile, 'wb')

            #encrypt
            ki= 0 #keyIndex
            kL = len(self.xorKey)
            table = 1

            flag = True

            encBuff = bytearray()
            while flag:
                #read 1024 or less number of bytes from the source file
                buff = sf.read(1024)
                if buff:
                    for eachByte in buff:
                        #level 1 encoding
                        enc1 = eachByte ^ int(self.xorKey[ki])
                        ki +=1
                        ki = ki % kL

                        #level 2 encoding
                        enc2 = self.c.colorEnode(enc1, table)
                        table = table % 3 + 1

                        encBuff.append(enc2)

                    tf.write(encBuff)
                    encBuff.clear()

                else:
                    #buff is empty
                    #EOF encountered
                    flag = False



        except IOError:
            #this block executes when any IOError occurs
            status = 1
        except:
            #this block executes for any other error
            status = 2
        finally:
            #this block executes everytime
            if sf is not None:
                sf.close()
            if tf is not None:
                tf.close()
