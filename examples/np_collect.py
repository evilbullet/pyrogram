import h5py
import numpy as np

a = [[12],[15],[111], ['222'], [0]]
a[3] = np.array(a[3]).astype('|S126')
# a = tmp

a = [a] * 5

h5f = h5py.File('data5.h5', 'w')

channel_name='memlrd'

h5f.create_dataset(channel_name, data=a)
h5f.attrs['columns_titles']=[['views_number'],['date_stamp'],['post_id'],
                             ['image_id'],['is_posted']]
# print(type(h5f.attrs['meta']))
h5f.close()

f = h5py.File('data5.h5', "r")
print(f.attrs['columns_titles'])
n1 = f.get(channel_name)
n1 = np.array(n1)
for x in n1:#['history']:
    print(n1)

# H = [x for x in f]