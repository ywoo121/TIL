import sys

sys.path.append('..')
import numpy as np
from dataset import ptb
from common.util import most_similar, ppmi, create_co_matrix

window_size = 2
wordvec_size = 100

# 데이터 준비
corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)

print('동시발생 수 계산...')
C = create_co_matrix(corpus, vocab_size, window_size=window_size)

print('PPMI 계산...')
W = ppmi(C, verbose=True)

# SVD 계산
print('SVD 계산...')
use_randomized_svd = False  # 초기값 설정
U, S, V = None, None, None  # SVD 결과 초기화

try:
    # sklearn의 randomized_svd를 사용할 수 있는지 확인
    from sklearn.utils.extmath import randomized_svd
    use_randomized_svd = True
    print('### calculating SVD using sklearn ###')
except ImportError:
    print('### sklearn not available, using np.linalg.svd ###')

# SVD 수행
if use_randomized_svd:
    # sklearn 사용
    U, S, V = randomized_svd(W, n_components=wordvec_size, n_iter=5, random_state=None)
else:
    # numpy 사용
    U, S, V = np.linalg.svd(W)

# 단어 벡터 추출
word_vecs = U[:, :wordvec_size]

# 유사 단어 검색
querys = ['you', 'year', 'car', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)