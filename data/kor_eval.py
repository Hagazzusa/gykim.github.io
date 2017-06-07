import sys

answer = [
    [5126],
    [3325, 3330],
    [728, 726],
    [1001, 1196, 2025],
    [3422],
    [2130, 2131, 2132],
    [407],
    [4587, 4588],
    [3911],
    [3891],
    [4564],
    [3885],
    [3950, 1570, 71],
    [5029],
    [1910, 1911, 1883, 1884, 1885],
    [4304, 4305],
    [836, 3952],
    [4688],
    [4127],
    [2838, 4743, 5051, 2802]
]
            
def calc(pred, ans, top=20):
    all_ans = 0
    for qn in ans:
        for temp in qn:
            all_ans += 1
    tp = 0.
    fp = 0.
    fn = 0.
    tn = 0.
    for idx in range(0, 20):
        for prediction in pred[idx][:top]:
            if prediction in ans[idx]: tp += 1
            else: fp += 1
        for answer in ans[idx]:
            if answer not in pred[idx][:top]: fn += 1
            
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    
    return precision, recall
            
if __name__ == '__main__':
    pred = [ [] for i in range(20)]
    with open(sys.argv[1]) as f:
        for line in f:
            temp = line.split()
            pred[int(temp[0])-1].append(int(temp[1]))
    p, r = calc(pred, answer, 20)
    print "top 20 precision : ", p
    print "top 20 recall : ", r
            