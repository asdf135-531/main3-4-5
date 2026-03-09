import random
import numpy as np
import matplotlib.pyplot as plt


class Source:

    def manual(self):
        k = int(input("Число частиц k: "))
        m = int(input("Число энергетических линий: "))

        energies = []
        probs = []

        print("Введите энергии:")
        for i in range(m):
            e = float(input(f"E{i+1}: "))
            energies.append(e)

        print("Введите вероятности:")
        for i in range(m):
            p = float(input(f"P{i + 1}: "))
            probs.append(p)

        s = sum(probs)
        if abs(s - 1) > 1e-6:
            raise ValueError("Ошибка: сумма вероятностей должна быть равна 1")
        probs = [p/s for p in probs]

        N = [0]*m

        for _ in range(k):
            r = random.random()
            cumulative = 0
            for i in range(m):
                cumulative += probs[i]
                if r <= cumulative:
                    N[i] += 1
                    break

        errors = [np.sqrt(n) for n in N]
        plt.bar(energies, N)
        plt.errorbar(energies, N, yerr=errors, fmt='none', capsize=5)

        plt.xlabel("Энергия")
        plt.ylabel("Отн. число частиц")
        plt.title("Спектр")
        plt.show()

    def maxwell(self):
        k = int(input("Число частиц k: "))
        bins = int(input("Число столбцов гистограммы: "))
        sigma = float(input("Параметр sigma: "))

        vx = np.random.normal(0, sigma, k)
        vy = np.random.normal(0, sigma, k)
        vz = np.random.normal(0, sigma, k)

        energies = np.sqrt(vx ** 2 + vy ** 2 + vz ** 2)

        N, bins_edges = np.histogram(energies, bins=bins)

        centers = (bins_edges[:-1] + bins_edges[1:]) / 2
        errors = np.sqrt(N)

        plt.bar(centers, N, width=(bins_edges[1] - bins_edges[0]),
                color="skyblue", edgecolor="black")

        plt.errorbar(
            centers,
            N,
            yerr=errors,
            fmt='o',
            color='red',
            ecolor='red',
            elinewidth=2,
            capsize=6,
            capthick=2
        )

        plt.xlabel("Скорости")
        plt.ylabel("Отн. число частиц")
        plt.title("Maxwell")
        plt.show()


s = Source()
mode = input("Выберите режим (1 — ручной, 2 — Максвелл): ")
if mode == "1":
    s.manual()
else:
    s.maxwell()