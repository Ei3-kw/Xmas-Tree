import matplotlib.pyplot as plt
import matplotlib.patches as patches

_, graph = plt.subplots()

head = patches.Ellipse(xy=(0,0), width=5, height=7, angle=0, facecolor='black')
graph.add_patch(head)

left_ear = patches.Polygon([[-3,3], [-5,5], [-3,7]], closed=True, facecolor='black')
graph.add_patch(left_ear)

right_ear = patches.Polygon([[3,3], [5,5], [3,7]], closed=True, facecolor='black')
graph.add_patch(right_ear)

left_eye = patches.Circle(xy=(-1,1), radius=1, facecolor='white')
graph.add_patch(left_eye)

right_eye = patches.Circle(xy=(1,1), radius=1, facecolor='white')
graph.add_patch(right_eye)

left_pupil = patches.Circle(xy=(-1,1), radius=0.3, facecolor='black')
graph.add_patch(left_pupil)

right_pupil = patches.Circle(xy=(1,1), radius=0.3, facecolor='black')
graph.add_patch(right_pupil)

nose = patches.Polygon([[-1,-1], [0,-2], [1,-1]], closed=True, facecolor='black')
graph.add_patch(nose)

graph.set_xlim(-6,6)
graph.set_ylim(-4,7)

plt.show()
