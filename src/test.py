import copy
# from captcha_solver import CaptchaSolver
from types import SimpleNamespace
import requests, sys, argparse, os, datetime, time
from utils import generate_token_OTP, check_and_book, beep, BENEFICIARIES_URL, WARNING_BEEP_DURATION, \
    display_info_dict, save_user_info, collect_user_details, get_saved_user_info, confirm_and_proceed, book_appointment, \
    check_calendar_by_pincode, display_table, generate_captcha, BOOKING_URL, CAPTCHA_URL


def main():
    # solver = CaptchaSolver('twocaptcha', api_key='2captcha.com API HERE')
    base_request_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    # ==================================================FILL DETAILS HERE ==================================== #

    # Rahul
    details = {
        'beneficiaries': ['98989898989898'],
        'dose': 1,
        'center_id': 602643,
        'session_id': '11062928-8315-4ff5-96ce-bd90fdf45f3a',
        'slot': '12:00PM-03:00PM'
    }
    mobile = '9999999999'


    # ==================================================FILL DETAILS HERE ==================================== #

    token = generate_token_OTP(mobile, base_request_header)
    request_header = copy.deepcopy(base_request_header)
    request_header["Authorization"] = f"Bearer {token}"

    print(f'Booking with info: {details}')

    valid_captcha = True
    while valid_captcha:
        time.sleep(2)
        captcha = generate_captcha(request_header)
        details['captcha'] = captcha

        print('================================= ATTEMPTING BOOKING ==================================================')

        resp = requests.post(BOOKING_URL, headers=request_header, json=details)
        print(f'Booking Response Code: {resp.status_code}')
        print(f'Booking Response : {resp.text}')

        if resp.status_code == 401:
            print('TOKEN INVALID')
            token = generate_token_OTP(mobile, base_request_header)
            request_header = copy.deepcopy(base_request_header)
            request_header["Authorization"] = f"Bearer {token}"

        elif resp.status_code == 200:
            beep(WARNING_BEEP_DURATION[0], WARNING_BEEP_DURATION[1])
            print('##############    BOOKED!  ############################    BOOKED!  ##############')
            print("                        Hey, Hey, Hey! It's your lucky day!                       ")
            print('\nPress any key thrice to exit program.')
            os.system("pause")
            os.system("pause")
            os.system("pause")
            sys.exit()

        elif resp.status_code == 400:
            print(f'Response: {resp.status_code} : {resp.text}')
            pass

        else:
            print(f'Response: {resp.status_code} : {resp.text}')
            pass


if __name__ == '__main__':
    main()
9162725603
831004