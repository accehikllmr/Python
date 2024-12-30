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

    def get_report(self) -> List[int]:
        """

        :return:
        """

        return self._report

    def set_gaps(self, new_gaps: List[int]) -> List[int]:
        """


        """

        self._gaps = new_gaps

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

unsafe_reports = []

for report in all_reports:
    # call method to calculate gaps, thus populating list of gaps for object
    report.calculate_gaps()
    # add safe reports to list of safe reports
    if report.is_safe_report():
        formatted_reports.add_safe_report(report)
    else:
        unsafe_reports.append(report)

#print(formatted_reports.number_safe_reports())

# instead of dealing with gaps (since they have positive and negative values) try dealing with the reports themselves
# NO, SINCE ALL REPORTS ARE EVALUATED ACCORDING TO THEIR GAPS
# CANNOT USE UNSAFE REPORT EVALUATION METHOD SINCE WHEN REMOVING GAP, REPORT IS NOT UPDATED
# for ordered unsafe reports, there are two cases:
# --- with no duplicate values, only removing the beginning or end value can make it safe
# --- with duplicate values, only removing the duplicate value can make it safe
# for unordered unsafe reports, there are two cases:
# --- if gap occurs at extremity, remove problematic gap
# --- otherwise, remove problematic gap and add new gap (removed gap + next gap)

# iterate through unsafe reports
count = 0
new_gaps = []
for u in unsafe_reports:
    # condition for ordered reports
    if u.get_report() == sorted(u.get_report()) or u.get_report() == sorted(u.get_report())[::-1]:
        # check for has duplicate values in report
        if u.get_gaps().count(0) != 0:
            # removing at least one zero from gaps
            new_gaps = u.get_gaps()
            new_gaps.remove(0)
        else:
            # condition to check whether beginning or end should be truncated (not one of three acceptable values)
            # no need to consider +/- since ordered, so all gaps have same sign
            if abs(u.get_gaps()[0]) != 1 and abs(u.get_gaps()[0]) != 2 and abs(u.get_gaps()[0]) != 3:
                # removing beginning of list
                new_gaps = u.get_gaps()[1:]
            # if beginning is fine, check end
            else:
                # removing end of list
                new_gaps = u.get_gaps()[:-1]
    # condition for unordered reports
    else:
        # condition for differentiating between most positive and mostly negative gaps
        if sum(u.get_gaps()) > 0:
            # condition to check beginning or end to truncate
            if u.get_gaps()[0] != 1 and u.get_gaps()[0] != 2 and u.get_gaps()[0] != 3:
                new_gaps = u.get_gaps()[1:]
            elif u.get_gaps()[-1] != 1 and u.get_gaps()[-1] != 2 and u.get_gaps()[-1] != 3:
                new_gaps = u.get_gaps()[:-1]
            else:
                for i in u.get_gaps():
                    if i < 0:
                        # copying list to not change one in product object
                        new_gaps = u.get_gaps()
                        index_i = new_gaps.index(i)
                        # inserting new value in list, bad value + next value (new gap)
                        new_gap = i + new_gaps[index_i + 1]
                        new_gaps.insert(index_i, new_gap)
                        new_gaps.remove(i)
        else:
            if u.get_gaps()[0] != -1 and u.get_gaps()[0] != -2 and u.get_gaps()[0] != -3:
                new_gaps = u.get_gaps()[1:]
            elif u.get_gaps()[-1] != -1 and u.get_gaps()[-1] != -2 and u.get_gaps()[-1] != -3:
                new_gaps = u.get_gaps()[:-1]
            else:
                for i in u.get_gaps():
                    if i > 0:
                        # copying list to not change one in product object
                        new_gaps = u.get_gaps()
                        index_i = new_gaps.index(i)
                        # inserting new value in list, bad value + next value (new gap)
                        new_gap = i + new_gaps[index_i + 1]
                        new_gaps.insert(index_i, new_gap)
                        new_gaps.remove(i)
    # check that new_gaps is safe before checking next report
    string = ""
    for m in new_gaps:
        safe_gaps = {1, 2, 3}
        for gap in new_gaps:
            if abs(gap) not in safe_gaps:
                string += '_'
            else:
                # assuming that positive sum implies all positive integers (which it does if all negatives are removed)
                if sum(new_gaps) > 0 > m:
                    string += '_'
                # same but with negatives
                elif sum(new_gaps) < 0 < m:
                    string += '_'
    if string == "":
        count += 1

print(formatted_reports.number_safe_reports() + count)


    # condition for unordered reports

'''
n = 0

for mehport in unsafe_reports:
    # collect unsafe reports gaps
    mehport.calculate_gaps()
    # convert gaps into sets, to condense, and back into list
    set_gaps = sorted(list(set(mehport.get_gaps())))
    # determine whether ascending or descending
    if set_gaps[0] > 0:
        # removing last element (largest number) might make it safe
        mehport.set_gaps(set_gaps[:-1])
        if mehport.is_safe_report():
            formatted_reports.add_safe_report(mehport)
            n += 1
    elif set_gaps[0] < 0:
        # removing first element (smallest number) might make it safe
        mehport.set_gaps(set_gaps[:1])
        if mehport.is_safe_report():
            formatted_reports.add_safe_report(mehport)
            n += 1
    else:
        # list starting at 0, so removing it might make it safe
        set_gaps.remove(0)
        # evaluating again, now that single problem has been removed
        if mehport.is_safe_report():
            formatted_reports.add_safe_report(mehport)
            n += 1

print(formatted_reports.number_safe_reports())
print(n)

doctest.testmod()
'''

