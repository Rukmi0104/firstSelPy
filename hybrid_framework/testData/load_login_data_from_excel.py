from hybrid_framework.utilities.xl_utilities import *
from hybrid_framework.utilities.read_config import read_config_class

def load_xl_login_data(xl_path, sheet):
    # get max row and max column
    max_row = get_max_row(xl_path, sheet)
    max_col = get_max_col(xl_path, sheet)
    print(max_col, max_row)

    # get list of tuple from excel
    '''
    1. create empty list
    2. append each row data in empty list using read_cell
    3. Now, we have 4 lists for 4 different test data
    4. convert these lists into tuple
    5. create single list of all 4 tuples and use in parameterization
    '''

    xl_data = []
    for r in range(2, max_row+1):
        emp_lst = []
        for c in range(1, max_col+1):
            emp_lst.append((read_cell(xl_path, sheet, r, c)))
        print(emp_lst)
        print(tuple(emp_lst))
        xl_data.append(tuple(emp_lst))
    print(xl_data)
    return xl_data
