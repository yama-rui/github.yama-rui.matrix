import numpy as np
class Rows_and_columns:
    def __init__(self):
        self.li = []
        self.true_rows = []
        self.rac = [] 
    def input_matrix(self):                                         #fanction to input a matrix
        self.rows = int(input("何行の行列ですか？"))
        self.culumns = int(input("何列の行列ですか？"))
        for i in range(self.rows):                                  #Loop as many times as there are rows
            print(str(i)+"行目")
            for j in range(self.culumns):                         #Loop as many times as there are culumns
                ts = input(str(j)+"列目を入力")
                self.li.append(ts)
            self.true_rows.append(self.li)
            self.li = []
        self.rac = np.matrix(self.true_rows)

def main():
    rc = Rows_and_columns()                                   #instance generation
    rc.input_matrix()                                                 
    print(rc.rac)


if __name__ == "__main__":
    main()
