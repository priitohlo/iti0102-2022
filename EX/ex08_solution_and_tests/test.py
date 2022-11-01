import solution

def test_none():
    assert None is None

def test_student_study__night_coffee_true():
    assert solution.students_study(2, True) is False

def test_student_study__night_coffee_false():
    assert solution.students_study(2, False) is False

def test_student_study__day_coffee_true():
    assert solution.students_study(14, True) is True