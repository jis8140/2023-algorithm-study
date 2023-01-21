# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기
from collections import defaultdict

report_dict = defaultdict(list)
stop_dict = defaultdict(list)
id_report_number_dict = defaultdict(int)
result_dict = defaultdict(int)
id_dict = defaultdict(int)

# 초기화


def init(reports):
    for report in reports:
        reporter, reported = report.split()
        if reported not in report_dict[reporter]:
            report_dict[reporter].append(reported)
            id_report_number_dict[reported] += 1
            stop_dict[reported].append(reporter)

# solution
# n: report 길이, m: id_list 길이 -> 시간 복잡도: O(n), 공간 복잡도: O(m)


def solution(id_list, report, k):
    answer = []
    init(report)

    for key in id_report_number_dict.keys():
        if id_report_number_dict[key] >= k:
            for person in stop_dict[key]:
                result_dict[person] += 1

    for person in id_list:
        answer.append(result_dict[person])

    return answer
