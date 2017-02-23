import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
import numpy as np


def imageprepare(argv):
    """
    This function returns the pixel values.
    The input is a png file location.
    """
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255)) #creates white canvas of 28x28 pixels

    if width > height: #check which dimension is bigger
        #Width is bigger. Width becomes 20 pixels.
        nheight = int(round((20.0/width*height), 0)) #resize height according to ratio width
        if (nheight == 0): #rare case but minimum is 1 pixel
            nheight = 1
            # resize and sharpen
        img = im.resize((20,nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight)/2), 0)) #caculate horizontal pozition
        newImage.paste(img, (4, wtop)) #paste resized image on white canvas
    else:
        #Height is bigger. Heigth becomes 20 pixels.
        nwidth = int(round((20.0/height*width), 0)) #resize width according to ratio height
        if (nwidth == 0): #rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth)/2), 0)) #caculate vertical pozition
        newImage.paste(img, (wleft, 4)) #paste resized image on white canvas

    #newImage.save("sample.png")

    tv = list(newImage.getdata()) #get pixel values
    #tv = list(im.getdata())

    #normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255-x)*1.0/255.0 for x in tv]
    npa = np.array(tva)
    print(npa)
    return npa


#import data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init_op = tf.initialize_all_variables()


# Train the model and save the model to disk as a model.ckpt file
# file is stored in the same directory as this python script is started
"""
The use of 'with tf.Session() as sess:' is taken from the Tensor flow documentation
on on saving and restoring variables.
https://www.tensorflow.org/versions/master/how_tos/variables/index.html
"""
with tf.Session() as sess:
    sess.run(init_op)
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

    img = imageprepare("test-images/1/im10000.png")

    classification = sess.run(tf.argmax(y, 1), feed_dict={x: [img]})
    plt.imshow(img.reshape(28, 28), cmap=plt.cm.binary)
    plt.show()
    print('Number is ', classification[0])

