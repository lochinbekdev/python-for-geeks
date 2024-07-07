def generate(n: int) -> list:
    row = [1]
    result = [row]
    
    for i in range(n-1):
        row = generate_row(row)
        result.append(row)
        
    return result

def generate_row(row):
    new_row = [1]
    for i in range(1, len(row)):
        new_row.append(row[i-1] + row[i])
    new_row.append(1)
    return new_row

print(generate(5))