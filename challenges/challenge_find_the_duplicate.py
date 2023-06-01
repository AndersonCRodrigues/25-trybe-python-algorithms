def find_duplicate(nums=None):
    if nums is None or len(nums) <= 1:
        return False

    numeros_vistos = set()

    for numero in nums:
        if isinstance(numero, str) or numero < 0:
            return False
        if numero in numeros_vistos:
            return numero
        numeros_vistos.add(numero)

    return False
