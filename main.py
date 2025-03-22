def calc_quadrilateral_area(width, length):
   area = width * length
   return area

print(f"\nA área do quadrilátero é: {calc_quadrilateral_area(5, 2)}")

def calc_quadrilateral_perimeter(width, length):
   perimeter = 2 * (width + length)
   return perimeter

print(f"\nO perímetro do quadrilátero é: {calc_quadrilateral_perimeter(5,6)}")

def calc_triangle_area(base, height):
   area = (base * height) / 2
   return area

print(f"\nA área do triângulo é: {calc_triangle_area(5, 2)}")

def calc_triangle_perimeter(a, b, c):
   perimeter = a + b + c
   return perimeter

print(f"\nO perímetro do triângulo é: {calc_triangle_perimeter(7,9,5)}")