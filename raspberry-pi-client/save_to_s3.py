import boto3

if __name__ == '__main__':
    AWS_ACCESS_KEY = 'AKIAJJXPMJJP6CMFFKLQ'
    AWS_ACCESS_SECRET_KEY = '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'
    bucket_name = 'fras-store'

    key = "temp.png"
    folder_name = "public_folder"
    output_name = folder_name + "/" + "temp.png"

    s3 = boto3.client('s3')
    s3.upload_file(key, bucket_name, output_name, ExtraArgs={'ACL': 'public-read'})
