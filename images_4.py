
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Tworzymy figurę i osie
fig, ax = plt.subplots()

# Ustawienia osi
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')                         # Ustawienie równych proporcji osi
#ax.axis('off')

# ------ Rysowanie przedziału dla x<=4 ----------------------------------------------------------------
ax.annotate("", xy=(8, 5), xytext=(2, 5),
            arrowprops=dict(arrowstyle="->", color="blue", fill=False, linewidth=1))


# Dodanie linii pionowej wychodzącej od środka kółka
x_center1, y_center1 = 6, 5                      # Współrzędne środka kółka
ax.plot([x_center1, x_center1], [y_center1, y_center1 + 0.7], color='blue', linewidth=1)
# Dodanie linii pionowej wychodzącej od środka kółka
x_center2, y_center2 = 4, 5                      # Współrzędne środka kółka
ax.plot([x_center2, x_center2], [y_center2, y_center2 + 0.95], color='blue', linewidth=1)

# Dodanie linii poziomej prostopadłej wychodzącej w lewo
x_end, y_end = x_center2, y_center2 + 0.95        # Punkt końcowy linii pionowej
ax.plot([x_end + 3.8, x_end], [y_end, y_end], color='blue', linewidth=1)
# Dodanie linii poziomej prostopadłej wychodzącej w prawo
x_end, y_end = x_center1, y_center1 + 0.7        # Punkt końcowy linii pionowej
ax.plot([x_end - 3.95, x_end], [y_end, y_end], color='blue', linewidth=1)

# Wypełnienie przestrzeni między równoległymi liniami
ax.fill_between([x_center1 - 4, x_center1], y_center1, y_center1 + 0.7, color='#E0E0E0', alpha=0.5)
ax.fill_between([x_center2 + 3.8, x_center2], y_center2, y_center2 + 0.95, color='#B8B8B8', alpha=0.5)
ax.fill_between([x_center2 + 1.95, x_center2], y_center2, y_center2 + 0.95, color='#6D86CE', alpha=0.5)
# rysowanie punktu -3
circle = patches.Circle((4, 5), radius=0.08, edgecolor='blue', facecolor='none', linewidth=0.7)
ax.add_patch(circle)
# rysowanie punktu 4
circle = patches.Circle((6, 5), radius=0.08, edgecolor='blue', facecolor='blue', linewidth=0.7)
ax.add_patch(circle)
# Dodanie cyfry "4" pod kółkiem
ax.text(6, 4.8, '4', color='blue', ha='center', va='top', fontsize=12)
ax.text(4, 4.8, '-3', color='blue', ha='center', va='top', fontsize=12)



# ------ Rysowanie przedziału  ----------------------------------------------------------------
ax.annotate("", xy=(8, 3), xytext=(2, 3),
            arrowprops=dict(arrowstyle="->", color="blue", fill=False, linewidth=1))

# Dodanie linii pionowej wychodzącej od środka kółka
x_center1, y_center1 = 6, 3                      # Współrzędne środka kółka
ax.plot([x_center1, x_center1], [y_center1, y_center1 + 0.95], color='blue', linewidth=1)
# Dodanie linii pionowej wychodzącej od środka kółka
x_center2, y_center2 = 4, 3.1                      # Współrzędne środka kółka
ax.plot([x_center2, x_center2], [y_center2, y_center2 + 0.6], color='blue', linewidth=1)

# Dodanie linii poziomej prostopadłej wychodzącej w lewo
x_end, y_end = x_center2, y_center2 + 0.6        # Punkt końcowy linii pionowej
ax.plot([x_end + 3.8, x_end], [y_end, y_end], color='blue', linewidth=1)
# Dodanie linii poziomej prostopadłej wychodzącej w prawo
x_end, y_end = x_center1, y_center1 + 0.95        # Punkt końcowy linii pionowej
ax.plot([x_end - 3.9, x_end], [y_end, y_end], color='blue', linewidth=1)

# Wypełnienie przestrzeni między równoległymi liniami
ax.fill_between([x_center2 + 3.8, x_center2], y_center2-0.1, y_center2 + 0.6, color='#B8B8B8', alpha=0.5)
ax.fill_between([x_center1 - 3.9, x_center1], y_center1, y_center1 + 0.95, color='#E0E0E0', alpha=0.5)
ax.fill_between([x_center1 - 1.95, x_center1], y_center1, y_center1 + 0.95, color='#6D86CE', alpha=0.5)

# rysowanie punktu 11
circle = patches.Circle((6, 3), radius=0.08, edgecolor='blue', facecolor='none', linewidth=0.7)
ax.add_patch(circle)
# rysowanie punktu 4
circle = patches.Circle((4, 3), radius=0.08, edgecolor='blue', facecolor='white', linewidth=0.7)
ax.add_patch(circle)
# Dodanie cyfry "4" pod kółkiem
ax.text(6, 2.8, '11', color='blue', ha='center', va='top', fontsize=12)
ax.text(4, 2.8, '4', color='blue', ha='center', va='top', fontsize=12)
# Wyświetlenie wykresu
plt.show()


