def triangle(style, size):
    
    air_size = size * 2
    size += 1
    real_style = str(style) + " "
    
    for i in range(0, size):
        print(f"{real_style*i: ^{air_size}}")
        
    print()

triangle("#", 100)