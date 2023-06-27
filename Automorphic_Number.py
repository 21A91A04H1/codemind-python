def is_automorphic(n):
    square = n**2
    original_digits=str(n)
    square_digits=str(square)[-len(original_digits):]
    return original_digits==square_digits
n=int(input())
if is_automorphic(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")