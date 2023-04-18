class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create a serial number generator from start"""
        self.start = self.current = start #TODO: rename current -> next

    def __repr__(self):
        return f"<SerialGenerator start={self.start} current={self.current}>"

    def generate(self):
        """Generate serial number"""
        current_val = self.current
        self.current += 1
        return current_val

    def reset(self):
        """Reset to the original start number"""
        self.current = self.start


