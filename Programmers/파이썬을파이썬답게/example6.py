## 파일 읽는 법

with open('izone.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))

## 굳이 close 안해도 with 구문이 끝나면 자동으로 close

## 파일뿐만아니라 socket 이나 http에도 사용가능