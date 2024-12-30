import doctest

# Q1

class Squirtle:

    def __init__(self):
        """
        Constructor to instantiate class object.

        >>> squirtle = Squirtle()
        >>> squirtle._hp
        44
        >>> squirtle._pp
        300
        """
        # instance variables are invariant among class objects
        self._hp = 44
        self._pp = 300

    def water_gun(self):
        """
        Water type attack that consumes 25 pp.

        >>> squirtle = Squirtle()
        >>> squirtle.water_gun()
        >>> squirtle._pp
        275
        """

        self._pp -= 25

    def bite(self):
        """
        Normal type attack that consumes 25 pp.

        >>> squirtle = Squirtle()
        >>> squirtle.bite()
        >>> squirtle._pp
        275
        """

        self._pp -= 25

    def skull_bash(self):
        """
        Fighting type attack that consumes 10 pp.

        >>> squirtle = Squirtle()
        >>> squirtle.skull_bash()
        >>> squirtle._pp
        290
        """

        self._pp -= 10

    def hydro_pump(self):
        """
        Water type attack that consumes 5 pp.

        >>> squirtle = Squirtle()
        >>> squirtle.hydro_pump()
        >>> squirtle._pp
        295
        """

        self._pp -= 5

    def being_attacked(self, damage: int):
        """
        Attack by another Pokémon reduces hp by a given amount.

        Parameters:
            damage (int): amount of hp lost by opposing Pokémon attack

        >>> squirtle = Squirtle()
        >>> squirtle.being_attacked(25)
        >>> squirtle._hp
        19
        >>> squirtle.being_attacked(20)
        Squirtle needs treatment!
        >>> squirtle._hp
        0
        """

        # Pokémon faints at 0, so hp cannot be negative
        if damage >= self._hp:
            self._hp = 0
            self.need_treatment()
        else:
            self._hp -= damage

    def being_treated(self):
        """
        Treatement from pokemon centre recovers all hp and pp to max value.

        >>> squirtle = Squirtle()
        >>> squirtle.hydro_pump()
        >>> squirtle._pp
        295
        >>> squirtle.being_attacked(40)
        >>> squirtle._hp
        4
        >>> squirtle.being_treated()
        >>> squirtle._hp
        44
        >>> squirtle._pp
        300
        """
        # reinitializing hp and pp to default values (is there a simpler way?)
        self._hp = 44
        self._pp = 300

    # warning about static method, since method does not depend on object at all (can disregard for now)
    def need_treatment(self):
        """
        Outputs message that squirtle object needs treatement (i.e. hp = 0)

        >>> squirtle = Squirtle()
        >>> squirtle.being_attacked(44)
        Squirtle needs treatment!
        >>> squirtle._hp
        0
        """

        print(f"Squirtle needs treatment!")

# Q2

from typing import Dict
from typing import List

class Student:

    def __init__(self, _id: int, _name: str, _grades: Dict[str, int]):
        """
        Constructor method to instantiate student objects.

        Parameters:
            _id (int): unique student identification number
            _name (str): full name of student
            _grades (Dict[str, int]): graded-work name and grade pairings

        >>> michel = Student(720495, "Michel Clark", {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        >>> michel._id
        720495
        >>> michel._name
        'Michel Clark'
        >>> michel._grades
        {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71}
        """

        self._id = _id
        self._name = _name
        self._grades = _grades

    def calculate_average(self):
        """
        Calculates student average and adds it to grades.

        >>> michel = Student(720495, "Michel Clark", {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        >>> michel.calculate_average()
        >>> michel.__str__()
        "Student(720495, Michel Clark, {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71, 'average': 80})"
        """

        grade_sum = 0

        # iterate through all grade values in grades dictionary
        for _grade in self._grades.values():
            # grade stored as string in dictionary, so convert to int
            grade_sum += int(_grade)

        # round first, to get correct rounding, and then convert to int
        average = int(round(grade_sum / len(self._grades), 0))

        # add new key-pair item to grades dictionary for student
        self._grades['average'] = average


    def __lst__(self):
        """
        Returns list representation of object.

        >>> michel = Student(720495, "Michel Clark", {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        >>> michel.__lst__()
        [720495, 'Michel Clark', {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71}]
        """

        return [self._id, self._name, self._grades]

    def __str__(self) -> str:
        """
        Outputs string representation of object.

        >>> michel = Student(720495, "Michel Clark", {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        >>> print(michel)
        Student(720495, Michel Clark, {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        """
        return f"Student({self._id}, {self._name}, {self._grades})"

    def get_student_id(self):
        """
        Getter function for student id attribute.

        >>> michel = Student(720495, "Michel Clark", {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        >>> michel.get_student_id()
        720495
        """

        return self._id


class ComputerScienceClass:

    def __init__(self, _keys: List[str]):
        """
        Constructor method to instantiate course object.

        >>> course = ComputerScienceClass(['id', 'student_name', 'grades'])
        >>> course.get_keys()
        ['id', 'student_name', 'grades']
        >>> course.get_student_list()
        []
        """

        self._student_list = []
        self._keys = _keys

    def get_keys(self) -> List[str]:
        """
        Defines keys used to identify information in csv file.

        >>> course = ComputerScienceClass(['id', 'student_name', 'grades'])
        >>> course.get_keys()
        ['id', 'student_name', 'grades']
        """

        return self._keys

    def get_student_list(self) -> List[Student]:
        """
        Returns current student list.

        >>> student_1 = Student(720496, "Michel Clark", {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        >>> student_2 = Student(720495, "Michelle Clark", {'lab_1': 86, 'lab_2': 93, 'assignment': 89, 'midterm': 64, 'final': 72})
        >>> course = ComputerScienceClass(['id', 'student_name', 'grades'])
        >>> course.add_student(student_1)
        >>> course.add_student(student_2)
        >>> student_list = course.get_student_list()
        >>> print(student_list[1])
        Student(720496, Michel Clark, {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        """

        return self._student_list

    def print_student_list(self):
        """
        Prints student list.

        >>> student_1 = Student(720495, "Michel Clark", {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        >>> student_2 = Student(720496, "Michelle Clark", {'lab_1': 86, 'lab_2': 93, 'assignment': 89, 'midterm': 64, 'final': 72})
        >>> course = ComputerScienceClass(['id', 'student_name', 'grades'])
        >>> course.add_student(student_1)
        >>> course.add_student(student_2)
        >>> course.print_student_list()
        Student(720495, Michel Clark, {'lab_1': 85, 'lab_2': 92, 'assignment': 88, 'midterm': 63, 'final': 71})
        Student(720496, Michelle Clark, {'lab_1': 86, 'lab_2': 93, 'assignment': 89, 'midterm': 64, 'final': 72})
        """

        for _i in self._student_list:
            print(_i)

    def add_student(self, student_: Student):
        """
        Adds student object to list of students in the course.

        Parameters:
            student_ (Student): student object to be added to course list

        >>> course = ComputerScienceClass(['id', 'student_name', 'grades'])
        >>> student_1 = Student(720496, "Michelle Clark", {'lab_1': 86, 'lab_2': 93, 'assignment': 89, 'midterm': 64, 'final': 72})
        >>> course.add_student(student_1)
        >>> course.print_student_list()
        Student(720496, Michelle Clark, {'lab_1': 86, 'lab_2': 93, 'assignment': 89, 'midterm': 64, 'final': 72})
        """

        # implementing a sorting algorithm to sort students in ascending order of id number
        # for empty list, simply append to list (same for new id larger than the largest current id value)
        if len(self._student_list) == 0 or student_.get_student_id() > self._student_list[-1].get_student_id():
            self._student_list.append(student_)
        # otherwise, need to iterate through list to find appropriate positioning (i.e. sorting algorithm)
        else:
            # iterate trough list to find appropriate positioning for object
            for _i_ in self._student_list:
                if student_.get_student_id() < _i_.get_student_id():
                    self._student_list.insert(self._student_list.index(_i_), student_)
                    break

# opening original file, in order to extract contents
with open('student_record.csv', 'r') as student_record:
    # storing csv file into list, each element is a separate line
    students = student_record.readlines()
    # iterating using indices, since otherwise updating value does not work
    for student in range(len(students)):
        # every element of the students collection is split by comma, in order to separate different data
        students[student] = students[student].split(',')
        # iterating through items of newly made collection to clean up formatting
        for info in range(len(students[student])):
            # cleaning up symbols in first collection, for column titles
            if info == 0 and student == 0:
                students[student][info] = students[student][info][3:]
            # removing new line character from all final elements in all error_checking_and_collections
            if info == len(students[student]) - 1:
                students[student][info] = students[student][info][:-1]

    # extracting column header information from formatted list, but only need assignment headers
    columns = students[0]

    # adding to calculate average, not included in original data
    columns += ["average"]

    # extracting student information from formatted list
    students = students[1:]

    # instantiation of course object, before looping otherwise overwrites each time, adding class keys
    cs_class = ComputerScienceClass(columns)    # unsure why PyCharm seeing columns as str...

    # iterating through formatted list of students
    for student in students:
        # extracting student info from formatted list
        id_ = int(student[0])
        name = student[1]
        # creating dictionary for grades, using headers as keys and grades as values
        grades = {
            columns[2]: student[2],
            columns[3]: student[3],
            columns[4]: student[4],
            columns[5]: student[5],
            columns[6]: student[6]
        }

        '''
        appending object with specific information for student
        issue since accessing challenges class attribute - resolved by implementing class method for adding students
        '''
        cs_class.add_student(Student(id_, name, grades))

    #
    for _student_ in cs_class.get_student_list():
        _student_.calculate_average()

with open('student_record_reformatted.csv', 'w') as student_record_re:
    # iterating through each key for the row information
    for j in range(len(cs_class.get_keys())):
        # starting each row with the corresponding key for the row information
        student_record_re.write(str(cs_class.get_keys()[j]))
        # iterating through all objects in course object
        for i in cs_class.get_student_list():
            # converting object into list, to extract its information
            i = i.__lst__()
            # for first two values, since afterward dealing with dictionary object (not the simplest implementation)
            if j < 2:
                # simply writing element from the list
                student_record_re.write(',' + str(i[j]))
            # to deal with dictionary object
            else:
                # writing element from list paired with current key (indexed by j, since current row key)
                student_record_re.write(',' + str(i[2][cs_class.get_keys()[j]]))
        # to begin new line for next student
        student_record_re.write('\n')


doctest.testmod()