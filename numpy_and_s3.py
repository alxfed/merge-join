# -*- coding: utf-8 -*-
"""...
"""
import numpy as np
import pickle
from s3fs.core import S3FileSystem
s3 = S3FileSystem()

def saveLabelsToS3(npyArray, name):
    with s3.open('{}/{}'.format(bucket, name), 'wb') as f:
        f.write(pickle.dumps(npyArray))

def readLabelsFromS3(name):
    return np.load(s3.open('{}/{}'.format(bucket, name)), allow_pickle=True)

# Use as below
saveLabelsToS3(labels, 'folder/filename.pkl')
labels = readLabelsFromS3('folder/filename.pkl')


def main():



    image_width = 300
    image_height = 300
    channels = 3
    bytes_per_image = 1314732  # the number of bytes used to store the array for a single image
    start_reading_from = 5  # we'll skip the first five images
    batch_size_to_read = 10  # we'll read 10 images

    with s3.open('{}/{}'.format(bucket, key)) as f:
        f.seek(start_reading_from * bytes_per_image)
        bytes = f.read(bytes_per_image * batch_size_to_read)
        ar = np.frombuffer(bytes, dtype="float32").copy()
        ar = ar.reshape((-1, image_width, image_height, channels))

        # ...do stuff
    return


if __name__ == '__main__':
    main()
    print('\ndone')
