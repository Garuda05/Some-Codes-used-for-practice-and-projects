import skimage
import skimage.feature
import skimage.viewer
import sys
import io

filename = sys.argv[1]
sigma = float(sys.argv[2])
low_threshold = float(sys.argv[3])
high_threshold = float(sys.argv[4])


image = skimage.io.imread(fname=filename, as_gray=True)
viewer = skimage.viewer(image=image)
viewer.show()



edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
)


viewer = skimage.viewer.ImageViewer(edges)
viewer.show()
