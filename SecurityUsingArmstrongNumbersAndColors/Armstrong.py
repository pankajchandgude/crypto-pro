class ArmstrongManager:
    #class level data
    #all objects share the one available copy
    _armstrongNumbers_ = [153,370,371,407]
    _baseTable_ = [1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, 2314, 2341, 2413, 2431, 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231, 4312, 4321]

    #methods accessible without object
    @classmethod
    def _KeyToNumber_(cls, key):
        # ASCII Sum
        keyL = len(key)
        i = 0
        sum = 0
        while i < keyL:
            sum += ord(key[i])
            i += 1

        return sum #portionB


    #build portion A of the XORKEY
    @classmethod
    def _getPermutationString_(cls, num):
        perm = cls._baseTable_[num % len(cls._baseTable_)]
        #say num % len(cls.baseTable) is 4
        #then perm will be 1423

        temp = ''#371, 370371, 407370371, 153407370371
        while perm >0:
            x = perm %10 -1 # 3-1,2-1,4-1,1-1
            temp = str(cls._armstrongNumbers_[x]) + temp;
            perm = perm //10 #142,14,1,0

        return temp #153407370371 (portion A)

    @classmethod
    def getXORKeY(cls, key):
        num = cls._KeyToNumber_(key)
        permutation = cls._getPermutationString_(num)
        xorkey = permutation+str(num)
        return  xorkey