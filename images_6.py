
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
ax.annotate("", xy=(9, 5), xytext=(1, 5),
            arrowprops=dict(arrowstyle="->", color="blue", fill=False, linewidth=1))


# Dodanie linii pionowych
x_center1, y_center1 = 2, 5
ax.plot([x_center1, x_center1], [y_center1, y_center1 + 0.7], color='blue', linewidth=1)
x_center2, y_center2 = 4, 5
ax.plot([x_center2, x_center2], [y_center2, y_center2 + 0.95], color='blue', linewidth=1)
x_center3, y_center3 = 6, 5
ax.plot([x_center3, x_center3], [y_center3, y_center3 + 0.95], color='blue', linewidth=1)
x_center4, y_center4 = 8, 5
ax.plot([x_center4, x_center4], [y_center4, y_center4 + 0.7], color='blue', linewidth=1)

# Dodanie linii poziomej prostopadłej
x_end, y_end = x_center1, y_center1 + 0.7
ax.plot([x_end + 6, x_end], [y_end, y_end], color='blue', linewidth=1)
x_end, y_end = x_center2, y_center2 + 0.95
ax.plot([x_end - 3, x_end], [y_end, y_end], color='blue', linewidth=1)
x_end, y_end = x_center3, y_center3 + 0.95
ax.plot([x_end + 2.8, x_end], [y_end, y_end], color='blue', linewidth=1)

# Wypełnienie przestrzeni między równoległymi liniami
ax.fill_between([x_center1 + 6, x_center1], y_center1, y_center1 + 0.7, color='#D6D6D6', alpha=0.5)
ax.fill_between([x_center2 - 3, x_center2], y_center2, y_center2 + 0.95, color='#F5F5F5', alpha=0.5)
ax.fill_between([x_center3 + 3, x_center3], y_center3, y_center3 + 0.95, color='#F5F5F5', alpha=0.5)
ax.fill_between([x_center1 + 2, x_center1], y_center1, y_center1 + 0.95, color='#6D86CE', alpha=0.5)
ax.fill_between([x_center3 + 2, x_center3], y_center3, y_center3 + 0.95, color='#6D86CE', alpha=0.5)
# rysowanie punktu -3
circle = patches.Circle((2, 5), radius=0.08, edgecolor='blue', facecolor='none', linewidth=0.7)
ax.add_patch(circle)
# rysowanie punktu 2
circle = patches.Circle((4, 5), radius=0.08, edgecolor='blue', facecolor='blue', linewidth=0.7)
ax.add_patch(circle)
# rysowanie punktu 6
circle = patches.Circle((6, 5), radius=0.08, edgecolor='blue', facecolor='blue', linewidth=0.7)
ax.add_patch(circle)
# rysowanie punktu 11
circle = patches.Circle((8, 5), radius=0.08, edgecolor='blue', facecolor='none', linewidth=0.7)
ax.add_patch(circle)
# Dodanie cyfry "4" pod kółkiem
ax.text(2, 4.8, '-3', color='blue', ha='center', va='top', fontsize=12)
ax.text(4, 4.8, '2', color='blue', ha='center', va='top', fontsize=12)
ax.text(6, 4.8, '6', color='blue', ha='center', va='top', fontsize=12)
ax.text(8, 4.8, '11', color='blue', ha='center', va='top', fontsize=12)

# Wyświetlenie wykresu
plt.show()


