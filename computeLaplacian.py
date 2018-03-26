def computeLaplacian(img, eps = 10**(-7), win_rad = 1,):
#     img = tf.Variable(initial_value)
    win_size = (win_rad*2+1)**2
    h, w, d = img.shape
    c_h, c_w = h - win_rad - 1, w - win_rad -1
    win_diam = win_rad * 2 + 1
    
    indsM = np.arange(h*w).reshape((h,w))
    ravelImg = img.reshape(h*w,d)
    win_inds = rolling_block(indsM, block=(win_diam,win_diam))
    
    win_inds = win_inds.reshape(c_h, c_w, win_size)
    winI = ravelImg[win_inds]
    # mean of the intensities in the window 
    win_mu = np.mean(winI, axis=2, keepdims=True)
    # variance of the intensities in the window 
    win_var = np.einsum('...ji, ...jk->...ik', winI, winI)/win_size - np.einsum('...ji, ...jk->...ik', win_mu,win_mu)
    inv = np.linalg.inv(win_var+(eps/win_size)*np.eye(3))
    
    X = np.einsum('...ij,...jk->...ik',winI-win_mu, inv)
    vals = np.eye(win_size) - (1/win_size)*(1 + np.einsum('...ij, ...kj->...ik', X, winI- win_mu))
    nz_indsCol = np.tile(win_inds, win_size).ravel()
    nz_indsRow = np.repeat(win_inds, win_size).ravel()
    nz_indsVal = vals.ravel()
    #matting laplacian matrix
    L = scipy.sparse.csr_matrix((nz_indsVal, (nz_indsRow, nz_indsCol)), shape=(h*w, h*w), dtype= np.float32)
    L.sort_indices()
    return L
