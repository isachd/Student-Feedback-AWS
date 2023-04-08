import zlib
import hashlib

def sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def compress_and_verify(input_file, output_file):
    # Read and hash the input file data
    with open(input_file, "rb") as file:
        data = file.read()
    original_hash = sha256_hash(data)

    # Compress the data
    compressed_data = zlib.compress(data)

    # Write the compressed data to the output file
    with open(output_file, "wb") as file:
        file.write(compressed_data)

    # Decompress the data for verification
    decompressed_data = zlib.decompress(compressed_data)

    # Compute the hash of the decompressed data
    decompressed_hash = sha256_hash(decompressed_data)

    # Verify that the original and decompressed hashes match
    if original_hash == decompressed_hash:
        print("Data integrity verified")
    else:
        print("Data integrity check failed")

# Example usage
compress_and_verify("input.txt", "compressed_output.bin")
