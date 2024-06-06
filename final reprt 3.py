import pandas as pd
from Levenshtein import distance as levenshtein_distance

# SimpleChatBot 클래스를 정의
class SimpleChatBot:
    # 초기화 메서드: 데이터를 로드하고, 질문과 답변을 저장
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    # 데이터를 CSV 파일에서 로드하는 메서드
    def load_data(self, filepath):
        # pandas를 사용하여 CSV 파일을 읽어옴
        data = pd.read_csv(filepath)
        # 'Q' 열을 질문 리스트로 변환
        questions = data['Q'].tolist()
        # 'A' 열을 답변 리스트로 변환
        answers = data['A'].tolist()
        # 질문과 답변 리스트를 반환
        return questions, answers

    # 입력 문장에 가장 적합한 답변을 찾는 메서드
    def find_best_answer(self, input_sentence):
        
        # 각 질문과 입력 문장의 레벤슈타인 거리를 계산
        distances = [levenshtein_distance(input_sentence, question) for question in self.questions]
        
        # 가장 짧은 레벤슈타인 거리를 가진 질문의 인덱스를 찾음
        best_match_index = distances.index(min(distances))
        
        # 가장 유사한 질문에 해당하는 답변을 반환
        return self.answers[best_match_index]

# 데이터 파일의 경로를 지정
filepath = 'ChatbotData.csv'

# 챗봇 객체를 생성
chatbot = SimpleChatBot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행
while True:
    # 사용자로부터 입력 문장을 받음
    input_sentence = input('You: ')
    
    # 입력 문장이 '종료'일 경우 루프를 종료
    if input_sentence.lower() == '종료':
        break
    
    # 입력 문장에 가장 적합한 답변을 찾음
    response = chatbot.find_best_answer(input_sentence)
    
    # 챗봇의 응답을 출력
    print('Chatbot:', response)