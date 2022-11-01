from solution import *


def test_none():
    assert None is None


def test_student_study():
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
    assert lottery(5, 5, 5) is 10
    assert lottery(6, 6, 6) is 5
    assert lottery(-6, -6, -6) is 5
    assert lottery(0, 0, 0) is 5

    assert lottery(4, 4, 5) is 0
    assert lottery(4, 5, 4) is 0
    assert lottery(5, 4, 4) is 1

    assert lottery(4, 5, 6) is 1
