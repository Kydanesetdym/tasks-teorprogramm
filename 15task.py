def forecast_qubits(generations: list):
    coeffs = [generations[i] / generations[i-1] for i in range(1, len(generations))]
    rounded_coeffs = [round(c, 2) for c in coeffs]
    
    avg_rate = sum(coeffs) / len(coeffs)
    rounded_avg = round(avg_rate, 2)
    
    next_gen = round(generations[-1] * avg_rate)
    
    print(f"Поколения кубитов: {generations}")
    print(f"Коэффициенты роста: {rounded_coeffs}")
    print(f"Средний темп роста: x{rounded_avg:.2f}")
    print(f"Прогноз следующего поколения: ~{next_gen} кубитов")

if __name__ == "__main__":
    generations = [127, 433, 1121]
    forecast_qubits(generations)