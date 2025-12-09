import sys
matrices = []
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    def __str__(self):
       return '\n'.join([' '.join(map(str, row)) for row in self.data])
    def add(self, m2):
        if self.rows != m2.rows or self.cols != m2.cols:
            return ValueError('Matrices do not have the same dimensions')
        add_result = []
        for m in range(self.rows):
            new_row = []
            for n in range(self.cols):
                new_row.append(0)
            add_result.append(new_row)
        for m in range(self.rows):
            for n in range(self.cols):
                add_result[m][n] += (self.data[m][n] + m2.data[m][n])
        return Matrix(add_result)
    def multiply(self, m2):
        if self.rows != m2.cols or self.cols != m2.rows:
            return ValueError('Matrices do not have the same inner dimensions')
        mult_result = []
        for m in range(self.rows):
            new_row = []
            for p in range(m2.cols):
                new_row.append(0)
            mult_result.append(new_row)
        for m in range(self.rows):
            for p in range(m2.cols):
                for n in range(self.cols):
                    mult_result[m][p] += (self.data[m][n] * m2.data[n][p])
        return Matrix(mult_result)
    def scalar(self, scalar, row):
        scaled_matrix = []
        for m in range(self.rows):
            new_row = []
            for n in range(self.cols):
                new_row.append(0)
            scaled_matrix.append(new_row)
        for m in range(self.rows):
            for n in range(self.cols):
                if m != row:
                    scaled_matrix[m][n] += self.data[m][n]
                elif m == row:
                    scaled_matrix[m][n] += (scalar * self.data[m][n])
        return Matrix(scaled_matrix)

def matrix_input():
    m_dimensions = input('Matrix dimensions (R C): ')
    m_dimensions_list = m_dimensions.split(' ')
    try:
        r = int(m_dimensions_list[0])
        c = int(m_dimensions_list[1])
        values = input('Input your values (1 2 3 4...): ')
        values_list = values.split(' ')
        if len(values_list) == r*c:
            for i in range(len(values_list)):
                if '.' in values_list[i]:
                    float_value = float(values_list[i])
                    values_list[i] = float_value
                else:
                    int_value = int(values_list[i])
                    values_list[i] = int_value
            matrix = [values_list[i * c:(i + 1) * c] for i in range(r)]
            matrices.append(matrix)
            print(f'''
Matrix {matrices.index(matrix)+1} created!
''')
        else:
            print('''
There must be exactly enough values to fill each spot in the matrix and values have to be ints/floats
''')
    except: print('''
Inputs must be numbers and in the correct format (no floats for dimensions)
''')

def main():
    while True:
        print('''Functions:
1. Create matrix
2. Show matrix
3. Add matrices
4. Multiply matrices
5. Scale a row of a matrix
6. Exit''')
        func_type = input('Which function would you like to run?: ')
        if func_type == '1':
            matrix_input()
        elif func_type == '2':
            matrix_show = input('Which matrix would you like to show?: ')
            try:
                if -len(matrices) <= int(matrix_show)-1 < len(matrices):
                    matrix = Matrix(matrices[int(matrix_show)-1])
                    print(f'''
Matrix {int(matrix_show)}:''')
                    print(matrix.__str__())
                    print('')
                else: print('''
Matrix does not exist
''')
            except: print('''
Inputs must be integers
''')
        elif func_type == '3':
            matrices_added = input('Which matrices would you like to add (1 2)?: ')
            matrices_added_list = matrices_added.split(' ')
            try:
                m1 = int(matrices_added_list[0])-1
                m2 = int(matrices_added_list[1])-1
                if -len(matrices) <= m1 < len(matrices) and -len(matrices) <= m2 < len(matrices):
                    real_m1 = Matrix(matrices[m1])
                    real_m2 = Matrix(matrices[m2])
                    print(f'''
Matrices {m1+1} and {m2+1} added:''')
                    print(real_m1.add(real_m2))
                    print('')
                else: print('''
At least one inputted matrix does not exist
''')
            except: print('''
Inputs must be integers
''')
        elif func_type == '4':
            matrices_mult = input('Which matrices would you like to multiply (1 2)?: ')
            matrices_mult_list = matrices_mult.split(' ')
            try:
                m1 = int(matrices_mult_list[0])-1
                m2 = int(matrices_mult_list[1])-1
                if -len(matrices) <= m1 < len(matrices) and -len(matrices) <= m2 < len(matrices):
                    real_m1 = Matrix(matrices[m1])
                    real_m2 = Matrix(matrices[m2])
                    print(f'''
Matrices {m1+1} and {m2+1} multiplied:''')
                    print(real_m1.multiply(real_m2))
                    print('')
                else: print('''
At least one inputted matrix does not exist
''')
            except: print('''
Inputs must be integers
''')
        elif func_type == '5':
            scaled_matrix = input('Which matrix would you like to scale?: ')
            inputs = input('What is your scalar and what row would you like to multiply (scalar row)?: ')
            inputs_list = inputs.split(' ')
            try:
                m = int(scaled_matrix[0])-1
                if -len(matrices) <= m < len(matrices):
                    real_m = Matrix(matrices[m])
                    scalar = inputs_list[0]
                    if '.' in scalar:
                        real_scalar = float(scalar)
                    else: real_scalar = int(scalar)
                    row = int(inputs_list[1])-1
                    print(f'''
Row {row+1} in Matrix {int(scaled_matrix)} scaled by {real_scalar}:''')
                    print(real_m.scalar(real_scalar, row))
                    print('')
                else: print('''
Matrix does not exist
''')
            except: print('''
Matrix input must be an integer, row must exist and be an integer, and scalar must be an integer or a float
''')
        elif func_type == '6':
            print('''
See ya!
''')
            sys.exit()
        else: print('''
That function does not exist
''')
main()