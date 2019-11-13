def cycle():
	while True:
		try:
			a = float(input("a = "))
			b = float(input("b = "))
			c = float(input("c = "))
			D = (b ** 2) - (4*a*c)
			if D >= 0:
				ID = D**0.5
				print("D =", D)
				if D > 0:
					print("√D =", ID)
					x1 = (-b-ID)/(2*a)
					x2 = (-b+ID)/(2*a)
					print('x1 =',x1)
					print('x2 =',x2)
					print(" ")
					print(" ")
				elif D == 0:
					x = -b/(2*a)
					print('x =',x)
					print(" ")
					print(" ")			
			else:
				print("D =",D)
				print("Розв'язку немає!")
				print(" ")
				print(" ")
		except ValueError:
			print("Вводити тільки числа!!")
while True:
	cycle()