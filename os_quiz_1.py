# 전체 디렉토리 트리 탐색 및 파일과 디렉토리 개수 계산

import os

def count_files_and_directories(path):
    dircnt = 0
    filecnt = 0
    for path, dirnames, filenames in os.walk(path):
        dircnt += len(dirnames)
        filecnt += len(filenames)
    return dircnt, filecnt

if __name__ == "__main__":
    dir_path = input("디렉터리 경로를 입력하세요: ")
    dircnt, filecnt = count_files_and_directories(dir_path)
    
    print(f"전체 파일의 개수: {filecnt}")
    print(f"전체 서브디렉터리의 개수: {dircnt}")