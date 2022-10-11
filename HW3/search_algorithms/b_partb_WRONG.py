# Implement occupancy gridmap-based Dijkstra for same functionality as 1a
from gridmap import OccupancyGridMap
from tkinter import *
import quadtreemap as qtm
import dijkstra_quadtree as dq

canvas_width = 425
canvas_height = 420
start_m = (360.0, 330.0)
goal_m = (285.0, 86.0)
img_loc = "examples/maps/example_map_binary.png"
# qtm.QuadTreeMap
# gmap = OccupancyGridMap.from_png('examples/maps/example_map_occupancy.png', 1)
# result = a_star_occupancy(start_m, goal_m, gmap)
# MESS WITH
qtm_input = qtm.QuadTreeMap.from_png(img_loc)
# _get_movements_8n(qtm: quadtreemap.QuadTreeMap , tile: quadtreemap.Tile)
#move_8 = dq._get_movements_8n()
# result = dijkstra_quadtree(start_m, goal_m, qtm, movement='8n', occupancy_cost_factor=3)
result = dq.dijkstra_quadtree(start_m, goal_m, qtm_input, "8N")
print(result)

window = Tk()
window.title("Occupance Map")

img = PhotoImage(file="examples/maps/example_map_occupancy.png")
cv = Canvas(window, width=canvas_width, height=canvas_height)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=img, anchor='nw')

# cv.bind("<Button-1>", plan)

window.mainloop()
