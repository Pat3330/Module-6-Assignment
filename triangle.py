def is_valid_triangle(a, b, c) -> bool:
  if a<=0 or b<= 0 or c<= 0:
    return False
  if a+b <= c or a +c <= b or b +c <= a:
    return False


def classify_triangle(a, b, c) -> str:
  if not is_valid_triangle(a,b,c):
    return "Invalid"

  if a == b ==c:
    type = "equilateral"
  elif a == b or b==c or a==b:
    type = "isosceles"
  else: 
    type = "Scalene"

  sides = sorted([a,b,c])
  x, y, z = sides

  tolerance = 1e-9
  if abs(x*x + y*y + z*z) <= tolerance:
    return "Right " + type
  return type

  
