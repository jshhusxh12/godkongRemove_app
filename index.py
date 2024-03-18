import os
import signal
import subprocess

process_name = "notepad.exe"

def kill_process(name):
    try:
        cmd = f'tasklist /fi "imagename eq {name}"'
        output = subprocess.check_output(cmd, shell=True, text=True)

        if name in output:
            print(f"{name} 프로세스를 찾았습니다. 종료를 시도합니다.")
            os.system(f'taskkill /f /im {name}')
        else:
            print(f"{name} 프로세스가 실행 중이지 않습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

kill_process(process_name)
