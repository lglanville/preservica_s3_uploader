import sys
import boto3


def get_client(bucketpath):
    """Get the thing that uploads files to bucketpath"""
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucketpath)
    return bucket


def clear_bucket(bucketpath):
    c = get_client(bucketpath)
    for o in c.objects.all():
        obj = o.get()
        print(
            'Deleting',
            obj['Metadata'].get('key'),
            obj['Metadata'].get('name'))
        o.delete()


if __name__ == '__main__':
    clear_bucket(sys.argv[1])
