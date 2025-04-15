

# Case 1:
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        parts = numbers.split(',')
        return sum(int(num) for num in parts) 




