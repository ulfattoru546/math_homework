  import random

  def get_random_code():
      number = str(random.randint(1,100))
      if len(number) == 2:
          return f"{number} * {number}"
      elif len(number) == 3:
          return f"{number} + {number}"
      else:
          return f"{number} - {number}"