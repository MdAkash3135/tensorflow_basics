import tensorflow as tf

tensor1 = tf.ones([1, 2, 3])
tensor2 = tf.reshape(tensor1, [2, 3, 1])

tensor3 = tf.reshape(tensor1, [3, -1])




print(" Tensor  1: ", tensor1)
print(" Tensor  2: ", tensor2)
print(" Tensor  3: ", tensor3)