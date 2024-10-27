
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Tworzymy figurę i osie
fig, ax = plt.subplots()

# Ustawienia osi
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')                         # Ustawienie równych proporcji osi
ax.axis('off')

# ------ Rysowanie przedziału dla x<=4 ----------------------------------------------------------------
ax.annotate("", xy=(8, 5), xytext=(2, 5),
            arrowprops=dict(arrowstyle="->", color="blue", fill=False, linewidth=1))
# rysowanie punktu
circle = patches.Circle((5, 5), radius=0.08, edgecolor='blue', facecolor='blue', linewidth=0.7)
ax.add_patch(circle)

# Dodanie linii pionowej wychodzącej od środka kółka
x_center, y_center = 5, 5                      # Współrzędne środka kółka
ax.plot([x_center, x_center], [y_center, y_center + 0.7], color='blue', linewidth=1)

# Dodanie linii poziomej prostopadłej wychodzącej w lewo
x_end, y_end = x_center, y_center + 0.7        # Punkt końcowy linii pionowej
ax.plot([x_end - 3, x_end], [y_end, y_end], color='blue', linewidth=1)

# Wypełnienie przestrzeni między równoległymi liniami
ax.fill_between([x_center - 3, x_center], y_center, y_center + 0.7, color='lightgray', alpha=0.5)

# Dodanie cyfry "4" pod kółkiem
ax.text(5, 4.7, '4', color='blue', ha='center', va='top', fontsize=12)


# ------ Rysowanie przedziału dla x>4 --------------------------------------------------------------------
ax.annotate("", xy=(8, 3), xytext=(2, 3),
            arrowprops=dict(arrowstyle="->", color="blue", fill=False, linewidth=1))
circle = patches.Circle((5, 3), radius=0.08, edgecolor='blue', facecolor='none', linewidth=0.7)
ax.add_patch(circle)
x_center, y_center = 5, 3
ax.plot([x_center, x_center], [y_center, y_center + 0.7], color='blue', linewidth=1)
x_end, y_end = x_center, y_center + 0.7
ax.plot([x_end + 2.8, x_end], [y_end, y_end], color='blue', linewidth=1)
ax.text(5, 2.7, '4', color='blue', ha='center', va='top', fontsize=12)
ax.fill_between([x_center + 2.8, x_center], y_center, y_center + 0.7, color='lightgray', alpha=0.5)

# Wyświetlenie wykresu
plt.show()


