def find_duplicate(nums=None):
    if nums is None:
        return False

    numeros_vistos = []

    for numero in nums:
        if isinstance(numero, str) or numero < 0:
            return False
        if numero in numeros_vistos:
            return numero
        numeros_vistos.append(numero)

    return False
