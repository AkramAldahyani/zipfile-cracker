import zipfile
import os

def crack_zip(zip_file):
    """Try all 4-digit passwords on a ZIP file"""
    
    print(f"Cracking {zip_file}...")
    print("Trying 4-digit passwords (0000-9999)...")
    
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for i in range(10000):
                password = f"{i:04d}"
                
                # Show progress every 500 attempts
                if i % 500 == 0:
                    print(f"Trying: {password}")
                
                try:
                    zip_ref.extractall(pwd=password.encode())
                    print(f"\n✓ SUCCESS! Password is: {password}")
                    print(f"Files extracted to current folder")
                    return True
                except:
                    continue
        
        print("\n✗ No 4-digit password worked")
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

# Main program
if __name__ == "__main__":
    zip_file = input("Enter ZIP file name: ")
    
    if not os.path.exists(zip_file):
        print("File not found!")
    else:
        crack_zip(zip_file)
    
    input("\nPress Enter to exit...")