from student import Student
from group import Group
from exception import GroupOverlimit

if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs') == st1, 'Test1.1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

    gr.delete_student('Taylor')
    print(gr)  # Only one student

    gr.delete_student('Taylor')  # No error!

    try:
        gr = Group("PD1")
        for i in range(15):
            st = Student("Male", 20 + i, f"FirstName{i}", f"LastName{i}", f"RB{i}")
            gr.add_student(st)
            print(f"Student {st.first_name} added.")
    except GroupOverlimit as e:
        print(f"Error: {e}")

    print(gr)
