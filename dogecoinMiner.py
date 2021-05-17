from hashlib import sha256
from typing import Text

MAX_NONCE = 100000000000

def convert(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_num, transactions, previous_hash, difficulty):
    prefixString= '0'*difficulty
    for nonce in range(MAX_NONCE):
        text = str(block_num) + transactions + previous_hash + str(nonce)
        newHash=convert(text)
        if newHash.startswith(prefixString):
            print(f"10 Dogecoin berhasil ditambang!")
            print(f"Ditambang di nonce :{nonce}")
            return newHash
    
    raise BaseException(f"Tidak dapat menemukan nonce walaupun sudah mencoba {MAX_NONCE} percobaan")



if __name__=='__main__':
    print("===========================================\n\n")
    print("       DOGECOIN BLOCKCHAIN MINER")
    print("             by: Andru Baskara\n\n")
    print("===========================================\n\n")

    block_num= int(input("Masukan nomor block >> "))
    transactions= input("Isi detail transaksi (beri (|) sebagai pemisah antar transaksi) >> ")
    previous_hash=input("Input kode hash >> ")
    difficulty= int(input("Input tingkat kesulitan >> "))

    import time
    start=time.time()
    print("Mulai menambang......")
    print("Sedang menambang.....(lama proses penambangan berdasarkan kemampuan hardware dan tingkat kesulitan)\n\n")


    newHash=mine(block_num,transactions,previous_hash,difficulty)

    totalTime=str((time.time() - start))
    print(f"\nPenambangan telah diselesaikan dalam  {totalTime} detik")
    print("current hash : ",newHash)