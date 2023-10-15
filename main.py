import subprocess

def run_app_py():
    try:
        subprocess.run(['python', 'app.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running app.py: {e}")

if __name__ == '__main__':
    run_app_py()
