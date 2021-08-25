fname = 'recipes.txt'

try:
    f = open(fname, 'x')
    f.write('Meatballs\n')
    f.close()
except FileExistsError as err:
    print(f"The {fname} file already exists")
except:
    print(f"Unable to write to the file")
else:
    print(f"Wrote to {fname}")
finally:
    print("Execution completed")
