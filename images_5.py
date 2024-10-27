
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Tworzymy figurę i osie
fig, ax = plt.subplots()

# Ustawienia osi
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')                         # Ustawienie równych proporcji osi
#ax.axis('off')

# ------ Rysowanie przedziału ----------------------------------------------------------------
ax.annotate("", xy=(8, 5), xytext=(2, 5),
            arrowprops=dict(arrowstyle="->", color="blue", fill=False, linewidth=1))
# rysowanie punktu 4
circle = patches.Circle((6, 5), radius=0.08, edgecolor='blue', facecolor='blue', linewidth=0.7)
ax.add_patch(circle)

# Dodanie linii pionowej wychodzącej od środka kółka
x_center1, y_center1 = 6, 5                      # Współrzędne środka kółka
ax.plot([x_center1, x_center1], [y_center1, y_center1 + 0.7], color='blue', linewidth=1)
# Dodanie linii pionowej wychodzącej od środka kółka
x_center2, y_center2 = 4, 5                      # Współrzędne środka kółka
ax.plot([x_center2, x_center2], [y_center2, y_center2 + 0.7], color='blue', linewidth=1)

# Dodanie linii poziomej prostopadłej
x_end, y_end = x_center2, y_center2 + 0.7        # Punkt końcowy linii pionowej
ax.plot([x_end + 1.95, x_end], [y_end, y_end], color='blue', linewidth=1)

# Wypełnienie przestrzeni między równoległymi liniami
ax.fill_between([x_center1 - 1.95, x_center1], y_center1, y_center1 + 0.7, color='#5672C8', alpha=0.5)

# rysowanie punktu 2
circle = patches.Circle((4, 5), radius=0.08, edgecolor='blue', facecolor='blue', linewidth=0.7)
ax.add_patch(circle)
# Dodanie cyfry "4" pod kółkiem
ax.text(6, 4.8, '11', color='blue', ha='center', va='top', fontsize=12)
ax.text(4, 4.8, '-3', color='blue', ha='center', va='top', fontsize=12)


# Wyświetlenie wykresu
plt.show()


