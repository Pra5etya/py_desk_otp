import pyotp
import time

def main(): 
    while True: 
        # Membuat secret key
        key = pyotp.random_base32()
        # Membuat objek TOTP dengan interval yang disesuaikan
        gen_totp = pyotp.TOTP(key, interval = 10)
        # Mendapatkan token saat ini
        totp_token = gen_totp.now()

        print(f'Time-based OTP: {totp_token}')
        print(f'Next OTP token:  {round(gen_totp.interval)} seconds')

        # before input otp
        init_time = int(time.time())
        # input otp
        users = input("Input your OTP: \n")
        # after input otp
        current_time = int(time.time())

        # timestamp
        print(f'Current time \t: {current_time}')
        print(f'init time \t: {init_time}')

        # time difference
        time_div = current_time - init_time
        print(f'time difference : {time_div} seconds \n')
        
        if time_div >= 10: 
            time.sleep(1)
            print('OTP has been expired')
            time.sleep(1)

        else: 
            if users == totp_token: 
                time.sleep(2)
                print('OTP valid')
                break

            else: 
                time.sleep(2)
                print('OTP in-valid')
                break


if __name__ == "__main__":
    main()