import tensorflow as tf

rank1_tensor = tf.Variable(["Hello", "TensorFlow"], tf.string)
rank2_tensor = tf.Variable([["Hello", "TensorFlow"], ["I", "am"], ["learning", "TensorFlow"]], tf.string)

print("Shape 1 Tensor: ", tf.shape(rank1_tensor))
print("Shape 2 Tensor: ", tf.shape(rank2_tensor))

rank3_tensor = tf.Variable([[[[1], [2], [3]], [[4], [5], [6]]]], tf.int32)
print("Shape 3 Tensor: ", tf.shape(rank3_tensor))