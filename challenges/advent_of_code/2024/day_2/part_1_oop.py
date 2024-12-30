import doctest
from typing import List

class Report:
    """ A class representing an individual nuclear reactor report."""

    # instantiate class with report attribute passed, otherwise may not work (how?)
    def __init__(self, _report: List[int]):
        """
        Constructor method for report class.

        >>> report_1 = Report([0, 1, 2, 3])
        >>> print(report_1)
        Report([0, 1, 2, 3])
        """

        self._report = _report
        # initializing attribute needed for later method (could also create gap object)
        self._gaps = []

    def __str__(self) -> str:
        """
        Outputs string representation of class object.

        >>> report_1 = Report([0, 1, 2, 3])
        >>> report_1.__str__()
        'Report([0, 1, 2, 3])'
        """

        return f"Report({self._report})"

    def calculate_gaps(self):
        """
        Calculates gaps (difference between adjacent values) for a report.

        >>> report_1 = Report([-4, -2, 0, 1, 2, 5])
        >>> report_1.calculate_gaps()
        >>> report_1.get_gaps()
        [2, 2, 1, 1, 3]
        >>> report_2 = Report([5, 0, -3, 6, 8, -2])
        >>> report_2.calculate_gaps()
        >>> report_2.get_gaps()
        [-5, -3, 9, 2, -10]
        """

        # initializing previous number (starting with first element in list), and index
        previous_num = self._report[0]

        # iterate through list to calculate gaps
        for num in self._report[1:]:
            # calculate difference between adjacent numbers
            gap = num - previous_num
            self._gaps.append(gap)
            # update previous number to current number, for next iteration
            previous_num = num

        # NOT manipulating data now, in order to preserve sequence (will manipulate in later method)
        # also, don't need dictionary to associate gaps to report, since associate as object attribute
        # also, cannot have a list object as a dictionary key

    # another method that might not be useful
    def get_gaps(self) -> List[int]:
        """
        Provides access to gaps attribute for class object.

        Returns:
            (List[int]): list of gaps (differences) between adjacent numbers in report

        >>> report_1 = Report([-4, -2, 0, 1, 2, 5])
        >>> report_1.calculate_gaps()
        >>> report_1.get_gaps()
        [2, 2, 1, 1, 3]
        >>> report_2 = Report([29, 32, 34, 35, 35, 37, 38, 38])
        >>> report_2.calculate_gaps()
        >>> report_2.get_gaps()
        [3, 2, 1, 0, 2, 1, 0]
        >>> report_3 = Report([80, 82, 85, 86, 87, 90, 94])
        >>> report_3.calculate_gaps()
        >>> report_3.get_gaps()
        [2, 3, 1, 1, 3, 4]
        """

        return self._gaps

    def is_safe_report(self) -> bool:
        """
        Determines whether a report is safe or not, given criteria.

        Returns:
            (bool): returns evaluation of statement that given report is safe, or not

        >>> report_1 = Report([-4, -2, 0, 1, 2, 5])
        >>> report_1.calculate_gaps()
        >>> report_1.get_gaps()
        [2, 2, 1, 1, 3]
        >>> report_1.is_safe_report()
        True
        >>> report_2 = Report([29, 32, 34, 35, 35, 37, 38, 38])
        >>> report_2.calculate_gaps()
        >>> report_2.get_gaps()
        [3, 2, 1, 0, 2, 1, 0]
        >>> report_2.is_safe_report()
        False
        >>> report_3 = Report([80, 82, 85, 86, 87, 90, 94])
        >>> report_3.calculate_gaps()
        >>> report_3.get_gaps()
        [2, 3, 1, 1, 3, 4]
        >>> report_3.is_safe_report()
        False
        """
        # set for safe gap values (negative excluded since considered with absolutes)
        safe_gaps = {1, 2, 3}

        # need to check gaps of object, using set to remove duplicates
        for gap in set(self._gaps):
            # covers condition that report values must not differ by less than 1 and more than 3
            if abs(gap) not in safe_gaps:
                return False

        # sorting reports, backwards and forwards (either in ascending or descending order)
        reversed_report = sorted(self._report)[::-1]
        sorted_report = sorted(self._report)

        # no change implies that list was already ordered
        if self._report != reversed_report and self._report != sorted_report:
            return False

        return True

class AllReports:
    """ A class representing a collection of nuclear reactor reports."""

    def __init__(self, reports: List[List[int]]):
        """
        Constructor method for report class.

        >>> all_reports = AllReports([[-1, -2, -3], [0, 1, 2], [-4, 3, 1]])
        >>> print(all_reports)
        AllReports([[-1, -2, -3], [0, 1, 2], [-4, 3, 1]])
        """

        self._all_reports = reports

        self._safe_reports = []

    def __str__(self):
        """
        Outputs string representation of class object.

        >>> all_reports = AllReports([[-1, -2, -3], [0, 1, 2], [-4, 3, 1]])
        >>> all_reports.__str__()
        'AllReports([[-1, -2, -3], [0, 1, 2], [-4, 3, 1]])'
        """

        return f"AllReports({self._all_reports})"

    # do not think that this method is needed, or will be used
    def get_all_reports(self) -> List[List[int]]:
        """
        Method to extract all reports from class.

        >>> all_reports = AllReports([[-1, -2, -3], [0, 1, 2], [-4, 3, 1]])
        >>> all_reports.get_all_reports()
        [[-1, -2, -3], [0, 1, 2], [-4, 3, 1]]
        """

        return self._all_reports

    def create_reports(self) -> List[Report]:
        """
        Method to create list of reports as products.

        No tests, since output changes everytime based on memory address of report object.
        """

        report_objects = []

        for i in self._all_reports:
            report_objects.append(Report(i))

        return report_objects

    def get_safe_reports(self):
        """
        Method to retrieve safe reports from class object.

        Need to add test.
        """

        return self._safe_reports

    def add_safe_report(self, _report_: Report):
        """
        Method to add individual safe reports to list of safe reports.

        No tests since not sure how to loop in doctest test.
        """

        self._safe_reports.append(_report_)

    def number_safe_reports(self):
        """
        Calculate the number of safe reports.

        No tests for now.
        """

        return len(self._safe_reports)

def format_file(raw_data) -> List[List[int]]:
    """
    Converts raw input data from text file into usable data format (nested list).

    >>> test_reports = format_file('test_file.txt')
    >>> print(test_reports)
    [[60, 62, 61, 63, 67], [33, 36, 38, 35, 41], [44, 46, 48, 54, 53]]
    """
    # open file and extract numbers into lists, splitting to separate numbers
    with open(raw_data, 'r') as file:
        # separating data from file into nested list, sublist are lines from file
        file = file.readlines()
        # initializing empty list to store reformatted data
        all_reports = []
        for line in file:
            report = []
            # splitting line using spaces as delimiter
            line = line.split(' ')
            # nothing needed to remove next line character (perhaps due to integer conversion of each element?)
            # converting all numbers in lists into integers
            for num in line:
                num = int(num)
                report.append(num)
            all_reports.append(report)

    return all_reports

'''
calling function to instantiate all reports class and convert all reports into Class objects
now can iterate through formatted reports and use class methods on them
'''
formatted_reports = (AllReports(format_file('input.txt')))
all_reports = formatted_reports.create_reports()

for report in all_reports:
    # call method to calculate gaps, thus populating list of gaps for object
    report.calculate_gaps()
    # add safe reports to list of safe reports
    if report.is_safe_report():
        formatted_reports.add_safe_report(report)

print(formatted_reports.number_safe_reports())

doctest.testmod()