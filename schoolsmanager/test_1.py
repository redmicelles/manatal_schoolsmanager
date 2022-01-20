from .models import School, Student
import pytest

@pytest.fixture()
def school_row(db):
    return School.objects.create(
       schoolname = "Loral",
       maxstudents = 40
    )

@pytest.fixture()
def student_row(db, school_row):
    return Student.objects.create(
      firstname = "Oluwaseyi",
      lastname = "Daniel",
      school = school_row,
      student_id = "LOR0001",
      age = 16,
      nationality = "Nigeria"
    )

def test_school(school_row):
    assert school_row.schoolname == "Loral"
    assert school_row.maxstudents == 40

def test_student(student_row):
    assert student_row.firstname == "Oluwaseyi"
    assert student_row.lastname == "Daniel"
    assert student_row.student_id == "LOR0001"
    assert student_row.age == 16
    assert student_row.nationality == "Nigeria"