import numpy as np

# arr_outcomes = np.load('../processed_data/arr_outcomes.npy', allow_pickle=True)

"""Use 8:1:1 split"""
p_train = 0.80
p_val = 0.10
p_test = 0.10

n = 11988  # original 12000 patients, remove 12 outliers
n_train = round(n*p_train)
n_val = round(n*p_val)
n_test = n - (n_train+n_val)
Nsplits = 5
for j in range(Nsplits):
    print(j)
    p = np.random.permutation(n)
    idx_train = p[:n_train]
    idx_val = p[n_train:n_train+n_val]
    idx_test = p[n_train+n_val:]
    print(idx_train.shape, idx_test.shape, idx_val.shape)
    np.save('/home/gaurang/Raindrop/P12data/splits/phy12_split_subset'+str(j+1)+'.npy', (idx_train, idx_val, idx_test))
print('split IDs saved')
