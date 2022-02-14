import math
import struct
import time
import random
import rng

class Interview(object):
    def __init__(self):
        self.quiz = Quiz()
        #stuff

class Quiz(object):
    def __init__(self):
        self.questions = []
        self.correct = 0
        self.lastOption = False
        self.seed = time.time()
    
    def generateQuestions(self):
        i = 0
        while i < 21:
            quiz = Question()
            if not self.lastOption: quiz.setCorrectAnswer(self.seed)
            else: quiz.setCorrectAnswer(True)
            self.questions.append(quiz)
            self.seed += 1
            i += 1

    def completeQuiz(self):
        for quiz in self.questions:
            # candidateAnswer = rng.random_uniform_sample_integer(1, (0, 5), self.seed)[0]
            candidateAnswer = random.randrange(0, 6)
            # print(quiz.correctAnswer)
            correctAnswer = quiz.correctAnswer
            # print('answer:', candidateAnswer, "correct answer:", correctAnswer)
            if (candidateAnswer == correctAnswer): self.correct += 1
            self.seed += 1

    def setLastOption(self, value=False):
        self.lastOption = value

    def reset(self):
        self.questions = []
        self.correct = 0
    

class Question(object):
    def __init__(self):
        self.correctAnswer = 0
#    def setCorrectAnswer(self, seed=time.time()):
       # self.correctAnswer = 

    def setCorrectAnswer(self, seed, answer=False):
        # if answer == False: self.correctAnswer = rng.random_uniform_sample_integer(1, (0, 5))[0]
        if answer == False: self.correctAnswer = random.randrange(0, 6)
        else: self.correctAnswer = 5


def main():
    interviews = []
    correct=[]
    count = 0
    numCorrect = 0
    numAsked = 0

    length = int(input('Input the number of interviews to run: '))

    while count < length:
        interview = Interview()
        print('quiz:', count)
        interview.quiz.generateQuestions()
        interview.quiz.completeQuiz()
        interviews.append(interview)
        numCorrect += interview.quiz.correct
        correct.append(interview.quiz.correct)
        print(str(interview.quiz.correct) + "/20")
        interview.quiz.reset()
        numAsked += 20
        count += 1
    
    averageRight = numCorrect / numAsked
    averageRightPercentage = averageRight * 100
    print('average percentage of questions answered correctly:', averageRightPercentage)
    print('average number right:', averageRight)
    print('max value:', max(correct))
    print('min correct:', min(correct))



if __name__ == "__main__":
    main()