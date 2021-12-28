class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        power = -1
        while num > 0 :
            power += 1
            digit = num % 10
            num = num // 10
            exponent = (10 ** power)
            value = digit * exponent
            toadd = ""
            print(digit, value)
            if value == 0:
                continue
            elif value >= 1 and value <= 9:
                if value == 4:
                    toadd = "IV"
                elif value == 9:
                    toadd = "IX"
                else:
                    dividend = value // 5
                    remainder = (value % 5) // exponent 
                    toadd = "V"*dividend + "I"*remainder
            elif value >= 10 and value <= 90:
                if value == 40:
                    toadd = "XL"
                elif value == 90:
                    toadd = "XC"
                else:
                    dividend = value // 50
                    remainder = (value % 50) // exponent
                    toadd = "L"*dividend + "X"*remainder
            elif value >= 100 and value <= 900:
                if value == 400:
                    toadd = "CD" 
                elif value == 900:
                    toadd = "CM"
                else:
                    dividend = value // 500
                    remainder = (value % 500) // exponent
                    toadd = "D"*dividend + "C"*remainder
            else:
                toadd = "M"*digit
            result = toadd + result
        return result

                    
                    