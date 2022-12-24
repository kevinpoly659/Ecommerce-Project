import os


AWS_QUERYSTRING_AUTH = False

AWS_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY_ID")


AWS_STORAGE_BUCKET_NAME = "kevinpoly"

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'ecommerce.cdn.backends.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'ecommerce.cdn.backends.StaticRootS3BotoStorage'

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
