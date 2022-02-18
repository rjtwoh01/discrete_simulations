import math
import struct
import time
import random
import rng
import distutils

class Interview(object):
    def __init__(self,lastOption=False):
        self.quiz = Quiz(lastOption)
        #stuff

class Quiz(object):
    def __init__(self, lastOption=False):
        self.questions = []
        self.correct = 0
        self.lastOption = lastOption
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
    lastOption = distutils.util.strtobool(input('Last answer always true?: '))

    while count < length:
        interview = Interview(lastOption)
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
    
    probabilityRight = numCorrect / numAsked
    probRightPercent = probabilityRight * 100
    averageRight = numCorrect / len(correct)
    print('percentage of questions answered correctly:', probRightPercent)
    print('prob right:', probabilityRight)
    print('average right:', averageRight)
    print('max value:', max(correct))
    print('min correct:', min(correct))



if __name__ == "__main__":
    main()