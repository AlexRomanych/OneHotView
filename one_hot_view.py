import pandas as pd
import random
import os

os.system('cls')    # очистка консоли

# избавляемся от "магических" чисел
ROBOT_WORD  = 'robot'
HUMAN_WORD  = 'human'
COLUMN_NAME = 'whoAmI'
ITEM_AMOUNT = 10

lst =  [ROBOT_WORD] * ITEM_AMOUNT
lst += [HUMAN_WORD] * ITEM_AMOUNT

random.shuffle(lst)

df = pd.DataFrame({COLUMN_NAME:lst})


def sep_data():
    '''
        Отделяем данные
    '''
    print('', '_' * 68, '', sep='\n')


if __name__ == '__main__':

    print('________________________ Исходные данные: __________________________ ')
    print(df)
    sep_data()

    print('_______________ One Hot View Without get_dummies(): ________________ ')

    df.loc[df[COLUMN_NAME] == HUMAN_WORD, [HUMAN_WORD]] = (df[COLUMN_NAME] == HUMAN_WORD)
    df.loc[df[COLUMN_NAME] == ROBOT_WORD, [HUMAN_WORD]] = False

    df.loc[df[COLUMN_NAME] == ROBOT_WORD, [ROBOT_WORD]] = (df[COLUMN_NAME] == ROBOT_WORD)
    df.loc[df[COLUMN_NAME] == HUMAN_WORD, [ROBOT_WORD]] = False

    print(df[[HUMAN_WORD, ROBOT_WORD]])
    sep_data()

    print('___________________ Проверочка: pd.get_dummies() ___________________ ')
    print(pd.get_dummies(df[COLUMN_NAME]))
    sep_data()
