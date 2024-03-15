
print("Ingrese el nombre de una especie avistada en el ecosistema o 'fin' para terminar la entrada de datos.")

especies_counts = {}

while True:
    especies = input()
    if especies == "fin":
        break
    if especies in especies_counts:
        especies_counts[especies] += 1
    else:
        especies_counts[especies] = 1

most_common_especies = max(especies_counts, key=especies_counts.get)
most_common_count = especies_counts[most_common_especies]

print("\nInforme de avistamientos de especies:")
for especies, count in especies_counts.items():
    print(f"{especies}: {count}")

print(f"\nLa especie más común en el ecosistema es {most_common_especies} con {most_common_count} avistamientos.")
