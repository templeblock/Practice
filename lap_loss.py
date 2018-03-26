def lap_loss(matrix, output):
# 把output矩阵拉直
    output = tf.reshape(output[:,:,:,0]/255, [-1,1])
# 矩阵乘法过程是 V[O].T * Laplacian * V[O]
# 则是一个 （1, height*width）* (height*width, height*width) * (height*width, 1）
# 因为Laplacian 矩阵太大，因此以dense的矩阵去做乘法，那么需要很多的内存空间，
# 因此用tensorflow的embedding_lookup_sparse来节约存储空间，提高运算效率、
# 该乘法先计算后半段，把param矩阵就是output矩阵，tf embedding中的weight为laplacian矩阵
    matrix_sp_indices = matrix.indices
    sp_indices = matrix_sp_indices
    
    matrix_sp_weights_val = matrix.values
    sp_weights_val = matrix_sp_weights_val
    
    d = matrix_sp_indices.get_shape().as_list()
    c_d = d[0]
    
    matrix_sp_ids_val = tf.slice(matrix_sp_indices, [0,1], [c_d, 1])
    matrix_sp_ids_val = tf.reshape(matrix_sp_ids_val, (c_d, ))
    sp_ids_val = matrix_sp_ids_val
    
    sp_shape = [image_height**2, image_width**2]
    
    sp_ids = tf.SparseTensor(sp_indices, sp_ids_val, sp_shape)
    sp_weights = tf.SparseTensor(sp_indices, sp_weights_val, sp_shape)    
    
#    print('1')   
    result = tf.nn.embedding_lookup_sparse(output.eval(), sp_ids, sp_weights, combiner= "sum") 
# 之前的方式
#         result = tf.matmul(output, tf.sparse_tensor_to_dense(matrix,0.0, validate_indices= False), 
#                            a_is_sparse= True, b_is_sparse= True)        
#    print('2')  
    loss = tf.sparse_matmul(output, result, transpose_a=True, 
                         transpose_b=False, a_is_sparse=True, b_is_sparse=True)
#     output = tf.squeeze(output)
#     output = output[:,:,0].flatten()
#     output_T = np.array([output]).T
#     loss = output.dot(matrix).dot(output_T)
    return loss

shape = [image_height**2,image_width**2]
shape = np.array(shape, dtype=np.int64)
place = tf.sparse_placeholder(dtype = tf.float32, shape = shape)

csr_lap_matrix = computeLaplacian(content_image)

tf_csr_lap_matrix = tf.SparseTensor(
    indices = np.array([csr_lap_matrix.tocoo().row, csr_lap_matrix.tocoo().col]).T,
    values = csr_lap_matrix.data, 
    shape = csr_lap_matrix.shape)
