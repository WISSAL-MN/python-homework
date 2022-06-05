from perception4e import *
from numpy import asarray
from PIL import Image
GI=Image.open('stapler1-test.png')
Tab = asarray(GI)

cont1 = gradient_edge_detector(Tab)
cont2 = gaussian_derivative_edge_detector (Tab)
cont3 = laplacian_edge_detector (Tab) 
show_edges (cont1)
show_edges (cont2)
show_edges (cont3)

