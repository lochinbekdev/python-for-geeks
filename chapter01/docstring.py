def double(n):
    '''Takes in a number n,return the double of its value'''
    return n**2


print(double.__doc__)

help(double)


# Commentlar structurasi tavfsiya qilinadi

# Xulosa : odatda bir qatorda bo'ladi
# Birinchi bo'sh qator
# Boshqa tariflar docstringga tegishli bo'lgan
# Ikkinchi bo'sh qator

class ComplexNumber:
    """
    This is a class for mathematical operation on complex numbers.

    Attributes:
        real(int):The real part of complex number.
        imag(int):The imaginary part of complex number.
    """

    def __init__(self, real, imag):
        """
       The constructor for ComplexNumber class.

        Attributes:
            real(int):The real part of complex number.
            imag(int):The imaginary part of complex number.
        """

    def add(self, num):
        """
        The function to add two Complex Numbers.

        Parameters:
            num(ComplexNumber): The complex number to be added.

        Returns:
            ComplexNumber: A complex number which contains the sum.
        """
    re = self.real + num.real
    im = self.imag + num.imag

    return ComplexNumber(re,im)
