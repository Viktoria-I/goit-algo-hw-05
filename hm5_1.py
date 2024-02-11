def caching_fibonacci():  # ФУНКЦІЯ caching_fibonacci

    cache = {} # Створити порожній словник cache

    def fibonacci(n):  # ФУНКЦІЯ fibonacci(n)
        if n <= 0:  # Якщо n <= 0
            return 0  # Повернути 0
        
        if n == 1:  # Якщо n == 1
            return 1  # Повернути 1
        
        if n in cache:  # Якщо n у cache
            return cache[n]  # Повернути cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n] 
 
    return fibonacci  # Повернути fibonacci


