import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-356 hash of the given arguments.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))

    # print(f"\n\nargs: {stringified_args}")
    
    joined_data =  "".join(stringified_args)
    
    # print(f"joined_data: {joined_data}")

    return hashlib.sha256(joined_data.encode("utf-8")).hexdigest()

def main():
    print(f"crypto_hash('one',2,[three]):{crypto_hash('one',2 ,[3])} \n")
    print(f"crypto_hash(2,'one',[three]):{crypto_hash(2,'one',[3])} \n")


if __name__ == "__main__":
    main()