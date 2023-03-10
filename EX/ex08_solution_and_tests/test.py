"""Tests."""
from solution import students_study
from solution import lottery
from solution import fruit_order


def test_none():
    """Test none."""
    assert None is None


def test_student_study():
    """Test study."""
    assert students_study(2, True) is False
    assert students_study(2, False) is False

    assert students_study(14, True) is True
    assert students_study(14, False) is False

    assert students_study(19, False) is True
    assert students_study(19, True) is True

    assert students_study(18, True) is True
    assert students_study(18, False) is True
    assert students_study(24, True) is True
    assert students_study(24, False) is True

    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False

    assert students_study(5, True) is True
    assert students_study(5, False) is False
    assert students_study(17, True) is True
    assert students_study(17, False) is False


def test_lottery():
    """Test lottery."""
    assert lottery(5, 5, 5) == 10
    assert lottery(6, 6, 6) == 5
    assert lottery(-6, -6, -6) == 5
    assert lottery(0, 0, 0) == 5

    assert lottery(4, 4, 5) == 0
    assert lottery(4, 5, 4) == 0
    assert lottery(5, 4, 4) == 1

    assert lottery(4, 5, 6) == 1


def test_fruit_order_zeroes():
    """Test zeroes."""
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(0, 1, 0) == 0
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(1, 1, 0) == 0


def test_fruit_order_only_big():
    """Test big."""
    assert fruit_order(0, 1, 5) == 0
    assert fruit_order(0, 1, 10) == -1
    assert fruit_order(0, 1, 9) == -1
    assert fruit_order(0, 2, 5) == 0
    assert fruit_order(0, 2, 6) == -1


def test_fruit_order_only_small():
    """Test small."""
    assert fruit_order(6, 0, 6) == 6
    assert fruit_order(6, 0, 7) == -1
    assert fruit_order(1, 0, 1) == 1
    assert fruit_order(1, 0, 2) == -1
    assert fruit_order(2, 0, 1) == 1


def test_fruit_order_various():
    """Test various."""
    assert fruit_order(6, 1, 11) == 6
    assert fruit_order(5, 1, 10) == 5

    assert fruit_order(4, 1, 4) == 4  # all smalls, some bigs
    assert fruit_order(1, 2, 10) == 0  # some smalls, all bigs
    assert fruit_order(5, 3, 14) == 4  # some smalls, some bigs
    assert fruit_order(1, 1, 7) == -1  # not enough
    assert fruit_order(3, 3, 14) == -1  # enough bigs, not enough smalls
    assert fruit_order(6, 1, 13) == -1  # not enough with more than 5 smalls

    assert fruit_order(1, 300, 1499) == -1
    assert fruit_order(1000, 3000, 16000) == 1000
