import solution


def test_none():
    assert None is None


def test_student_study__night_coffee_true():
    assert solution.students_study(2, True) is False
    assert solution.students_study(2, False) is False
    assert solution.students_study(14, True) is True
    assert solution.students_study(19, False) is True
    assert solution.students_study(19, True) is True
    assert solution.students_study(17, True) is True
    assert solution.students_study(17, False) is False
    assert solution.students_study(4, True) is False
    assert solution.students_study(4, False) is False
    assert solution.students_study(17, True) is True
    assert solution.students_study(17, False) is False
