import gspread
from google.oauth2.service_account import Credentials

# =========================
# KONEKSI GOOGLE SHEETS
# =========================

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open("database").sheet1


# =========================
# MEMBUAT HEADER
# =========================

if sheet.cell(1, 1).value == "":
    sheet.update("A1:B1", [["username", "password"]])


# =========================
# FUNGSI LOGIN
# =========================

def login(username, password):

    data = sheet.get_all_values()

    for baris in data[1:]:
        if len(baris) >= 2:
            if baris[0] == username and baris[1] == password:
                return True

    return False


# =========================
# FUNGSI BUAT AKUN
# =========================

def buat_akun(username, password):

    data = sheet.get_all_values()

    # Mengecek username
    for baris in data[1:]:
        if len(baris) >= 1:
            if baris[0] == username:
                return False

    # Menyimpan akun
    sheet.append_row([username, password])

    return True
