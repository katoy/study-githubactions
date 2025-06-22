class NumberHolder:
    """
    2つの整数を保持するクラス。

    Attributes:
        num1 (int): 1つ目の整数。
        num2 (int): 2つ目の整数。
    """
    def __init__(self, num1: int, num2: int):
        """
        NumberHolder の新しいインスタンスを初期化します。

        Args:
            num1 (int): 1つ目の整数。
            num2 (int): 2つ目の整数。
        """
        if not isinstance(num1, int):
            raise TypeError("num1 must be an integer")
        if not isinstance(num2, int):
            raise TypeError("num2 must be an integer")
        self.num1 = num1
        self.num2 = num2

    def get_numbers(self) -> tuple[int, int]:
        """
        保持している2つの整数を返します。

        Returns:
            tuple[int, int]: 2つの整数を含むタプル。
        """
        return self.num1, self.num2
