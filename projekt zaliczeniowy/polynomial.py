import numbers

class Polynomial:

    def __init__(self, coefficients):
        if isinstance(coefficients, numbers.Number):
            self.coeffs = [coefficients]
        else:
            self.coeffs = list(coefficients)
        
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()    
        if not self.coeffs:
            self.coeffs = [0]

    def is_zero(self):
        if len(self.coeffs) == 1 and self.coeffs[0] == 0:
            return True
        return False

    def degree(self):
        return len(self.coeffs) - 1
    
    def __add__(self, other):
        if isinstance(other, numbers.Number):
            other_coeffs = [other]
        elif isinstance(other, Polynomial):
            other_coeffs = other.coeffs
        else:
            return NotImplemented

        max_len = max(len(self.coeffs), len(other_coeffs))
        result = [0] * max_len
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other_coeffs[i] if i < len(other_coeffs) else 0
            result[i] = a + b
        return Polynomial(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            other_coeffs = [other]
        elif isinstance(other, Polynomial):
            other_coeffs = other.coeffs
        else:
            return NotImplemented

        max_len = max(len(self.coeffs), len(other_coeffs))
        result = [0] * max_len
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other_coeffs[i] if i < len(other_coeffs) else 0
            result[i] = a - b
        return Polynomial(result)

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return Polynomial(other) - self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Polynomial([c * other for c in self.coeffs])
        
        if isinstance(other, Polynomial):
            result = [0] * (self.degree() + other.degree() + 1)
            for i in range(len(self.coeffs)):
                for j in range(len(other.coeffs)):
                    result[i + j] += self.coeffs[i] * other.coeffs[j]
            return Polynomial(result)
            
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def value(self, x):
        result = 0
        for c in reversed(self.coeffs):
            result = result * x + c
        return result

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            other = Polynomial(other)
            
        if not isinstance(other, Polynomial):
            return False
            
        diff = self - other
        return diff.is_zero()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, x):
        if x < 0:
            raise IndexError("Potęga musi być >= 0")
        if x >= len(self.coeffs):
            return 0
        return self.coeffs[x]

    def __str__(self):
        if self.is_zero():
            return "0"

        terms = []
        for i in reversed(range(len(self.coeffs))):
            coeff = self.coeffs[i]
        
            if coeff == 0:
                continue

            if i == 0:
                term = str(coeff)          
            elif i == 1:
                term = str(coeff) + "x"    
            else:
                term = str(coeff) + "x^" + str(i) 
        
            terms.append(term)

        result = " + ".join(terms)
        return result.replace("+ -", "- ")