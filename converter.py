from numpy import array
from PIL import Image
import matplotlib.pyplot as plt
import sys

def image_to_graph(image_name : str, pixel_size : float = 1) -> None:
    
    npdat = array(Image.open(sys.path[0]+'/'+image_name)).tolist()

    height = len(npdat)
    colors = {}

    # converts image to color dictionary
    for i in range(len(npdat)):
        for j in range(len(npdat[i])):
            
            name = ','.join([str(c//10*10) for c in npdat[i][j]])
            
            # adds color key if one doesnt exist
            if name not in colors: colors[name] = []
                
            colors[name].append((j, height - i))

    # converts color dictionary to graph
    for color, rgb_list in colors.items(): plt.scatter([c[0] for c in rgb_list], [c[1] for c in rgb_list], color = [int(c)/255 for c in color.split(',')], s = pixel_size)
        
    plt.show()
    
image_to_graph('joe.jpeg')