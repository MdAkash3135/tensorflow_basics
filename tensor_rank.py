import tensorflow as tf

rank1_tensor = tf.Variable(["Hello", "TensorFlow"], tf.string)
rank2_tensor = tf.Variable([["Hello", "TensorFlow"], ["I", "am"]], tf.string)

print("Rank 1 Tensor: ", tf.rank(rank1_tensor))
print("Rank 2 Tensor: ", tf.rank(rank2_tensor))

rank3_tensor = tf.Variable([[[[1], [2], [3]], [[4], [5], [6]]]], tf.int32)
print("Rank 3 Tensor: ", tf.rank(rank3_tensor))