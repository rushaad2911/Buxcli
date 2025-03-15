import subprocess
import shutil



def is_flutter_installed():
    
    print("Checking if flutter is installed")
    flutter_path = shutil.which("flutter")
    
    if flutter_path != None:
        try:
            # Run 'flutter --version' and capture the output
            flutter_path = shutil.which("flutter")
            result = subprocess.run([flutter_path, "--version"], capture_output=True, text=True, check=True)
            print("✅ Flutter is installed!")
            return True
        except:
            print("Error in getting flutter version")
            return False
    else:
        print("Flutter is not installed")
        
        
# Example usage
if __name__ == "__main__":
    is_flutter_installed()
