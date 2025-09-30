import tensorflow as tf

rank1_tensor = tf.Variable(["Hello", "TensorFlow"], tf.string)
rank2_tensor = tf.Variable([["Hello", "TensorFlow"], ["I", "am"]], tf.string)


with tf.Session() as sess:
    rank1_tensor.eval()