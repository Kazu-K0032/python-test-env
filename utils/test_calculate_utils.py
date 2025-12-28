# utils/test_calculate_utils.pyのテストファイル

import sys
import pytest
from utils.calculate_utils import calculate_sum


class TestCalculateSum:
    """calculate_sum関数の包括的なテストスイート"""

    # パラメータ化テスト - 等価クラステスト
    @pytest.mark.parametrize("a,b,expected", [
        # 正数同士の組み合わせ
        (1, 2, 3),
        (10, 20, 30),
        (100, 200, 300),

        # 負数同士の組み合わせ
        (-1, -2, -3),
        (-10, -20, -30),

        # 正数と負数の組み合わせ
        (5, -3, 2),
        (-5, 3, -2),
        (10, -5, 5),

        # ゼロを含む組み合わせ
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (0, -5, -5),
        (-5, 0, -5),
    ])
    def test_calculate_sum_comprehensive(self, a: int, b: int, expected: int) -> None:
        """包括的なパラメータ化テスト"""
        result = calculate_sum(a, b)
        assert result == expected
        assert isinstance(result, int)

    # 境界値テスト
    def test_calculate_sum_large_numbers(self) -> None:
        """大きな数値の境界値テスト"""
        large_num = 10**18
        # 大きな正数同士
        assert calculate_sum(large_num, large_num) == 2 * large_num
        # 正数と負数の相殺
        assert calculate_sum(large_num, -large_num) == 0
        # Pythonのintは任意精度なのでオーバーフローは発生しない
        very_large = 10**100
        assert calculate_sum(very_large, very_large) == 2 * very_large

    def test_calculate_sum_min_max_int(self) -> None:
        """システムのint境界値テスト"""
        # Pythonではsys.maxsizeはCのlongの最大値
        max_int = sys.maxsize
        min_int = -sys.maxsize - 1
        assert calculate_sum(max_int, 0) == max_int
        assert calculate_sum(min_int, 0) == min_int

    # プロパティベーステスト - 数学的性質の検証
    @pytest.mark.parametrize("a,b", [
        (1, 2),
        (-1, 3),
        (0, 5),
        (10, -5),
        (-10, -5),
    ])
    def test_calculate_sum_commutative(self, a: int, b: int) -> None:
        """交換法則のテスト: a + b = b + a"""
        assert calculate_sum(a, b) == calculate_sum(b, a)

    def test_calculate_sum_associative(self) -> None:
        """結合法則のテスト: (a + b) + c = a + (b + c)"""
        test_cases = [
            (1, 2, 3),
            (-1, 2, -3),
            (0, 5, -5),
        ]
        for a, b, c in test_cases:
            left_side = calculate_sum(calculate_sum(a, b), c)
            right_side = calculate_sum(a, calculate_sum(b, c))
            assert left_side == right_side

    def test_calculate_sum_identity(self) -> None:
        """単位元のテスト: a + 0 = a"""
        test_values = [0, 1, -1, 100, -100, 10**10, -10**10]
        for value in test_values:
            assert calculate_sum(value, 0) == value
            assert calculate_sum(0, value) == value

    def test_calculate_sum_inverse(self) -> None:
        """逆元のテスト: a + (-a) = 0"""
        test_values = [1, -1, 100, -100, 10**10, -10**10]
        for value in test_values:
            assert calculate_sum(value, -value) == 0

    # 型チェックテスト（mypyで検出されるべき）
    def test_calculate_sum_type_preservation(self) -> None:
        """戻り値がint型であることを確認"""
        result = calculate_sum(1, 2)
        assert isinstance(result, int)
        assert type(result) == int
