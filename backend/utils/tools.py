import hashlib


def calculate_md5_path(file_path, chunk_size=8192):
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            md5.update(chunk)
    return md5.hexdigest()


def calculate_md5_raw(raw_bytes, chunk_size=8192):
    md5 = hashlib.md5()
    # with open(file_path, "rb") as f:
    #     while chunk := f.read(chunk_size):
    md5.update(raw_bytes)
    return md5.hexdigest()
