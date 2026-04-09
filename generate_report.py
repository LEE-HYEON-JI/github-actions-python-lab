from datatime import datetime

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("Github Actions Report\n")
    f.write("Generated on: {datetime.now()}\n")
print("REPORT.TXT 파일 생성 완료.")