# Question(#8): Given a string representing an integer, return that integer
# Solution: Parse the string and bulild up the number

def myAtoi(self, str: str) -> int:      
        # Firstly, strip the string of whitespaces, initialize variables to hold our number and the sign (positive or negative)
        str = str.lstrip()
        sign = 1
        base = i = 0

        if not str: return 0

        # If the string starts with a sign, set out sign variable appropriately
        if str[0] in '-+':
                sign = -1 if str[0] == '-' else 1
                str = str[1:]

        while i < len(str):
                # If we encounter something thats not a digit, we can break out of our loop 
                if not str[i].isdigit(): break

                # Multiply the number by 10 and add out current digit (this is a very common technique for building numbers from strings)
                base *= 10
                base += int(str[i])
                i += 1
                
                if base*sign >= 2**31-1: return 2**31-1
                if base*sign <= -2**31: return -2**31
        return base * sign 