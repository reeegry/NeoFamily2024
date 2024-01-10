def f(x):
    return (ваша функция)

for a in range(1, 1000): # всегда внимательно следите за диапозоном
    if all(f(x) for x in range(1, 1000)): # Если функция должна быть ложью, то all(f(x) == 0for x in range(1, 1000))
        print(a)