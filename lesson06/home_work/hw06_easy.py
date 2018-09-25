import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, acord, bcord, ccord):
        """
        :param acord: list [Xa, Ya]
        :param bcrd: list [Xb, Yb]
        :param ccrd: list [Xc, Yc]
        """
        self.acord = acord
        self.bcord = bcord
        self.ccord = ccord
        self.sides = self.sides_length()

    def sides_length(self): 
        """
        :return: dictionary длины сторон {C : длина AB , B : длина AC , A :  длина BC }
        """
        return_dict = {}
        Xa, Ya = self.acord
        Xb, Yb = self.bcord
        Xc, Yc = self.ccord
        return_dict.update({"C": math.fabs(math.sqrt(((Xb - Xa) ** 2) + ((Yb - Ya) ** 2)))})
        return_dict.update({"B": math.fabs(math.sqrt(((Xc - Xa) ** 2) + ((Yc - Ya) ** 2)))})
        return_dict.update({"A": math.fabs(math.sqrt(((Xc - Xb) ** 2) + ((Yc - Yb) ** 2)))})
       # print(return_dict)
        return return_dict


    def area(self):
        Xa, Ya = self.acord
        Xb, Yb = self.bcord
        Xc, Yc = self.ccord
        return math.fabs(1/2 * (((Xa - Xc) * (Yb - Yc)) - ((Xb - Xc) * (Ya - Yc))))

    def height(self):
        area = self.area()
        return area * 2 / self.sides['A']

    def perimeter(self):
        return sum(self.sides.values())

    def print_result(self, *args):
        print("{} треугольника равна {}".format(*args))


triangle = Triangle([1, 1], [2, 5], [5, 3])
triangle.print_result("Площадь", triangle.area())
triangle.print_result("Высота", triangle.height())
triangle.print_result("Периметр", triangle.perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class EqualTrapezoid:

    def __init__(self, *args):
        if len(args) == 4:
            self.points = [p for p in args]
            self.sides = self.sides_length()
        else:
            print("Введите 4 координаты")
            exit()

    def sides_length(self):
        """
        :return: dictionary длины сторон {AB : длина AB , BC : длина BC , CD :  длина CD, DA: длина DA}
        """
        sides = {}
        side_names = ["AB", "BC", "CD", "DA"]
        for idx, point in enumerate(self.points):
            if idx < 3:
               next_cord = idx + 1
            else:
                next_cord = 0
            length_d = {side_names[idx]: math.fabs(math.sqrt(((self.points[next_cord][1] - point[1]) ** 2) + ((self.points[next_cord][0] - point[0]) ** 2)))}
            sides.update(length_d)
        return sides

    def is_isosceles(self):
        if self.sides["AB"] == self.sides["CD"] and self.sides["BC"] == self.sides["DA"]:
            print("Это параллелограмм")
        elif self.sides["AB"] == self.sides["CD"] or self.sides["BC"] == self.sides["DA"]:
            print("Трапеция равнобедренная")
        else:
            print("Трапеция не равнобедренная")

    def perimeter(self):
        return sum(self.sides.values())

    def area(self):
        h = math.sqrt(self.sides["AB"] ** 2 - (((((self.sides["DA"] - self.sides["BC"]) ** 2) + (self.sides["AB"] ** 2) - (self.sides["CD"] ** 2))) / (2 * (self.sides["DA"] - self.sides["BC"]))) ** 2)
        area = 0.5 * (self.sides["BC"] + self.sides["DA"]) * h
        return area

equalTrapezoid = EqualTrapezoid([1, 1], [2, 5], [6, 5], [7, 1])

equalTrapezoid.is_isosceles()

print("Длины сторон трапеции {}, {}, {}, {}" .format(*[s for s in equalTrapezoid.sides.values()]))
print("Периметр трапеции {}" .format(equalTrapezoid.perimeter()))
print("Площадь трапеции {}" .format(equalTrapezoid.area()))
