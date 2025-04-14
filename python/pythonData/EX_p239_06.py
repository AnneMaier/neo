from pandas import Series
import matplotlib.pyplot as plt

# 폰트 설정 (한글 깨짐 방지)
plt.rcParams['font.family'] = 'NanumBarunGothic'

# 데이터
mylist = [30, 20, 40, 60]
myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주']
myseries = Series(data=mylist, index=myindex)

# 막대 그래프 그리기
ax = myseries.plot(kind='bar', rot=0, use_index=True, grid=False, table=False, color=['r', 'g', 'b', 'y', 'c'], figsize=(8, 6))  # 그래프 크기 조정

# 그래프 레이블 및 제목 설정
plt.xlabel('학생 이름', fontsize=12)
plt.ylabel('점수', fontsize=12)
plt.title('학생별 시험 점수', fontsize=14)

# Y축 범위 조정 (데이터가 잘 보이도록)
plt.ylim(0, myseries.max() + 10)

# 각 막대 위에 값 표시
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}점', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=10)

# 비율 계산 및 출력
ratio = 100 * myseries / myseries.sum()
print("각 학생 점수 비율:")
print(round(ratio, 1))
print('-' * 50)

# 각 막대 중간에 비율 표시
for idx in range(myseries.size):
    ratival = '%.1f' % ratio.iloc[idx] + '%'
    ax.text(x=idx, y=myseries.iloc[idx] / 2, s=ratival, ha='center', va='center', color='white', fontsize=9) # 위치 및 색상 조정

# 평균 점수 계산 및 출력
meanval = myseries.mean()
print(f"평균 점수: {meanval:.2f}점")
print('-' * 50)

# 평균 점수 수평선 그리기
ax.axhline(y=meanval, color='red', linestyle='--', linewidth=1, label=f'평균: {meanval:.2f}점')
plt.legend(fontsize=10) # 범례 표시

# 그래프 저장
filename = 'Ex_p239_06_Graph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(f"'{filename}' saved")

# 그래프 보여주기
plt.tight_layout() # 레이아웃 조정
plt.show()