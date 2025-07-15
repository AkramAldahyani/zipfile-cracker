import zipfile
import os
import time
from termcolor import colored

def print_banner():
    """Display a colorful banner"""
    print(colored("""
   ███████╗██╗██████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗
   ╚══███╔╝██║██╔══██╗   ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
     ███╔╝ ██║██████╔╝   ██║     ██████╔╝███████║██║     █████╔╝ 
    ███╔╝  ██║██╔═══╝    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
   ███████╗██║██║        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
   ╚══════╝╚═╝╚═╝         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """, 'cyan'))
    print(colored("🔐 ZIP 4-Digit Brute-Force Cracker v2.0", 'yellow'))
    print(colored("⚠ For educational and legal use only\n", 'red'))



def crack_zip(zip_file):
    """Try all 4-digit passwords on a ZIP file"""
    start_time = time.time()
    attempts = 0
    
    print(colored(f"\n🔓 Target: {zip_file}", 'blue'))
    print(colored("🔢 Trying all 4-digit combinations (0000-9999)...\n", 'magenta'))
    
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for i in range(10000):
                password = f"{i:04d}"
                attempts += 1
                
                # Show progress every 250 attempts
                if i % 250 == 0:
                    progress = i / 100
                    print(colored(f"⏳ Progress: {progress}% | Trying: {password}", 'yellow'))
                
                try:
                    zip_ref.extractall(pwd=password.encode())
                    end_time = time.time()
                    elapsed = end_time - start_time
                    
                    print(colored(f"\n🎉 SUCCESS! Password found: {password}", 'green'))
                    print(colored(f"📦 Files extracted to: {os.getcwd()}", 'green'))
                    print(colored(f"⏱ Time elapsed: {elapsed:.2f} seconds", 'green'))
                    print(colored(f"🔑 Attempts made: {attempts}", 'green'))
                    return True
                    
                except (RuntimeError, zipfile.BadZipFile):
                    continue
        
        print(colored("\n❌ No matching 4-digit password found", 'red'))
        return False
        
    except FileNotFoundError:
        print(colored("\n❌ Error: File not found!", 'red'))
        return False
    except zipfile.BadZipFile:
        print(colored("\n❌ Error: Invalid or corrupted ZIP file", 'red'))
        return False
    except Exception as e:
        print(colored(f"\n❌ Unexpected error: {str(e)}", 'red'))
        return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    zip_file = input(colored("📁 Enter ZIP file path: ", 'blue'))
    
    if not os.path.exists(zip_file):
        print(colored("\n❌ Error: File does not exist!", 'red'))
    else:
        crack_zip(zip_file)
    
    input(colored("\nPress Enter to exit...", 'yellow'))

if __name__ == "__main__":
    main()