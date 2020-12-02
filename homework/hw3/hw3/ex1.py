import pandas as pd
import matplotlib.pyplot as plt

class SIR:
    def __init__(self, steps=150, S=999, I=1, R=0, beta=0.2, delta=0.1):
        self.S = S
        self.I = I
        self.R = R
        self.beta = beta
        self.delta = delta
        self.steps = steps

    def run(self):
        S = [self.S]
        I = [self.I]
        R = [self.R]
        N = self.S + self.I + self.R

        for step in range(1, self.steps):
            S_to_I = (self.beta * S[-1] * I[-1]) / N
            I_to_R = I[-1] * self.delta
            S.append(S[-1] - S_to_I)
            I.append(I[-1] + S_to_I - I_to_R)
            R.append(R[-1] + I_to_R)

        results = pd.DataFrame.from_dict({'Time': list(range(len(S))),
                                               'Susceptible': S,
                                               'Infected': I,
                                               'Resistant': R},
                                              orient='index').transpose()

        plt.plot(results['Time'], results['Susceptible'], color='blue')
        plt.plot(results['Time'], results['Infected'], color='red')
        plt.plot(results['Time'], results['Resistant'], color='green')

        plt.legend(['Susceptible', 'Infected', 'Resistant'], prop={'size': 10}, loc='upper center',
                   bbox_to_anchor=(0.5, 1.02), ncol=1, fancybox=True, shadow=False)
        plt.title(r'$\beta = {0}, \delta = {1}$'.format(self.beta, self.delta))
        plt.xlabel('Time')
        plt.ylabel('Population')
        plt.savefig('SIR.png')
        plt.show()
        plt.close()


if __name__ == '__main__':
    m = SIR()
    m.run()
