import random #buat import random untuk fungsi random which is buat random angka
MAX_LINES = 3 # jumlah maksimum baris yang bisa dipilih ga bisa diubah
MAX_BET = 100
MIN_BET = 1
ROWS = 3 # jumlah baris yang ada di slot game ga bisa diubah
COLS = 3 # jumlah kolom yang ada di slot game ga bisa diubah

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,

}


symbol_value= {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,

}

def check_winnings(columns,Lines,bet,value):
    winnings=0 # inisialisasi winnings
    winning_lines = []
    # columns: list of columns, each column is a list of symbols
    for line in range(Lines):
        symbol=columns[0][line] # ambil simbol dari kolom pertama
        for column in columns: # loop untuk setiap kolom
            symbol_to_check = column[line] # ambil simbol dari kolom saat ini
            if symbol != symbol_to_check: # jika simbol tidak sama
                break # keluar dari loop jika ada simbol yang tidak sama
        else: # jika semua simbol sama
            winnings += value[symbol] * bet # tambahkan winnings sesuai dengan nilai simbol dan taruhan
            winning_lines.append(line + 1) # tambahkan baris kemenangan ke daftar winning_lines
    return winnings,winning_lines # kembalikan total winnings
#   fungsi untuk mendapatkan spin dari slot machine         
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
#   fungsi untuk mencetak slot machine
#   fungsi ini akan mencetak setiap kolom dari slot machine 

def print_slot_machine(columns):
    for row in range (len(columns[0])): # loop untuk setiap baris
        for i, column in enumerate(columns): # loop untuk setiap kolom
            if i != len(columns) -1 : # jika bukan kolom terakhir
                print(column[row], end=" | ")
            else: # jika kolom terakhir
                print(column[row], ) 
    
    print() # untuk pindah ke baris berikutnya

#   fungsi untuk deposit
#   fungsi ini akan meminta user untuk memasukkan jumlah deposit    
def deposit():# fungsi untuk deposit
    while True:# loop untuk validasi input 
        amount = input("Masukkan jumlah deposit:$ ")# input jumlah deposit
        if amount.isdigit():# cek apakah input berupa angka
            amount= int(amount) 
            if amount > 0:
                break
            else:
                print("Jumlah deposit harus lebih dari 0. $")
        else:
            print("input tidak valid. Silakan masukkan angka yang benar.")
    
    return amount # kembalikan nilai amount yang sudah valid


#fungsi untuk mendapatkan jumlah Lines dari user
# fungsi ini akan meminta user untuk memasukkan jumlah Lines yang ingin di bet

def get_number_of_Lines():
    while True:# loop untuk validasi input 
        Lines = input("Masukkan jumlah Lines untuk di bet   (1-" + str(MAX_LINES)+")? ")# input jumlah Lines
        if Lines.isdigit():# cek apakah input berupa angka
            Lines= int(Lines) 
            if  1 <= Lines <= MAX_LINES :
                break
            else:
                print("Enter Jumlah lines yang valid.")
        else:
            print("input tidak valid. Silakan masukkan angka yang benar.")
    
    return Lines # kembalikan nilai amount yang sudah valid
#fungsi untuk mendapatkan jumlah taruhan dari user
# fungsi ini akan meminta user untuk memasukkan jumlah taruhan per baris
def get_bet():
    while True:# loop untuk validasi input 
        amount = input("Berapa yang ingin anda taruh duit di setiap line:$ ")# input jumlah deposit
        if amount.isdigit():# cek apakah input berupa angka
            amount= int(amount) 
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print( f"Jumlah deposit harus minimal ${MIN_BET}-${MAX_BET}. ")
        else:
            print("input tidak valid. Silakan masukkan angka yang benar.")
    
    return amount # kembalikan nilai amount yang sudah valid
#fungsi untuk spin slot machine
# fungsi ini menerima parameter balance untuk mengecek apakah saldo cukup untuk taruhan
def spin(balance):  # tambahkan parameter balance
    Lines = get_number_of_Lines()
    while True:
        bet = get_bet()
        total_bet = bet * Lines
        if total_bet > balance:
            print(f"saldo anda ga cukup untuk taruah ${total_bet} XD YGy")
        else:
            break
    print(f"Total taruhan anda adalah ${total_bet} untuk {Lines} baris.SETARA DENGAN ${bet} PER BARIS")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, Lines, bet, symbol_value)
    print(f"Anda menang ${winnings}")
    print(f"Anda menang di baris:", *winning_lines)
    return winnings - total_bet
#fungsi nya untuk menjalankan game
def main():
    balance = deposit()
    while True:
        print(f"Saldo anda adalah ${balance}")
        spin_input = input("Tekan enter untuk spin (atau ketik 'q' untuk keluar): ")
        if spin_input == 'q':
            break
        balance += spin(balance)  # kirim balance ke spin
        print(f"Saldo anda sekarang adalah ${balance}")

main()