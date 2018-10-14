from math import gcd
import numpy


class Group:
    def __init__(self, elements, operation, table_name_map):
        """
        elements:       elements of the group
        operation:      operation on group
        table_name_map: map for cayley table to prettify any complex objects in groups for printing
        """
        self.elements = elements
        self.operation = operation
        self.table_name_map = table_name_map
        self.id = None  # placeholder to find group identity later
        self.order = len(elements)+1

    def compose(self, e1, e2):
        """
        e1: element 1 of composition
        e2: element 2 of composition

        returns the composition of e1 and e2. read "e1 o e2"
        """
        # if (e1 not in self.elements) or (e2 not in self.elements):
        #raise Exception('Elements not in group.')
        e1 %= self.order
        e2 %= self.order
        value = self.operation(e1, e2)
        if value not in self.elements:
            raise Exception(
                'Closure does not hold for {0} + {1} = {2}.'.format(e1, e2, value))
        return value

    def identity(self):
        """
        Gets the identity of the group
        """
        """if self.id:
            return self.id  # if already found return
        for element in self.elements:
            for test_element in self.elements:
                if not (self.compose(element, test_element) == test_element):
                    break
            self.id = element
            return element
        # shouldn't reach
        raise Exception('No identity, not a group')"""
        return 1

    # If G is in fact a group then this function always returns
    def inverse(self, e):
        return int((XEuclidean(e, self.order)[0] + self.order) % self.order)

    def power(self, g, e):
        return pow(g, e, self.order)

    def __repr__(self):
        longest = max(len(str(v)) for k, v in self.table_name_map.items()) + 2
        # makes an element into a guarenteed len cell

        def cell(data, filler=' '):
            # thanks https://stackoverflow.com/questions/5676646/how-can-i-fill-out-a-python-string-with-spaces
            return '{message:{fill}{align}{width}}'.format(
                message=data,
                fill=filler,
                align='^',
                width=longest
            )
        # maps elements to pretty values and strs

        def data_cell(e):
            return cell(str(self.table_name_map[e]))
        vert_sepr = '|'  # vertical bar separator

        def hori_sepr(char):  # horizontal row separator
            return cell('', filler=char)

        def row_sepr(char):  # row separator
            return (hori_sepr(char) + vert_sepr * 2) + ((hori_sepr(char) + vert_sepr) * len(self.elements)) + '\n'

        cayley = cell('o') + vert_sepr * 2
        # headers
        for header in self.elements:
            cayley += data_cell(header) + vert_sepr
        cayley += '\n' + row_sepr('=')

        # table
        for row in self.elements:
            line = (data_cell(row) + vert_sepr * 2)
            for column in self.elements:
                line += data_cell(self.compose(row, column)) + vert_sepr
            cayley += line + '\n' + row_sepr('-')
        return cayley


def coprime(a, b):
    return gcd(a, b) == 1


def U(n):
    elements = [e for e in range(1, n) if coprime(e, n)]
    return Group(elements, lambda e1, e2: ((e2 * e1) % n), {e: e for e in elements})


def Z(n):
    elements = [e for e in range(0, n)]
    return Group(elements, lambda e1, e2: ((e2 + e1) % n), {e: e for e in elements})


def XEuclidean(u, v, verbose=False):
    # extended euclidean algorithm
    U = numpy.array([1, 0, int(u)])
    V = numpy.array([0, 1, int(v)])
    if verbose:
        print("U=", U, "")
        print("V=", V, "\n")
    while V[2] != 0:
        q = U[2] // V[2]
        R = U - V * q
        # print "R=",R,"\n"
        U = V
        V = R
        if verbose:
            print("U=", U, "")
            print("V=", V, "\n")
            print(u, "*", U[0], "+", v, "*", U[1], "=", U[2], "\n")
    # (u0,u1,u2) -> u*u0+v*u1=u2
    return U
