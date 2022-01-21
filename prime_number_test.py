def prime():
  a=1
  b=1
  flag = None

  while True:
    
    if a == 1:
      flag = False
      break
    else:
      if a > 1:
        for i in range(2,a):
          if (a % i) == 0:
            flag = True
            break
    if flag:
      mes = f"{a} is not a Prime."
      flag = None
      a += b
    else:
      mes = f"{a} is PRIME."
      flag = None
      a += b
    print(mes)
    return mes

prime()