# 디렉토리 파일 모니터링 시스템 구현 - 단계1

import os
import time

def monitoring(path):
    mntset_original = set(os.listdir(path))
    new_file_list = []
    while True:
        mntset_new = set(os.listdir(path)) # 해당 경로의 디렉토리 및 파일을 탐색하여 집합으로 유지
        print(f"반복적 모니터링: {mntset_new}\n")
        new_contents = list(mntset_new.difference(mntset_original)) # 새로 생성된 디렉토리 혹은 파일을 저장할 리스트
        print(f"새로 생긴 디렉토리 혹은 파일 목록: {new_contents}\n")
        if mntset_original != mntset_new: 
            mntset_original = mntset_new # 집합의 변화가 생겼다면, 업데이트!!
        for content in new_contents:
            if os.path.isfile(os.path.join(path,content)):
                new_file_list.append(os.path.join(path,content))
                print("!!!!!!!!!!!!!!!================================!!!!!!!!!!!!!!!")
                print(f"새로운 파일 {os.path.join(path,content)} 이 감지되었습니다.\n")
                print(f"실행 후 새로 추가된 파일 목록: {new_file_list}\n")
                print("!!!!!!!!!!!!!!!================================!!!!!!!!!!!!!!!")
        
        time.sleep(5)
        


if __name__ == "__main__":
    input_path = input("지속적으로 모니터링할 경로를 입력하세요: ")
    monitoring(input_path)
    